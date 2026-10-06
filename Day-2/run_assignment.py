import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

from dotenv import load_dotenv
from openai import OpenAI, APIError, APIConnectionError

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description="Save independent prompt comparisons; review scores manually.")
    parser.add_argument("--versions", default="selected")
    parser.add_argument("--cases", default="cases/development.json")
    parser.add_argument("--repeat", type=int, default=1)
    args = parser.parse_args()
    if args.repeat < 1:
        parser.error("--repeat must be positive")
    versions = [v.strip() for v in args.versions.split(",")]
    if any(v not in {"V0", "V1", "V2", "V3", "V4", "V5", "selected"} for v in versions):
        parser.error("Versions must be V0 through V5 or selected")
    # Explicit project-local path; never print secrets.
    load_dotenv(ROOT / ".env")
    required = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_BASE_URL", "AZURE_OPENAI_DEPLOYMENT"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise SystemExit("Missing .env settings: " + ", ".join(missing))
    base_url = os.environ["AZURE_OPENAI_BASE_URL"].rstrip("/") + "/"
    if not base_url.startswith("https://") or not base_url.endswith("/openai/v1/"):
        raise SystemExit("Use the HTTPS resource inference URL ending /openai/v1/.")
    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    client = OpenAI(api_key=os.environ["AZURE_OPENAI_API_KEY"], base_url=base_url,
                    timeout=60.0, max_retries=2)
    prompts = {}
    for version in versions:
        path = ROOT / "prompts" / (version + ".txt")
        if not path.exists():
            raise SystemExit(f"Create prompts/{version}.txt from observed findings before this run.")
        prompts[version] = path.read_text(encoding="utf-8").strip()
        if version != "V0" and not prompts[version]:
            raise SystemExit(f"Prompt {version} is empty")
    cases = json.loads((ROOT / args.cases).read_text(encoding="utf-8"))
    policy = (ROOT / "context" / "damaged_delivery_policy.txt").read_text(encoding="utf-8")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    destination = ROOT / "results" / (run_id + ".jsonl")
    destination.parent.mkdir(exist_ok=True)
    with destination.open("w", encoding="utf-8") as log:
        for version, prompt in prompts.items():
            # V0/V1 deliberately have no policy: historical baseline, not a
            # controlled prompt-only comparison against grounded versions.
            supplied_policy = "" if version in {"V0", "V1"} else policy
            for case in cases:
                for repeat in range(1, args.repeat + 1):
                    input_text = (f"POLICY:\n{supplied_policy}\n\nREQUEST:\n{case['request']}"
                                  if supplied_policy else case["request"])
                    record = dict(run_id=run_id, version=version, case_id=case["id"],
                                  repeat=repeat, deployment=deployment,
                                  instructions=prompt, input=input_text)
                    started = perf_counter()
                    try:
                        kwargs = dict(model=deployment, input=input_text)
                        if prompt:
                            kwargs["instructions"] = prompt
                        # No previous_response_id: each case is independent.
                        # No temperature/top_p or request for hidden reasoning.
                        response = client.responses.create(**kwargs)
                        record.update(response_id=response.id, model=response.model,
                                      status=response.status, output=response.output_text,
                                      usage=response.usage.model_dump() if response.usage else None,
                                      incomplete_details=(response.incomplete_details.model_dump()
                                                          if response.incomplete_details else None))
                    except (APIError, APIConnectionError) as exc:
                        # Error type/status only, avoiding accidental secret exposure.
                        record.update(status="error", error_type=type(exc).__name__,
                                      http_status=getattr(exc, "status_code", None))
                    record["elapsed_seconds"] = round(perf_counter() - started, 3)
                    log.write(json.dumps(record, ensure_ascii=False) + "\n")
                    log.flush()
                    print(version, case["id"], repeat, record["status"],
                          record["elapsed_seconds"], "seconds")
    print("Saved:", destination)
    print("Apply worksheets/findings.md manually; no quality scores were generated.")

if __name__ == "__main__":
    main()
