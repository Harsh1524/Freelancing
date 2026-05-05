import gradio as gr
from services.tax_service import estimate_tax


def build_tax_tab():
    with gr.Tab("🧮 Tax Estimator"):
        gr.Markdown("### Estimate your freelance taxes with deductions and saving tips")
        with gr.Row():
            with gr.Column():
                country        = gr.Dropdown(
                    ["India", "United States", "United Kingdom", "Canada", "Australia", "Germany", "UAE"],
                    label="Country", value="India"
                )
                annual_income  = gr.Number(
                    label="Estimated Annual Freelance Income (local currency)",
                    value=1200000
                )
                expenses       = gr.Number(
                    label="Estimated Annual Business Expenses (local currency)",
                    value=200000
                )
                btn = gr.Button("🧮 Estimate My Taxes", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Tax Breakdown & Savings", value="*Tax estimate will appear here...*")

        btn.click(
            fn=estimate_tax,
            inputs=[country, annual_income, expenses],
            outputs=output
        )