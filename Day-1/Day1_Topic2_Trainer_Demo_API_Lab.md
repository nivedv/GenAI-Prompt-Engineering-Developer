# Day 1 Topic 2 Trainer Demo Lab: Working with LLM APIs from Code

**Scenario:** Supplier payment triage from Python  
**Tooling:** Python, OpenAI Python client, Azure AI Foundry / Azure OpenAI deployment  
**Authentication for demo:** API key through environment variable  
**Model:** Deployed original GPT-5 model supplied for the course  
**Trainer:** Nived Varma  
**Estimated time:** 45-60 minutes

This demo moves from Chat Playground to code. The trainer shows how to call an LLM deployment from Python, pass messages, add local context, inspect the response, stream output, and handle basic failure cases.

Use `Day1_Topic2_API_Demo_Context_Pack.md` as the context source.

---

## Prerequisites

Participants should have:

- Python 3.10 or later.
- VS Code or any editor.
- Internet access to the approved Azure endpoint.
- The endpoint/base URL provided by the trainer.
- The deployment name provided by the trainer.
- An API key provided through the training environment.

Install the Python package:

```bash
pip install openai
```

Set environment variables. Use the values supplied by the trainer:

```bash
export AZURE_OPENAI_API_KEY="<your-key>"
export AZURE_OPENAI_BASE_URL="https://<resource-name>.openai.azure.com/openai/v1/"
export AZURE_OPENAI_DEPLOYMENT="<deployment-name>"
```

On Windows PowerShell:

```powershell
$env:AZURE_OPENAI_API_KEY="<your-key>"
$env:AZURE_OPENAI_BASE_URL="https://<resource-name>.openai.azure.com/openai/v1/"
$env:AZURE_OPENAI_DEPLOYMENT="<deployment-name>"
```

Do not paste real keys into slides, chat windows, screenshots or Git repositories. Keys are shy creatures: once they escape, they become expensive.

---

## Demo 1 — Minimal chat completion call

Create `01_basic_call.py`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "You are a concise enterprise assistant."},
        {"role": "user", "content": "In two sentences, explain what an LLM API call does."},
    ],
)

print(response.choices[0].message.content)
```

Run:

```bash
python 01_basic_call.py
```

Trainer points:

- `model` is the deployment name.
- `messages` is the prompt.
- The SDK response contains more than the visible answer.

---

## Demo 2 — Print response metadata and usage

Create `02_usage.py`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "You are a concise enterprise assistant."},
        {"role": "user", "content": "Explain why API usage data matters for an enterprise LLM app."},
    ],
)

print("Answer:\n", response.choices[0].message.content)
print("\nFinish reason:", response.choices[0].finish_reason)
print("Usage:", response.usage)
```

Trainer points:

- Usage helps compare prompts and monitor cost drivers.
- Finish reason helps detect incomplete output or content filtering.
- Production logging should avoid storing sensitive user content unnecessarily.

---

## Demo 3 — Add local context from a Markdown file

Save the supplied context pack as `supplier_context.md` in the same folder.

Create `03_context_grounding.py`:

```python
import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
)

context = Path("supplier_context.md").read_text(encoding="utf-8")

messages = [
    {
        "role": "system",
        "content": (
            "You are a finance operations triage assistant. "
            "Use only the supplied context. Do not claim live payment status. "
            "Return a compact JSON object using the expected triage shape."
        ),
    },
    {
        "role": "user",
        "content": f"Context:\n{context}\n\nTask: Triage the supplier email and recommend the safe next action.",
    },
]

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=messages,
)

print(response.choices[0].message.content)
print("Usage:", response.usage)
```

Trainer points:

- This is manual context injection, not retrieval.
- The static record does not prove live payment status.
- The answer should avoid promising that payment has been released.

---

## Demo 4 — Streaming response

Create `04_streaming.py`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
)

messages = [
    {"role": "system", "content": "You are a concise trainer explaining LLM APIs."},
    {"role": "user", "content": "Explain streaming in LLM APIs using a simple business example."},
]

stream = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=messages,
    stream=True,
)

for event in stream:
    delta = event.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()
```

Trainer points:

- Streaming is useful for responsiveness.
- Streaming does not mean the answer is validated.
- Applications still need final-state handling after the stream ends.

---

## Demo 5 — Simple retry wrapper

Create `05_retry.py`:

```python
import os
import time
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
)

def call_with_retry(messages, attempts=3):
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                messages=messages,
            )
        except Exception as exc:
            last_error = exc
            wait_seconds = 2 ** (attempt - 1)
            print(f"Attempt {attempt} failed. Waiting {wait_seconds}s...")
            time.sleep(wait_seconds)
    raise last_error

messages = [
    {"role": "system", "content": "You are a concise enterprise assistant."},
    {"role": "user", "content": "List three failure-handling practices for LLM API calls."},
]

response = call_with_retry(messages)
print(response.choices[0].message.content)
```

Trainer points:

- Real systems should handle specific exception types, timeouts and rate limits.
- Backoff avoids hammering the service.
- The user experience should explain recoverable failure clearly.

---

## Trainer closeout

In code, the model is only one part of the feature. The application owns configuration, prompt assembly, context selection, retries, logging, validation and business action.
