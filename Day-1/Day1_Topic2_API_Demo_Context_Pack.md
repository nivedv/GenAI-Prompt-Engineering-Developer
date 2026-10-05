# Day 1 Topic 2 Context Pack: Supplier Payment Triage

Use these fictional documents as local context for the trainer's Python API demo. They are designed to be read from a Markdown file and inserted into the API prompt.

---

## Document 1 — Finance Operations Payment Policy

**Document ID:** FIN-PAY-01  
**Owner:** Finance Operations  
**Version:** 1.0

### Rules

1. Supplier invoices are normally paid within **30 calendar days** after invoice approval.
2. Payment status must not be promised from static context.
3. If invoice number, supplier name, purchase order number or approval status is missing, request the missing detail.
4. If the invoice is approved and older than 30 calendar days, classify as **Needs finance review**.
5. If the invoice is not approved, ask the requester to confirm approval status or contact the PO owner.
6. The assistant must not claim that payment has been released, escalated or scheduled unless live finance-system evidence is available.

---

## Document 2 — Supplier Email

**From:** accounts@northwind-supplies.example  
**Subject:** Payment follow-up for invoice NW-7781

Hello Finance Team,

We submitted invoice NW-7781 for PO PO-4492. The invoice was approved by your procurement contact on 1 September 2026. We have not received payment yet. Could you confirm when payment will be released?

Regards,  
Northwind Supplies

---

## Document 3 — Static Vendor Record

**Supplier:** Northwind Supplies  
**Supplier ID:** SUP-2041  
**PO:** PO-4492  
**Invoice:** NW-7781  
**Invoice amount:** INR 4,80,000  
**Approval status in this static sample:** Approved  
**Approval date:** 2026-09-01  
**Payment status:** Not available in this static sample

This record is a classroom sample. It does not prove live payment status.

---

## Expected Triage Shape

```json
{
  "category": "supplier_payment_follow_up",
  "priority": "normal | needs_finance_review",
  "known_facts": [],
  "missing_information": [],
  "policy_basis": [],
  "safe_next_action": "",
  "must_not_claim": []
}
```
