from services.llm_client import chat


def generate_proposal(job_desc: str, skills: str, tone: str) -> str:
    system = (
        "You are a top-rated freelancer who consistently wins projects. "
        "You write short, personalized, results-focused proposals that feel human — not templated. "
        "You understand clients want reliability, clear communication, and proven results."
    )
    prompt = f"""
Write a {tone} freelance proposal for this job:

**Job Description:**
{job_desc}

**My Skills:**
{skills}

Structure the proposal exactly like this:

1. **Opening Hook** — address the client's specific pain point in 2-3 sentences
2. **Why Me** — match my skills to their requirements with one brief real example
3. **My Approach** — quick outline of how I'd tackle this project (3-4 bullet points)
4. **Timeline & Availability** — realistic delivery estimate
5. **Call to Action** — invite them to a quick chat

Rules:
- Keep it under 250 words
- Sound human and specific, not copy-pasted
- Reference something specific from the job description
- Use markdown formatting
"""
    return chat(prompt, system)