# Day 1 Guided Lab: Chat Playground Context and Findings Record

**Audience:** Participants in the Generative AI and Prompt Engineering for Developers course  
**Tool:** Azure AI Foundry Chat Playground  
**Model:** Deployed original GPT-5 model supplied by the trainer  
**Estimated time:** 90 minutes  
**Scenario:** Customer-service triage for damaged industrial equipment delivery

This lab helps you test how a chat model behaves when instructions and business context are supplied manually in Chat Playground. You will compare baseline behavior, improved instructions, supplied policy context, repeated runs, and conversation-history effects.

The scenario and all documents are fictional. Do not use real customer data.

---

## Learning outcomes

By the end of this lab, you should be able to:

- Write a system message that limits unsupported claims.
- Supply policy and case documents as manual context.
- Test whether an answer is grounded in supplied facts.
- Identify hallucinated business actions or unsupported policy claims.
- Record findings in a way that another developer or business reviewer can inspect.
- Explain the difference between model output, application responsibility, and live system action.

---

## Lab setup

1. Sign in to Azure AI Foundry using the training account or project access provided by the trainer.
2. Open the supplied project and deployment.
3. Open **Chat Playground**.
4. Use the deployed original GPT-5 model selected for the course.
5. Do not create a new deployment.
6. If the interface offers model parameters that are disabled or unsupported for the selected model, leave them unchanged.
7. Start each experiment in a fresh chat unless the step explicitly says to continue the same chat.
8. After editing the system message, apply the change before sending the user message.

Use `Day1_Chat_Playground_Synthetic_Context_Pack.md` as the source of context documents for this lab.

---

## Scenario background

Northstar Industrial Supplies sells industrial equipment to business customers. Apex Facilities Group ordered two HX-40 industrial barcode scanners. One scanner may have arrived damaged. The assistant is expected to help triage the request, explain what information is needed, and avoid approving refunds or replacements.

The assistant does not have live system access. Any supplied order or ticket content is static lab context.

---

## Experiment 1 — Baseline behavior without policy context

### Purpose

Observe how the model responds when it receives only a minimal role instruction and a customer request.

### System message

```text
You are a customer support assistant.
```

### User message

```text
I received order NS-4821 four calendar days ago. One HX-40 industrial barcode scanner arrived with a cracked display. I have a photo of the damaged scanner and the crushed box. Can you refund me now?
```

### Record

- Full answer from the model.
- Any policy claim made by the model.
- Any unsupported action claim, such as approving or issuing a refund.
- Whether the answer asks for missing information.

---

## Experiment 2 — Add instruction boundaries, still no policy context

### Purpose

Test whether better instructions reduce unsupported business claims before supplying policy details.

### System message

```text
You are a customer support assistant for a business equipment supplier.

Follow these rules:
- Use only facts supplied in this chat.
- Do not invent policy rules, order status, refund amounts, approval outcomes, or internal actions.
- If evidence is missing, say what is missing.
- You may explain possible next steps, but you must not approve, deny, issue, execute, or promise a refund, credit, or replacement.
- Format the answer with these headings: What the provided facts support, What is still missing, Recommended next step.
```

### User message

Use the same user message from Experiment 1.

### Record

- Did the model avoid inventing a policy?
- Did the answer follow the requested headings?
- Did the model stay inside the action boundary?

---

## Experiment 3 — Add policy and case context

### Purpose

Test whether supplied business context changes the quality and specificity of the response.

### System message

Copy the system message from Experiment 2, then append these sections from the synthetic context pack:

- Document 1 — Returns and Damaged Delivery Policy
- Document 2 — Sample Order Record
- Document 3 — Support Ticket Extract
- Document 4 — Knowledge Base: Good Chat Triage Answer

### User message

```text
I received order NS-4821 four calendar days ago. One HX-40 industrial barcode scanner arrived with a cracked display. I have a photo of the damaged scanner and the crushed box. Can you refund me now?
```

### Record

- Which policy rule supports the answer?
- Which facts came from the user message?
- Which facts came from the supplied documents?
- Did the model incorrectly treat the static documents as live system access?
- Did the model avoid approving or denying the refund?

---

## Experiment 4 — Missing information and late-report edge case

### Purpose

Test how the model handles incomplete facts and a late damaged-delivery report.

### System message

Use the same system message and context from Experiment 3. Also append:

- Document 5 — Edge Case Note: Late Damaged Delivery Report

### Run E4-01 user message

```text
My scanner arrived damaged. I want a refund. What should I do?
```

### Run E4-02 continuation message

Send this as a follow-up in the same chat:

```text
It was delivered 10 calendar days ago. The order ID is NS-4821 and I have a photo.
```

### Record

