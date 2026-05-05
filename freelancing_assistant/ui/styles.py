CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
    --primary:       #6366f1;
    --primary-dark:  #4f46e5;
    --accent:        #f59e0b;
    --bg:            #0f0f17;
    --surface:       #1a1a2e;
    --surface2:      #16213e;
    --border:        #2d2d4e;
    --text:          #e2e8f0;
    --text-muted:    #94a3b8;
    --success:       #10b981;
    --danger:        #ef4444;
}

body, .gradio-container {
    background: var(--bg) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

.gradio-container { max-width: 1200px !important; margin: 0 auto !important; }

h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; }

/* ── Tabs ── */
.tab-nav button {
    background: var(--surface) !important;
    color: var(--text-muted) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px 8px 0 0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
}
.tab-nav button.selected { background: var(--primary) !important; color: white !important; border-color: var(--primary) !important; }
.tab-nav button:hover    { background: var(--primary-dark) !important; color: white !important; }

/* ── Inputs ── */
label { color: var(--text-muted) !important; font-size: 0.85rem !important; font-weight: 500 !important; }

input, textarea, select {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
input:focus, textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}

/* ── Buttons ── */
button.primary, .gr-button-primary {
    background: linear-gradient(135deg, var(--primary), var(--primary-dark)) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    padding: 10px 24px !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 12px rgba(99,102,241,0.3) !important;
}
button.primary:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 20px rgba(99,102,241,0.4) !important; }

/* ── Panels ── */
.gr-panel, .gr-box, .gr-form {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}

/* ── Markdown output ── */
.gr-markdown {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    padding: 16px !important;
    color: var(--text) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    line-height: 1.7 !important;
}
.gr-markdown code {
    background: #0d0d1a !important;
    color: var(--accent) !important;
    font-family: 'JetBrains Mono', monospace !important;
    border-radius: 4px !important;
    padding: 2px 6px !important;
}
.gr-markdown table { width: 100% !important; border-collapse: collapse !important; }
.gr-markdown th { background: var(--primary) !important; color: white !important; padding: 8px !important; }
.gr-markdown td { padding: 8px !important; border-bottom: 1px solid var(--border) !important; }

/* ── Header ── */
#header-banner {
    background: linear-gradient(135deg, #1a1a3e 0%, #0f0f2e 50%, #1a1a3e 100%) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 32px !important;
    margin-bottom: 24px !important;
    text-align: center !important;
}

.status-badge {
    display: inline-block;
    background: rgba(16,185,129,0.15);
    color: var(--success);
    border: 1px solid rgba(16,185,129,0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 600;
}
"""

HEADER_HTML = """
<div id="header-banner">
    <div style="font-size:2.5rem;margin-bottom:8px;">🚀</div>
    <h1 style="font-size:2rem;font-weight:700;color:#e2e8f0;margin:0 0 8px 0;">
        FreelanceAI <span style="color:#6366f1;">M28</span>
    </h1>
    <p style="color:#94a3b8;margin:0 0 16px 0;font-size:1rem;">
        Your AI-powered freelancing command center — powered by Qwen via Ollama
    </p>
    <span class="status-badge">✓ Qwen Active · Runs 100% Locally</span>
</div>
"""

FOOTER_HTML = """
<div style="text-align:center;padding:24px;color:#475569;font-size:0.8rem;margin-top:16px;">
    <strong style="color:#6366f1;">FreelanceAI M28</strong> ·
    Powered by <strong style="color:#f59e0b;">Qwen via Ollama</strong> ·
    Runs 100% locally 🔒
</div>
"""