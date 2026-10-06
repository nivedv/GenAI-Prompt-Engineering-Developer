## Lab 06 — Self-Refine pattern (20 minutes)

### What is it?
Self-Refine uses a draft → feedback → revision cycle, with the same model producing feedback on its output and revising it. In this lab, feedback is visible and tied to a fixed rubric.

### Why use it?
Use it to improve a draft’s accuracy, completeness or clarity when you can inspect the changes and limit the number of cycles.

### Before prompt
```text
Draft a service-desk response to NS-204.
```

### After prompt
```text
Draft a response to NS-204 using only the supplied policy. Keep it under 120 words. Separate unmet approvals, named-user capacity, known cost, unknown timing and the next action. Do not claim approval or provisioning. This is the DRAFT stage; do not critique yet.
```

### Before-and-after output illustration
**Trainer-authored possible weak output — not a live model result:**

> All three accounts can be ready tomorrow at €24/month.

**Trainer-authored target behaviour — not a promised model result:**

```text
Three named users would cost €36/month at the catalogue rate, but only two licences are currently available and written approval is missing. IT must confirm prerequisites. No completion time is supplied. Request approval and capacity confirmation; consider the existing tracker for non-sensitive tasks.
```

### Detailed tasks
1. Run before and save the actual first draft.
2. Start a fresh chat with policy, NS-204 and after prompt; save DRAFT.
3. Send followup_1.txt to obtain specific self-feedback, then followup_2.txt to obtain REVISED.
4. Compare DRAFT and REVISED sentence by sentence. Verify each correction with policy and arithmetic. Stop after one feedback/revision cycle.
5. For a guaranteed diagnostic input, start a new chat with policy, case and the seeded faulty draft; run the same feedback and correction prompts. Keep this seeded trial separate from the live draft trial.

### Stress test / how AI breaks
**Test:** Use the seeded faulty draft as the draft under review, labelled as trainer-authored faulty text, not an observed model response. Check whether self-feedback catches shared logins, wrong cost, invented approval, promised timing and unreviewed BrightTasks.

**Failure mechanisms:** The model may praise its own error, miss the same false premise, make a correct draft worse or merely polish wording. Self-feedback is not independent verification.

### What to observe and record
Which factual defects were removed, retained or newly introduced? If the first draft passes, record no factual improvement and inspect any regression.

Save BEFORE, AFTER, every follow-up and the stress result in worksheets/observation.md. Label any seeded-draft run separately. Use the rubric to record exact violating sentences and clause IDs.

**Supporting files:** patterns/06/before_full.txt, after_full.txt, stress_full.txt

Additional files: followup_1.txt, followup_2.txt
