import gradio as gr
from services.matcher_service import match_projects


def build_matcher_tab():
    with gr.Tab("🎯 Project Matcher"):
        gr.Markdown("### Paste job listings manually — AI ranks them by fit for your skills")
        with gr.Row():
            with gr.Column():
                my_skills = gr.Textbox(
                    label="Your Skills & Experience",
                    lines=4,
                    placeholder=(
                        "5 years Python, FastAPI, React, PostgreSQL, Docker.\n"
                        "Built 3 SaaS products. Expert in REST APIs and cloud deployment."
                    )
                )
                job_listings = gr.Textbox(
                    label="Job Listings (separate each with ---)",
                    lines=10,
                    placeholder=(
                        "Job 1: Need a React developer to build an admin dashboard...\n"
                        "Budget: $500–$1000\n"
                        "---\n"
                        "Job 2: Looking for Python ML engineer for NLP project...\n"
                        "Budget: $2000–$5000"
                    )
                )
                btn = gr.Button("🎯 Find Best Matches", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="AI Match Analysis", value="*Match results will appear here...*")

        btn.click(
            fn=match_projects,
            inputs=[my_skills, job_listings],
            outputs=output
        )