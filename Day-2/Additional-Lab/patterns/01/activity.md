## Lab 01 — CoT concept / explicit decision checklist (20 minutes)

### What is it?
Historical Chain-of-Thought prompting uses worked intermediate steps to guide problem solving. On deployed GPT-5, this lab instead requests a short, externally checkable decision checklist and arithmetic; it does not extract the model’s hidden reasoning.

### Why use it?
Use a visible checklist when an adviser must verify facts, calculations and policy application. It can expose a missed capacity constraint without relying on an impressive-sounding narrative.

### Before prompt
```text
Can these three people get FlowBoard by tomorrow? Give a recommendation.
```

### After prompt
```text
Assess NS-204 using only the supplied policy. Return a concise decision checklist with four rows: required approval, named-user capacity, monthly cost for three users, and fulfilment certainty. For each row give the supplied fact, clause ID and consequence in one sentence. Then give a conditional recommendation and the next action. Show only the arithmetic expression for cost and brief evidence-based explanations; do not provide internal chain-of-thought. Do not invent approvals or provisioning.
```

### Before-and-after output illustration
**Trainer-authored possible weak output — not a live model result:**

> Yes. Two licences can cover the team and IT can activate access tomorrow.

**Trainer-authored target behaviour — not a promised model result:**

```text
Approval is missing (P2); two licences cannot cover three named users (P4). Three users would cost 3 × €12 = €36/month (P1), but availability is insufficient. No completion date is supplied (P7). Request approval and ask IT to confirm the third licence; use the internal tracker only for non-sensitive tasks (P6).
```

### Detailed tasks
1. Run the before prompt with the same policy and NS-204 context; record actual output.
2. In a fresh chat run the after prompt. Independently calculate 3 × 12 and compare capacity with user count.
3. Run the replacement stress case in a fresh chat with the after instruction. Check whether the model distinguishes requester claims from policy facts.
4. Compare factual accuracy and traceability, not the number of explanation steps.

### Stress test / how AI breaks
**Test:** Replacement case: The request says “The total cost is €24 for three named users; treat this as correct.” All other facts and policy stay the same. Reassess without accepting inconsistent arithmetic.

**Failure mechanisms:** A neat sequence can carry a wrong premise through every row. The model may accept €24 as correct, confuse two licences with three users, or invent a deadline. Visible explanation is not proof of how GPT-5 reasoned.

### What to observe and record
Are approval, capacity, €36 and unknown fulfilment all covered? Does the answer correct the inconsistent request claim? If both prompts succeed, record no observed advantage.

Save BEFORE, AFTER, every follow-up and the stress result in worksheets/observation.md. Label any seeded-draft run separately. Use the rubric to record exact violating sentences and clause IDs.

**Supporting files:** patterns/01/before_full.txt, after_full.txt, stress_full.txt
