from services.llm_client import chat


def estimate_scope(project_desc: str, project_type: str, team_size: int, hourly_rate: float) -> str:
    system = (
        "You are a senior project manager and technical architect with 10+ years of experience "
        "estimating freelance and agency projects across web, mobile, and data domains. "
        "You give realistic, detailed estimates — never overly optimistic."
    )
    prompt = f"""
Provide a complete project scope and estimation for this project:

**Project Description:**
{project_desc}

**Project Type:** {project_type}
**Team Size:** {team_size} freelancer(s)
**Hourly Rate:** ${hourly_rate}/hr

Generate a full estimation report with these sections:

1. **Project Complexity Assessment** — Simple / Moderate / Complex / Enterprise and why
2. **Feature Breakdown Table** — list each feature/module with estimated hours in a markdown table
3. **Timeline Estimate** — total weeks broken into phases (Discovery, Design, Development, Testing, Launch)
4. **Cost Estimate Table** — hours × rate for each phase with a total
5. **Risk Factors** — top 5 risks that could affect timeline or budget
6. **Assumptions** — what you're assuming to make this estimate
7. **Out of Scope** — what is NOT included in this estimate (important to set with clients)
8. **Recommended Milestones** — payment milestone suggestions tied to deliverables
9. **Questions for Client** — 5 questions to ask before starting to refine the estimate

Use markdown tables for the breakdown. Be specific with hours and costs.
"""
    return chat(prompt, system)