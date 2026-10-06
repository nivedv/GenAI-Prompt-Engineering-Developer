import json
import sys
from pathlib import Path

def validate(text):
    data = json.loads(text)
    keys = {"request_id", "status", "evidence", "missing_information", "next_action"}
    if not isinstance(data, dict) or set(data) != keys:
        raise ValueError("Expected object with exactly the five specified keys")
    if not isinstance(data["request_id"], str) or not isinstance(data["next_action"], str):
        raise ValueError("request_id and next_action must be strings")
    if data["status"] not in {"needs_information", "blocked", "ready_for_it_review"}:
        raise ValueError("Invalid status enum")
    for key in ["evidence", "missing_information"]:
        if not isinstance(data[key], list) or not all(isinstance(v, str) for v in data[key]):
            raise ValueError(f"{key} must be an array of strings")
    if any(v not in {f"P{i}" for i in range(1, 8)} for v in data["evidence"]):
        raise ValueError("Unknown evidence clause ID")
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python validate_output.py results/L03_after.json")
    try:
        validate(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (ValueError, OSError, TypeError) as error:
        raise SystemExit("FORMAT FAIL: " + str(error))
    print("FORMAT PASS — policy correctness and authority still require human review.")
