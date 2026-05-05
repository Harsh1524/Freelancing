import gradio as gr
from services.profile_service import optimize_profile


def build_profile_tab():
    with gr.Tab("👤 Profile Optimizer"):
        gr.Markdown("### Optimize your freelancer profile with AI")
        with gr.Row():
            with gr.Column():
                platform   = gr.Dropdown(
                    ["Upwork", "Fiverr", "Toptal", "Freelancer.com", "PeoplePerHour"],
                    label="Platform", value="Upwork"
                )
                skills     = gr.Textbox(
                    label="Your Skills (comma-separated)",
                    placeholder="Python, FastAPI, React, PostgreSQL, Docker"
                )
                experience = gr.Slider(0, 20, value=3, step=0.5, label="Years of Experience")
                niche      = gr.Textbox(
                    label="Your Niche / Specialty",
                    placeholder="Full-stack SaaS development for startups"
                )
                btn = gr.Button("✨ Generate Optimized Profile", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Optimized Profile", value="*Your profile will appear here...*")

        btn.click(
            fn=optimize_profile,
            inputs=[platform, skills, experience, niche],
            outputs=output
        )