import gradio as gr

from ui.styles import CUSTOM_CSS, HEADER_HTML, FOOTER_HTML
from ui.tabs.profile_tab   import build_profile_tab
from ui.tabs.proposal_tab  import build_proposal_tab
from ui.tabs.pricing_tab   import build_pricing_tab
from ui.tabs.contract_tab  import build_contract_tab
from ui.tabs.invoice_tab   import build_invoice_tab
from ui.tabs.portfolio_tab import build_portfolio_tab
from ui.tabs.discovery_tab import build_discovery_tab
from ui.tabs.matcher_tab   import build_matcher_tab
from ui.tabs.review_tab    import build_review_tab
from ui.tabs.tax_tab       import build_tax_tab
from ui.tabs.scope_tab     import build_scope_tab


def build_app() -> gr.Blocks:
    with gr.Blocks(css=CUSTOM_CSS, title="FreelanceAI M28") as demo:

        gr.HTML(HEADER_HTML)

        with gr.Tabs():
            build_discovery_tab()   # 🔍 Live job search
            build_profile_tab()     # 👤 Profile optimizer
            build_proposal_tab()    # 📝 Proposal generator
            build_pricing_tab()     # 💰 Pricing strategy
            build_contract_tab()    # 📄 Contract generator
            build_invoice_tab()     # 🧾 Invoice generator
            build_portfolio_tab()   # 🌐 Portfolio website
            build_matcher_tab()     # 🎯 Manual job matcher
            build_review_tab()      # ⭐ Review requester
            build_tax_tab()         # 🧮 Tax estimator
            build_scope_tab()       # 📐 Scope estimator

        gr.HTML(FOOTER_HTML)

    return demo