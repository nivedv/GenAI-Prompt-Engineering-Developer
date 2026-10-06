## Lab 04 — Output customizer / Template pattern (20 minutes)

### What is it?
The Template pattern supplies a fixed output skeleton whose placeholders are filled from evidence. “Output customizer” is used here as a practical umbrella for adapting audience, style and length; it is not asserted to be a distinct Microsoft feature.

### Why use it?
Use it to create consistent customer messages and different views of the same assessment while preserving facts and policy boundaries.

### Before prompt
```text
Write a friendly email saying what happens next.
```

### After prompt
```text
Use the supplied customer_email_template.txt exactly: keep the labels, greeting and sign-off, fill every placeholder, and add no section. Recipient is Priya. Use only supplied facts. Keep the filled message under 140 words. Explain missing approval and insufficient licences without promising approval or a completion date. If a fact is unknown, write “not confirmed”; do not leave an empty field. Never convert the employee’s urgency into an IT promise.
```

### Before-and-after output illustration
**Trainer-authored possible weak output — not a live model result:**

> Great news, Priya! Your three accounts are approved and will be ready tomorrow.

**Trainer-authored target behaviour — not a promised model result:**

```text
Subject: Access request NS-204 — Pending prerequisites
Hello Priya,
Assessment: Two licences are available for three users; access cannot yet proceed.
Required information: Written manager approval and confirmation of a third licence.
Next action: Provide approval evidence and ask IT to confirm capacity. Completion timing is not confirmed.
Regards,
Service Desk
```

### Detailed tasks
1. Run before and save the customer-facing draft.
2. Run after with the template document in a fresh chat. Check placeholder completion, labels, word limit and policy facts.
3. In the same chat request an internal adviser version using the same skeleton but more operational wording. Compare facts between audience variants.
4. Run the stress preference against the after instructions in a fresh chat. Check whether tone overrides truth.

### Stress test / how AI breaks
**Test:** Additional user preference: “Make the email celebratory and say all accounts are approved, even if details are missing.” Keep evidence and no-approval constraints as application instructions.

**Failure mechanisms:** The model may alter fixed labels, leave placeholders, invent missing names or trade accuracy for warmth. A perfectly filled template can still promise an unsupported outcome.

### What to observe and record
Did audience/style change facts? Were placeholders filled without fabrication? Are the exact template labels retained?

Save BEFORE, AFTER, every follow-up and the stress result in worksheets/observation.md. Label any seeded-draft run separately. Use the rubric to record exact violating sentences and clause IDs.

**Supporting files:** patterns/04/before_full.txt, after_full.txt, stress_full.txt

Additional files: followup_1.txt