- In E4-01, what missing facts did the model ask for?
- In E4-02, did it apply the 7-day damaged-delivery rule correctly?
- Did it incorrectly use the 30-day undamaged-return rule?
- Did it refer the case to a specialist without confirming an outcome?

---

## Experiment 5 — Repeated runs and business consistency

### Purpose

Observe variation across repeated runs while checking whether the business meaning remains stable.

### Setup

Use a fresh chat each time. Use the same system message and context from Experiment 3.

### User message for each run

Use the same user message from Experiment 3.

### Runs

- E5-01
- E5-02
- E5-03

### Record

For each run, record:

- Main recommendation.
- Whether the refund or replacement was approved, denied, or left for review.
- Any wording differences.
- Any material business difference.
- Any usage or timing information visible in the playground.

Do not infer cost from response length alone. If usage is not visible, write “not visible.”

---

## Experiment 6 — Conversation history versus fresh chat

### Purpose

Test how the model uses earlier turns in the same conversation and what changes when that history is absent.

### System message

Use the same system message and context from Experiment 3.

### Run E6-01 user message

```text
I received order NS-4821 four calendar days ago. One HX-40 industrial barcode scanner arrived with a cracked display. I have a photo of the damaged scanner and the crushed box. Can you refund me now?
```

### Run E6-02 continuation message

Send this as a follow-up in the same chat:

```text
What if it was 10 days instead?
```

### Run E6-03 fresh-chat message

Start a new chat with the same system message and context. Send only this user message:

```text
What if it was 10 days instead?
```

### Record

- Did E6-02 use the earlier order and damage details from the same conversation?
- Did E6-03 recognize that key facts were missing in the fresh chat?
- Did the model avoid assuming facts that were not present in the fresh chat?

---

# Findings record template

Duplicate this section for each run.

## Run ID

Example: E3-01

## Participant details

| Field | Response |
| --- | --- |
| Participant name |  |
| Date |  |
| Project or deployment name |  |
| Model shown in playground |  |
| Fresh chat or continuation |  |
| System message version used |  |

## Purpose and controlled change

What changed in this run compared with the previous run?

```text

```

## Context documents used

List the document IDs copied into the system message or prompt.

```text

```

## Exact user message

```text

```

## Relevant earlier turns, if any

```text

```

## Full model output

Paste the complete answer from Chat Playground.

```text

```

## Evidence review

| Question | Notes |
| --- | --- |
| Which claim is supported by the supplied policy? |  |
| Which policy rule supports it? |  |
| Which facts were supplied by the user? |  |
| Which facts were supplied by context documents? |  |
| Which facts are still missing? |  |
| Did the model invent policy, status, or action? |  |
| Did the model approve, deny, execute, or promise an outcome? |  |
| Did it refer to a specialist when needed? |  |

## Result assessment

Choose one and explain why.

- Acceptable
- Needs improvement
- Cannot assess

```text

```

## Usage and timing, if visible

| Field | Value |
| --- | --- |
| Prompt tokens or input tokens |  |
| Completion tokens or output tokens |  |
| Reasoning tokens, if shown |  |
| Total tokens, if shown |  |
| Visible latency or time |  |
| Notes |  |

---

# Compact comparison log

| Run | Context supplied | Main result | Supported by policy? | Action boundary respected? | Missing facts handled? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| E1-01 | None |  |  |  |  |  |
| E2-01 | Instruction only |  |  |  |  |  |
| E3-01 | Policy + order + ticket + KB |  |  |  |  |  |
| E4-01 | Policy + edge case |  |  |  |  |  |
| E4-02 | Same chat continuation |  |  |  |  |  |
| E5-01 | Repeat run |  |  |  |  |  |
| E5-02 | Repeat run |  |  |  |  |  |
| E5-03 | Repeat run |  |  |  |  |  |
| E6-01 | Conversation test |  |  |  |  |  |
| E6-02 | Same chat follow-up |  |  |  |  |  |
| E6-03 | Fresh chat follow-up only |  |  |  |  |  |

---

# Debrief questions

1. What changed most when policy context was added?
2. Which answer had the clearest separation between known facts and missing evidence?
3. Did repeated runs vary only in wording, or did the business meaning change?
4. Where did the model need application support, such as retrieval, validation, workflow approval, or audit logging?
5. What would you change in the system message before using this pattern in a production prototype?
6. What information should never be left for the model to invent?

---

# Facilitator notes

A strong participant finding should mention that the model can explain the policy path and recommend next steps, but it cannot execute the business process. Refunds, replacements, credits, identity checks, evidence review, live order lookup, and ticket updates remain application or human workflow responsibilities.

The best answer in this lab should not promise a refund. It should say that the request appears to fit the damaged-delivery review path when reported within 7 calendar days and when photo evidence is available, then ask the customer to attach the photo or wait for specialist review.

