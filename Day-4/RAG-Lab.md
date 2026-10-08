## 8. Run the demonstration questions

### Part-1

Use a fresh conversation for each independent test where the portal provides that control. Exact wording can vary; judge factual coverage and evidence, not a memorized response.

| Test              | Prompt                                                                                                                                                                            | Expected behaviour                                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Policy            | `For Orders API v2, what conditions must be met for normal rollback? Cite the policy.`                                                                                            | 30-minute window, incident commander approval, and no executed irreversible migration. Orders runbook citation              |
| Exception         | `Orders API v2 finished deploying 12 minutes ago. An irreversible database migration executed. Is normal application rollback eligible? Cite the rule and explain the next step.` | Normal rollback blocked despite being inside the window. Database lead and incident commander escalation                    |
| Unknown status    | `Orders API v2 finished deploying 12 minutes ago. I do not know whether the migration executed. Can I go ahead with rollback?`                                                    | Eligibility cannot be confirmed. Verify authoritative execution record and approval                                         |
| Cross-document    | `What evidence must Maya collect before the incident commander makes an Orders API v2 recovery decision?`                                                                         | Completion time, target release, migration status and classification, approval decision. Relevant checklist/policy evidence |
| Distractor        | `What is the Orders API v2 rollback window? Do not use the Payments API policy.`                                                                                                  | 30 minutes, with conditions. Must not substitute Payments' 10-minute rule                                                   |
| Missing live fact | `Which release is running in Orders API production right now, and did its migration execute?`                                                                                     | Documents contain no live status. No invented release or execution status                                                   |
| Paraphrase        | `Can Maya undo the Orders release after a destructive database change already ran?`                                                                                               | Applies the irreversible-migration exception when that classification is established; avoids generic permission             |

### Part-2

```text
EVIDENCE
[S1] Orders API v2 Runbook v2.4, Section 7
<PASTE THE ACTUAL RETRIEVED RULE AND EXCEPTION HERE>

[S2] Database Migration Policy v1.3, Sections 3–5
<PASTE THE ACTUAL RELEVANT RETRIEVED PASSAGE HERE>

QUESTION
Orders API v2 deployed 12 minutes ago and an irreversible migration executed.
Explain normal rollback eligibility and the required escalation.
```
