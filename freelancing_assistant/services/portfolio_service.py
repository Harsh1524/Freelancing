from services.llm_client import chat

THEME_MAP = {
    "Dark Tech":       "dark background #0f0f17, neon indigo/purple accents, JetBrains Mono font, futuristic tech aesthetic",
    "Minimal Light":   "white background, black text, generous whitespace, clean sans-serif, elegant minimal design",
    "Creative Bold":   "vibrant colors, oversized bold typography, asymmetric layout, creative agency feel",
    "Corporate Blue":  "professional blue palette, structured grid, clean corporate design, trustworthy feel",
}


def generate_portfolio(
    name: str,
    title: str,
    skills: str,
    projects: str,
    contact_email: str,
    theme: str,
) -> str:
    system = (
        "You are a senior frontend developer and UI designer. "
        "You write clean, modern, complete single-file HTML portfolio websites. "
        "Output ONLY the raw HTML code starting with <!DOCTYPE html>. No explanation, no markdown fences."
    )
    theme_desc = THEME_MAP.get(theme, THEME_MAP["Dark Tech"])
    prompt = f"""
Generate a complete, production-ready single-file HTML portfolio website.

Owner Details:
- Name: {name}
- Professional Title: {title}
- Skills: {skills}
- Contact Email: {contact_email}
- Projects:
{projects}

Design Theme: {theme_desc}

Requirements:
- Single HTML file with embedded <style> and <script> — no external files
- Sections: Hero, About, Skills (with visual skill bars), Projects (cards), Contact (form)
- Smooth scroll navigation
- Hover animations on project cards
- Mobile responsive with hamburger menu
- Animated hero section
- Skill progress bars with percentages
- Project cards with title, description, and a placeholder link
- Contact section with email link
- Professional footer

Output ONLY the complete HTML starting with <!DOCTYPE html>.
"""
    return chat(prompt, system)