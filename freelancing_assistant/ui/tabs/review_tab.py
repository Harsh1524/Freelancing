import gradio as gr
from services.review_service import generate_review_request


def build_review_tab():
    with gr.Tab("⭐ Review Requester"):
        gr.Markdown("### Generate personalized review request messages for clients")
        with gr.Row():
            with gr.Column():
                client_name = gr.Textbox(label="Client Name")
                project     = gr.Textbox(
                    label="Project Completed",
                    placeholder="React analytics dashboard for FinTech startup"
                )
                platform    = gr.Dropdown(
                    ["Upwork", "Fiverr", "Freelancer.com", "LinkedIn", "Email", "Direct"],
                    label="Platform", value="Upwork"
                )
                tone        = gr.Dropdown(
                    ["Warm & Personal", "Professional", "Brief & Direct", "Grateful"],
                    label="Message Tone", value="Warm & Personal"
                )
                btn = gr.Button("⭐ Generate Review Messages", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Review Request Messages", value="*Messages will appear here...*")

        btn.click(
            fn=generate_review_request,
            inputs=[client_name, project, platform, tone],
            outputs=output
        )