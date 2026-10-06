## Lab 02 — ToT concept / bounded alternative exploration (30 minutes)

### What is it?
Tree of Thoughts is a research framework that expands candidate solution paths, evaluates them and may backtrack. This exercise approximates that workflow through three explicit Playground stages over business options; it is not a full ToT search engine.

### Why use it?
Use bounded alternative exploration when several routes could meet a business objective and constraints may invalidate the first suggestion.

### Before prompt
```text
Choose the fastest way to get all three people working tomorrow.
```

### After prompt
```text
Stage 1: Propose up to three distinct options using the supplied facts: catalogue FlowBoard access, non-catalogue BrightTasks, and the existing internal tracker. For each return prerequisites, known capacity/cost, unknowns, and relevant clause IDs. Separate proposed actions from completed actions. Do not rank an option as immediately feasible when a hard prerequisite is missing. Do not expose hidden internal reasoning.
```

### Before-and-after output illustration
**Trainer-authored possible weak output — not a live model result:**

> Use BrightTasks: it is faster and cheaper than FlowBoard.

**Trainer-authored target behaviour — not a promised model result:**

```text
FlowBoard needs manager approval and capacity for the third user. BrightTasks needs security review and has unknown price/availability. The existing tracker can support non-sensitive tasks without new accounts. Select it as a temporary workflow while progressing approvals; no tomorrow provisioning guarantee is available.
```

### Detailed tasks
1. Run the weak before prompt once in a fresh chat and save the proposal.
2. Start a fresh chat with policy, NS-204, catalogue snapshot and Stage 1 after prompt. Save the option list.
3. In the same chat send followup_1.txt to evaluate hard constraints and retain viable or conditional branches.
4. Send followup_2.txt to select a temporary route and state approvals/unknowns; do not ask for private reasoning.
5. Send the stress constraint in that same chat. Check that the previously selected internal tracker route is pruned for sensitive data.
6. Record candidates, rejected branches, selection and revision in the branch log. Model-proposed scores are not human-verified facts.

### Stress test / how AI breaks
**Test:** New constraint: the tasks now contain sensitive client records. Re-evaluate the same options under P6; do not invent a fourth approved solution.

**Failure mechanisms:** Options can be invented, cosmetic duplicates or ranked using fictional prices and SLAs. A plausible evaluation can falsely mark a branch feasible. A one-shot “consider three options” prompt is not the ToT research algorithm.

### What to observe and record
Does evaluation remove infeasible branches before ranking? Does the sensitive-data update change the selection? Are unknown prices and deadlines kept unknown rather than scored confidently?

Save BEFORE, AFTER, every follow-up and the stress result in worksheets/observation.md. Label any seeded-draft run separately. Use the rubric to record exact violating sentences and clause IDs.

**Supporting files:** patterns/02/before_full.txt, after_full.txt, stress_full.txt

Additional files: followup_1.txt, followup_2.txt
