from services.llm_client import chat


def optimize_profile(platform: str, skills: str, experience: float, niche: str) -> str:
    system = (
        "You are an expert freelance profile coach with deep knowledge of "
        "Upwork, Fiverr, and Toptal ranking algorithms. "
        "You write compelling, keyword-rich profiles that rank high and convert visitors into clients."
    )
    prompt = f"""
Create a fully optimized freelancer profile for **{platform}**:

- Skills: {skills}
- Years of Experience: {experience}
- Niche / Specialty: {niche}

Generate the following sections:

1. **Professional Title** (max 80 chars, keyword-rich for {platform})
2. **Profile Overview / Bio** (300–400 words, first-person, results-focused, with relevant keywords)
3. **Top 5 Skill Tags** to select on {platform}
4. **3 Portfolio Project Ideas** to showcase immediately
5. **Profile Optimization Tips** specific to {platform} algorithm

Use markdown formatting with clear section headers.
"""
    return chat(prompt, system)