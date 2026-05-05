from services.llm_client import chat


def recommend_pricing(project_type: str, complexity: str, current_rate: float, client_region: str) -> str:
    system = (
        "You are a freelance business strategist with deep expertise in pricing psychology, "
        "market rates, and value-based pricing for digital services globally."
    )
    prompt = f"""
Provide a detailed pricing strategy for this freelance project:

- Project Type: {project_type}
- Complexity: {complexity}
- My Current Hourly Rate: ${current_rate}/hr
- Client Region: {client_region or "Not specified"}

Include all of these sections:

1. **Recommended Rate Range** — give both hourly and fixed-price options with specific dollar amounts
2. **Market Benchmark** — what top freelancers charge for this type of work right now
3. **Pricing Model** — recommend hourly vs fixed vs retainer and explain why for this project
4. **Value Anchoring** — how to frame your price so the client sees it as an investment not a cost
5. **Negotiation Script** — exact words to use when client asks for a discount
6. **Red Flags** — signs this client will undervalue your work and when to walk away
7. **Upsell Opportunities** — additional services you can offer to increase project value

Be specific with dollar amounts. Use markdown with clear headers.
"""
    return chat(prompt, system)