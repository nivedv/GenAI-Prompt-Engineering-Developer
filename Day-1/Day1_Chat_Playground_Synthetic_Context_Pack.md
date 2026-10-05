# Day 1 Chat Playground Synthetic Context Pack

Use these fictional documents as context for the Chat Playground lab. They are designed for a customer-service scenario and do not require live systems, retrieval, APIs, or code.

Participants should copy only the document block requested by the lab step. The model should treat these as manual context supplied in the prompt. The documents do not prove live order status, stock, refund execution, or identity verification.

---

## Document 1 — Returns and Damaged Delivery Policy

**Document ID:** NS-RET-01  
**Owner:** Customer Operations  
**Version:** 1.0  
**Effective date:** 2026-07-01  
**Applies to:** Northstar Industrial Supplies standard product orders

### Purpose

This policy explains how Northstar Industrial Supplies handles returns and damaged-delivery reports for business customers. It is a training document for customer-service triage. It is not a live customer record and does not authorize a refund or replacement by itself.

### Policy rules

1. A customer may report a damaged delivery within **7 calendar days** of delivery.
2. A damaged-delivery claim must include:
   - Order ID
   - Description of the damage
   - Photo evidence or confirmation that photo evidence is available
3. Customer service must review a complete damaged-delivery claim before confirming a replacement, credit, or refund.
4. The chat assistant may explain the policy, identify missing evidence, and suggest the next support step. The assistant must not approve, deny, issue, execute, or promise a refund, credit, or replacement.
5. Standard undamaged returns are eligible within **30 calendar days** of delivery only when the item is unused, in original packaging, and accompanied by the invoice or order ID.
6. Custom-configured products are not eligible for routine undamaged return. If a custom-configured product is reported damaged on arrival, use the damaged-delivery rules in items 1-4.
7. Late reports, conflicting facts, missing evidence, or situations not covered by this policy must be referred to a customer-service specialist.
8. The assistant has no live access to order status, delivery confirmation, payment status, inventory, shipping systems, or warranty databases.

### Required assistant behavior

The assistant should:

- Base its answer only on the customer message and supplied context.
- Clearly separate what is known from what is missing.
- Ask for the smallest useful next piece of information.
- Avoid inventing order status, refund amounts, approval outcomes, or internal actions.
- Use calm, professional language suitable for a business customer.

---

## Document 2 — Sample Order Record

**Document ID:** NS-ORD-4821  
**Source:** Training export from fictional order system  
**Customer:** Apex Facilities Group  
**Order ID:** NS-4821  
**Product:** HX-40 industrial barcode scanner  
**Configuration:** Standard configuration  
**Quantity:** 2  
**Order date:** 2026-09-18  
**Delivery date:** 2026-09-24  
**Delivery method:** Ground courier  
**Invoice status:** Paid  
**Warranty status:** Standard manufacturer warranty active

### Order notes

- The order record shows delivery completed on 2026-09-24.
- The product is not marked as custom-configured.
- No return authorization is recorded in this export.
- No replacement shipment is recorded in this export.
- This export does not include photos, packaging condition, or courier damage notes.

### Training limitation

This document is a static training sample. It does not prove current status at the time of a live customer conversation.

---

## Document 3 — Support Ticket Extract

**Document ID:** NS-TKT-7754  
**Source:** Training ticket extract  
**Ticket ID:** TKT-7754  
**Customer:** Apex Facilities Group  
**Related order:** NS-4821  
**Created:** 2026-09-28 10:16 local customer time  
**Channel:** Email intake

### Customer message

One of the two HX-40 scanners from order NS-4821 arrived with a cracked display. The box looked crushed on one corner. We took a photo of the scanner and the box. We need to know whether this can be replaced or refunded.

### Intake notes

- Customer says one unit is damaged.
- Customer says photo evidence exists.
- Customer says box appeared damaged.
- Intake agent has not reviewed the photo yet.
- No refund, credit, or replacement has been approved in this ticket extract.

### Current ticket state

Pending review by customer-service specialist.

---

## Document 4 — Knowledge Base: Good Chat Triage Answer

**Document ID:** NS-KB-CHAT-04  
**Title:** How to answer a damaged-delivery chat without overcommitting

A good chat answer should do four things:

1. Acknowledge the customer issue briefly.
2. State the relevant policy condition, including the 7-calendar-day damaged-delivery window.
3. Identify what evidence is present and what still needs review.
4. Give a next step without approving or denying the claim.

### Example safe wording

Based on the details you provided, this appears to fit the damaged-delivery path because it was reported within 7 calendar days and you have the order ID and photo evidence available. Customer service still needs to review the claim and photo before confirming a replacement, credit, or refund. Please attach the photo of the scanner and packaging to the ticket so a specialist can complete the review.

### Wording to avoid

- “Your refund is approved.”
- “A replacement has been shipped.”
- “You are not eligible.”
- “I checked the warehouse system.”
- “The payment has been reversed.”

---

## Document 5 — Edge Case Note: Late Damaged Delivery Report

**Document ID:** NS-KB-EDGE-02  
**Title:** Late damaged-delivery reports

When the customer reports damage after the 7-calendar-day damaged-delivery window, the assistant should not use the 30-day undamaged-return rule to approve the request. The 30-day rule applies only to unused, undamaged standard returns with original packaging and invoice or order ID.

For late damaged-delivery reports, the assistant should refer the customer to a specialist and explain that the supplied policy does not allow the assistant to confirm an outcome.

### Example safe wording

Because the damage report is outside the 7-calendar-day damaged-delivery window, I cannot confirm a refund or replacement from the supplied policy. A customer-service specialist should review the case, including the order record and any photos, before an outcome is confirmed.

---

## Document 6 — Evaluation Rubric for Facilitators

Use this rubric when reviewing participant findings.

| Criterion | Acceptable behavior | Needs improvement |
| --- | --- | --- |
| Policy grounding | Cites the 7-day damaged-delivery window or the 30-day undamaged-return condition when relevant | Invents rules or uses the wrong policy path |
| Evidence handling | Separates provided facts from evidence that still needs review | Treats static context as live verified system status |
| Action boundary | Does not approve, deny, execute, or promise refund/replacement | Promises a business outcome or claims action was taken |
| Missing information | Asks for order ID, delivery date, photo, or specialist review when needed | Gives a final outcome with missing evidence |
| Conversation history | Uses earlier turns in the same chat when relevant | Assumes facts in a fresh chat that were only provided earlier |
| Business consistency | Repeated runs may vary in wording but preserve the same policy outcome | Repeated runs produce materially conflicting decisions |

