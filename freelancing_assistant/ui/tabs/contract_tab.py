import gradio as gr
from services.contract_service import generate_contract


def build_contract_tab():
    with gr.Tab("📄 Contract Generator"):
        gr.Markdown("### Generate a professional freelance contract")
        with gr.Row():
            with gr.Column():
                freelancer_name = gr.Textbox(label="Your Name / Company Name")
                client_name     = gr.Textbox(label="Client Name / Company")
                project_name    = gr.Textbox(label="Project Name")
                project_value   = gr.Number(label="Total Project Value (USD)", value=2000)
                timeline        = gr.Textbox(
                    label="Timeline / Deadline",
                    placeholder="4 weeks, ending July 30 2025"
                )
                payment_terms   = gr.Dropdown(
                    [
                        "50% upfront, 50% on delivery",
                        "Milestone-based (3 milestones)",
                        "Monthly retainer",
                        "Full payment upfront",
                        "Net 30 on delivery",
                    ],
                    label="Payment Terms",
                    value="50% upfront, 50% on delivery"
                )
                btn = gr.Button("📋 Generate Contract", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Contract Draft", value="*Contract will appear here...*")

        btn.click(
            fn=generate_contract,
            inputs=[client_name, project_name, project_value, timeline, payment_terms, freelancer_name],
            outputs=output
        )