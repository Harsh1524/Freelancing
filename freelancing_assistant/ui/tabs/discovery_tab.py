import gradio as gr
from services.job_fetcher_service import fetch_all_jobs, format_jobs_for_display, format_jobs_for_ai
from services.matcher_service import match_projects


def search_and_match(keywords: str, limit: int, use_ai: bool, my_skills: str):
    jobs       = fetch_all_jobs(keywords=keywords, limit_per_source=int(limit))
    job_display = format_jobs_for_display(jobs)
    ai_result  = ""
    if use_ai and my_skills.strip():
        job_text  = format_jobs_for_ai(jobs)
        ai_result = match_projects(my_skills, job_text)
    return job_display, ai_result


def build_discovery_tab():
    with gr.Tab("🔍 Project Discovery"):
        gr.Markdown("### Find real-time freelancing projects from Upwork, Freelancer, RemoteOK, Remotive & Himalayas")
        with gr.Row():
            with gr.Column(scale=1):
                keywords  = gr.Textbox(
                    label="Search Keywords",
                    placeholder="python, react, data science, UI design...",
                    value="python developer"
                )
                limit     = gr.Slider(1, 10, value=5, step=1, label="Results per source")
                use_ai    = gr.Checkbox(label="🤖 Run AI Match Analysis after fetching", value=False)
                my_skills = gr.Textbox(
                    label="Your Skills (for AI matching)",
                    lines=3,
                    placeholder="5 years Python, FastAPI, React. Built 3 SaaS products...",
                    visible=False
                )
                btn = gr.Button("🔍 Fetch Live Jobs", variant="primary")

            with gr.Column(scale=2):
                job_out = gr.Markdown(value="*Live jobs will appear here...*")
                ai_out  = gr.Markdown(value="")

        use_ai.change(
            fn=lambda x: gr.update(visible=x),
            inputs=use_ai,
            outputs=my_skills
        )

        btn.click(
            fn=search_and_match,
            inputs=[keywords, limit, use_ai, my_skills],
            outputs=[job_out, ai_out]
        )