from services.llm_client import chat


def estimate_tax(country: str, annual_income: float, expenses: float) -> str:
    system = (
        "You are a tax advisor specializing in freelancer taxation across multiple countries. "
        "You provide accurate, practical tax breakdowns with actionable saving tips. "
        "Always add a disclaimer that this is an estimate and professional CA/CPA advice is recommended."
    )
    net_income = annual_income - expenses
    prompt = f"""
Provide a detailed tax estimation for a freelancer in {country}:

- Gross Annual Freelance Income: {annual_income:,.2f} (local currency)
- Annual Business Expenses: {expenses:,.2f} (local currency)
- Net Taxable Income: {net_income:,.2f} (local currency)

Include all of these sections:

1. **Tax Summary Table** — show income, deductions, taxable income, and estimated tax in a markdown table
2. **Tax Slab Breakdown** — show which portions of income fall in which tax bracket with amounts
3. **Applicable Taxes** — list all taxes that apply (income tax, self-employment tax, GST/VAT, etc.)
4. **Quarterly Payment Schedule** — how much to set aside each quarter
5. **Legal Deductions & Write-offs** — top 8 expenses freelancers in {country} can deduct
6. **Tax Saving Strategies** — 5 legal ways to reduce tax liability in {country}
7. **Important Deadlines** — key filing dates for {country} freelancers
8. **Tools & Resources** — recommended platforms for filing in {country}

Use markdown tables where helpful. Be specific with numbers and percentages.

⚠️ *Disclaimer: This is an AI-generated estimate. Consult a qualified CA/CPA for professional advice.*
"""
    return chat(prompt, system)