import gradio as gr
from services.proposal_service import generate_proposal


def build_proposal_tab():
    with gr.Tab("📝 Proposal Generator"):
        gr.Markdown("### Generate a customized winning proposal for any job")
        with gr.Row():
            with gr.Column():
                job_desc = gr.Textbox(
                    label="Job Description / Project Brief",
                    lines=7,
                    placeholder="Paste the full job post here..."
                )
                skills = gr.Textbox(
                    label="Your Relevant Skills & Experience",
                    placeholder="5 years Python, built 3 SaaS apps, FastAPI expert..."
                )
                tone = gr.Dropdown(
                    ["Professional", "Friendly", "Confident", "Technical", "Creative"],
                    label="Proposal Tone", value="Professional"
                )
                btn = gr.Button("🖊️ Generate Proposal", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Your Proposal", value="*Your proposal will appear here...*")

        btn.click(
            fn=generate_proposal,
            inputs=[job_desc, skills, tone],
            outputs=output
        )