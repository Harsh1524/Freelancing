import gradio as gr
from services.pricing_service import recommend_pricing


def build_pricing_tab():
    with gr.Tab("💰 Pricing Strategy"):
        gr.Markdown("### Get AI-powered pricing recommendations for any project")
        with gr.Row():
            with gr.Column():
                project_type  = gr.Textbox(
                    label="Project Type",
                    placeholder="E-commerce website, Mobile app, REST API, ML pipeline..."
                )
                complexity    = gr.Dropdown(
                    ["Simple", "Moderate", "Complex", "Enterprise"],
                    label="Project Complexity", value="Moderate"
                )
                current_rate  = gr.Number(
                    label="Your Current Hourly Rate (USD)", value=30
                )
                client_region = gr.Textbox(
                    label="Client's Region (optional)",
                    placeholder="USA, Europe, Middle East, India..."
                )
                btn = gr.Button("📊 Get Pricing Strategy", variant="primary")
            with gr.Column():
                output = gr.Markdown(label="Pricing Strategy", value="*Pricing recommendation will appear here...*")

        btn.click(
            fn=recommend_pricing,
            inputs=[project_type, complexity, current_rate, client_region],
            outputs=output
        )