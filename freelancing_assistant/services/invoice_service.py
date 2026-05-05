from datetime import date
from services.llm_client import chat


def generate_invoice(
    client_name: str,
    freelancer_name: str,
    items_raw: str,
    due_date: str,
    currency: str,
) -> str:
    today      = date.today().strftime("%B %d, %Y")
    inv_number = f"INV-{date.today().strftime('%Y%m%d')}-001"

    # Parse line items dynamically
    rows  = []
    total = 0.0
    for line in items_raw.strip().split("\n"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 3:
            try:
                desc, hours, rate = parts[0], float(parts[1]), float(parts[2])
                amount = hours * rate
                total += amount
                rows.append(f"| {desc} | {hours}h | {currency}{rate:.2f}/hr | {currency}{amount:,.2f} |")
            except ValueError:
                continue

    table = "\n".join(rows) if rows else f"| Development Work | 10h | {currency}50.00/hr | {currency}500.00 |"

    prompt = f"""
Generate a clean, professional invoice in markdown format:

---
# 🧾 INVOICE

**Invoice #:** {inv_number}
**Date Issued:** {today}
**Due Date:** {due_date}

**FROM:**
{freelancer_name}

**BILL TO:**
{client_name}

---

## Services Rendered

| Description | Hours | Rate | Amount |
|-------------|-------|------|--------|
{table}

---

**Subtotal:** {currency}{total:,.2f}
**Tax (0%):** {currency}0.00
**Total Due:** **{currency}{total:,.2f}**

---

## Payment Instructions
- Bank Transfer / PayPal / UPI / Wise / Stripe
- Reference: {inv_number}
- Make payable to: {freelancer_name}

*Thank you for your business! Please process payment by {due_date}.*

---

Now write 3 professional payment reminder email templates below the invoice for:
1. Friendly reminder (3 days before due date)
2. Due today reminder
3. Polite overdue notice (5 days after due date)

Each email should be short, professional, and reference invoice number {inv_number}.
"""
    return chat(prompt)