import gradio as gr
from services.scope_service import estimate_scope


def build_scope_tab():
    with gr.Tab("📐 Scope Estimator"):
        gr.Markdown("### Estimate project scope, timeline, effort and cost")
        with gr.Row():
            with gr.Column():
                project_desc = gr.Textbox(
                    label="Project Description",
                    lines=6,
                    placeholder=(
                        "Build a multi-tenant SaaS platform with user authentication, "
                        "subscription billing, admin dashboard, REST API and mobile-responsive UI..."
                    )
                )
                project_type = gr.Dropdown(
                    ["Web App", "Mobile App", "API / Backend", "Data Pipeline", "UI/UX Design", "AI / ML Project", "E-commerce"],
                    label="Project Type", value="Web App"
                )
                team_size    = gr.Slider(1, 10, value=1, step=1, label="Number of Freelancers")
                hourly_rate  = gr.Number(label="Your Hourly Rate (USD)", value=40)
                btn = gr.Button("📐 Estimate Scope & Cost", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Scope & Cost Estimate", value="*Estimate will appear here...*")

        btn.click(
            fn=estimate_scope,
            inputs=[project_desc, project_type, team_size, hourly_rate],
            outputs=output
        )