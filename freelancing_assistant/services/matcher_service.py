from services.llm_client import chat


def match_projects(my_skills: str, job_listings: str) -> str:
    system = (
        "You are a sharp freelance career advisor who helps freelancers "
        "identify best-fit projects based on skills, earning potential, and red flags."
    )
    prompt = f"""
Analyze these job listings and rank them by fit for this freelancer.

**Freelancer Profile:**
{my_skills}

**Job Listings:**
{job_listings}

For EACH job provide:
1. **Job Title & Source**
2. **Match Score** (0–100%) with a one-line reason
3. **Skill Alignment** — what matches well, what is missing
4. **Estimated Earnings** — realistic project value
5. **Red Flags** — anything suspicious or problematic
6. **Verdict** — one of: ✅ Apply Now | ⚠️ Apply with Caution | ❌ Skip

---

End with:
### 🏆 Top Pick
State which job to apply to first and write a one-paragraph reason why.

Use markdown with clear headers per job.
"""
    return chat(prompt, system)