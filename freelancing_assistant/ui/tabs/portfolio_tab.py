import gradio as gr
from services.portfolio_service import generate_portfolio


def build_portfolio_tab():
    with gr.Tab("🌐 Portfolio Generator"):
        gr.Markdown("### Generate a complete portfolio website (single HTML file)")
        with gr.Row():
            with gr.Column():
                name          = gr.Textbox(label="Your Full Name")
                title         = gr.Textbox(
                    label="Professional Title",
                    placeholder="Full-Stack Developer & UI Designer"
                )
                skills        = gr.Textbox(
                    label="Skills (comma-separated)",
                    placeholder="React, Node.js, Python, AWS, Figma"
                )
                contact_email = gr.Textbox(
                    label="Contact Email",
                    placeholder="your@email.com"
                )
                projects      = gr.Textbox(
                    label="Past Projects (one per line)",
                    lines=4,
                    placeholder=(
                        "E-commerce platform for RetailCo — React + Node.js\n"
                        "AI dashboard for HealthTech startup — Python + FastAPI\n"
                        "Mobile banking app — React Native"
                    )
                )
                theme         = gr.Dropdown(
                    ["Dark Tech", "Minimal Light", "Creative Bold", "Corporate Blue"],
                    label="Design Theme", value="Dark Tech"
                )
                btn = gr.Button("🌐 Generate Portfolio HTML", variant="primary")
            with gr.Column():
                output = gr.Markdown(
                    label="Generated HTML (copy & save as index.html)",
                    value="*Portfolio HTML will be generated here...*"
                )

        btn.click(
            fn=generate_portfolio,
            inputs=[name, title, skills, projects, contact_email, theme],
            outputs=output
        )