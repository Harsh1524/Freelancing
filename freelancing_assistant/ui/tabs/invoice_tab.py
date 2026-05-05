import gradio as gr
from services.invoice_service import generate_invoice


def build_invoice_tab():
    with gr.Tab("🧾 Invoice Generator"):
        gr.Markdown("### Generate professional invoices with payment reminders")
        with gr.Row():
            with gr.Column():
                freelancer_name = gr.Textbox(label="Your Name / Company")
                client_name     = gr.Textbox(label="Client Name")
                currency        = gr.Dropdown(
                    ["$", "₹", "€", "£", "AED", "CAD"],
                    label="Currency", value="$"
                )
                items_raw = gr.Textbox(
                    label="Line Items  —  format: Description | Hours | Rate",
                    lines=6,
                    placeholder=(
                        "UI Design | 10 | 50\n"
                        "API Integration | 8 | 60\n"
                        "Testing & QA | 4 | 40\n"
                        "Deployment | 2 | 50"
                    )
                )
                due_date = gr.Textbox(
                    label="Due Date",
                    placeholder="30 days from today / June 30 2025"
                )
                btn = gr.Button("🧾 Generate Invoice", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Invoice + Payment Reminders", value="*Invoice will appear here...*")

        btn.click(
            fn=generate_invoice,
            inputs=[client_name, freelancer_name, items_raw, due_date, currency],
            outputs=output
        )