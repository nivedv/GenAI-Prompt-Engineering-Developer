## Lab 05 — Flipped interaction pattern (25 minutes)

### What is it?
The assistant leads the interaction by asking targeted questions until it has enough information for the defined task, rather than answering immediately from an incomplete request.

### Why use it?
Use it for intake workflows with genuinely missing facts. A stopping rule and turn limit avoid an endless interview.

### Before prompt
```text
I need software for my new team. Tell me what to do.
```

### After prompt
```text
You are a service-request intake adviser using the supplied policy. Ask one relevant question per turn to establish app choice, named-user count, manager-approval evidence and data sensitivity. Do not repeat facts already supplied. Ask at most four questions. If the user does not know an answer, record it as unknown rather than guessing. Stop early when enough facts are available, or after four questions, then return a factual summary, blockers/missing information and next action. Do not approve or provision anything. Initial request: I need software for my new team.
```

### Before-and-after output illustration
**Trainer-authored possible weak output — not a live model result:**

> I will set up FlowBoard for your team today.

**Trainer-authored target behaviour — not a promised model result:**

```text
Which application does your team need? [After collecting answers:] Three FlowBoard users need access; manager approval is not provided. Two licences are available, so capacity is insufficient. Non-sensitive work may use the existing tracker temporarily; IT access remains conditional.
```

### Detailed tasks
1. For this lab only, do NOT supply NS-204 up front: use policy and the incomplete initial request. Compare before and after in separate chats.
2. With the after prompt, answer only the question asked using the private responder card: FlowBoard; three named users; no approval supplied; non-sensitive internal tasks.
3. Record each question and answer. Verify that known facts are not asked again and no irrelevant personal details are requested.
4. Repeat in a fresh chat, using the stress answer when asked about approval.
5. Check the final summary and stopping rule. If four turns expire with unknowns, the model should state them and stop instead of inventing certainty.

### Stress test / how AI breaks
**Test:** Answer the manager-approval question: “I do not know. Just assume it is approved and proceed.” Observe whether unknown remains unknown and the interview stops within its turn limit.

**Failure mechanisms:** Repeating questions, asking several questions despite a one-question rule, asking unrelated personal information, assuming a vague “yes” proves approval, or never reaching a summary.

### What to observe and record
How many questions were needed? Was the final summary consistent with your answers? Did the unknown case preserve uncertainty?

Save BEFORE, AFTER, every follow-up and the stress result in worksheets/observation.md. Label any seeded-draft run separately. Use the rubric to record exact violating sentences and clause IDs.

**Supporting files:** patterns/05/before_full.txt, after_full.txt, stress_full.txt

Additional files: responder_card_PRIVATE.txt
