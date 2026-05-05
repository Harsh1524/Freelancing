from services.llm_client import chat


def generate_review_request(
    client_name: str,
    project: str,
    platform: str,
    tone: str,
) -> str:
    system = (
        "You are an expert at client communication. "
        "You write review request messages that feel genuine and personal — never pushy or templated. "
        "Your messages consistently result in 5-star reviews."
    )
    prompt = f"""
Write review request messages for this completed project:

- Client Name: {client_name}
- Project Completed: {project}
- Platform: {platform}
- Tone: {tone}

Generate three separate messages:

### 1. Primary Review Request
Send immediately after project delivery.
- 3–5 sentences, warm, grateful, specific to the project
- Mention the value delivered
- Include a clear but soft call to action

### 2. Follow-up Message
Send if no response after 5 days.
- 2–3 sentences max
- Gentle reminder, not pushy
- Reference the project briefly

### 3. Thank You Message
Send after they leave a review.
- Express genuine gratitude
- Mention you'd love to work with them again
- Keep it short and warm

All messages must:
- Feel personal and reference {project} specifically
- Be appropriate for {platform}
- Match the {tone} tone throughout
- Never sound copy-pasted or automated

Use markdown with clear section headers.
"""
    return chat(prompt, system)