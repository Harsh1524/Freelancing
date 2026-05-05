import re
import feedparser
import requests
from config import FREELANCER_API_TOKEN

# ─────────────────────────────────────────
# UPWORK RSS (no auth needed)
# ─────────────────────────────────────────

UPWORK_RSS_BASE = "https://www.upwork.com/ab/feed/jobs/rss"

def fetch_upwork_jobs(keywords: str, limit: int) -> list[dict]:
    url = f"{UPWORK_RSS_BASE}?q={keywords.replace(' ', '+')}&sort=recency"
    try:
        feed = feedparser.parse(url)
        jobs = []
        for entry in feed.entries[:limit]:
            jobs.append({
                "source":      "Upwork",
                "title":       entry.get("title", "N/A"),
                "description": _strip_html(entry.get("summary", ""))[:350] + "...",
                "link":        entry.get("link", ""),
                "published":   entry.get("published", "N/A"),
                "budget":      _upwork_budget(entry.get("summary", "")),
                "tags":        [],
            })
        return jobs
    except Exception as e:
        print(f"[Upwork RSS] {e}")
        return []


def _upwork_budget(summary: str) -> str:
    m = re.search(r"Budget</b>:\s*(.*?)<br", summary)
    if m:
        return m.group(1).strip()
    m = re.search(r"Hourly Range</b>:\s*(.*?)<br", summary)
    if m:
        return m.group(1).strip() + " /hr"
    return "Not specified"


# ─────────────────────────────────────────
# FREELANCER.COM API (free token)
# ─────────────────────────────────────────

FREELANCER_BASE = "https://www.freelancer.com/api/projects/0.1"

def fetch_freelancer_jobs(keywords: str, limit: int) -> list[dict]:
    if not FREELANCER_API_TOKEN:
        return []
    headers = {"freelancer-oauth-v1": FREELANCER_API_TOKEN}
    params  = {
        "query":          keywords,
        "limit":          limit,
        "job_details":    True,
        "sort_field":     "time_updated",
    }
    try:
        r = requests.get(
            f"{FREELANCER_BASE}/projects/active/",
            headers=headers, params=params, timeout=10
        )
        projects = r.json().get("result", {}).get("projects", [])
        jobs = []
        for p in projects:
            budget   = p.get("budget", {})
            currency = p.get("currency", {}).get("sign", "$")
            jobs.append({
                "source":      "Freelancer.com",
                "title":       p.get("title", "N/A"),
                "description": p.get("preview_description", "N/A")[:350] + "...",
                "link":        f"https://www.freelancer.com/projects/{p.get('seo_url', '')}",
                "published":   str(p.get("time_submitted", "N/A")),
                "budget":      f"{currency}{budget.get('minimum','?')} – {currency}{budget.get('maximum','?')}",
                "tags":        [j.get("name", "") for j in p.get("jobs", [])],
            })
        return jobs
    except Exception as e:
        print(f"[Freelancer API] {e}")
        return []


# ─────────────────────────────────────────
# REMOTEOK (free, no auth)
# ─────────────────────────────────────────

REMOTEOK_URL = "https://remoteok.com/api"

def fetch_remoteok_jobs(keywords: str, limit: int) -> list[dict]:
    try:
        r = requests.get(REMOTEOK_URL, headers={"User-Agent": "FreelanceAI-M28/1.0"}, timeout=10)
        data     = r.json()
        listings = [i for i in data if isinstance(i, dict) and "position" in i]
        kw       = keywords.lower()
        filtered = [
            j for j in listings
            if kw in j.get("position", "").lower()
            or kw in j.get("description", "").lower()
            or any(kw in t.lower() for t in j.get("tags", []))
        ]
        jobs = []
        for j in filtered[:limit]:
            jobs.append({
                "source":      "RemoteOK",
                "title":       j.get("position", "N/A"),
                "description": _strip_html(j.get("description", ""))[:350] + "...",
                "link":        j.get("url", ""),
                "published":   j.get("date", "N/A"),
                "budget":      j.get("salary", "Not specified"),
                "tags":        j.get("tags", []),
            })
        return jobs
    except Exception as e:
        print(f"[RemoteOK] {e}")
        return []


# ─────────────────────────────────────────
# REMOTIVE (free, no auth)
# ─────────────────────────────────────────

REMOTIVE_URL = "https://remotive.com/api/remote-jobs"

def fetch_remotive_jobs(keywords: str, limit: int) -> list[dict]:
    try:
        r    = requests.get(REMOTIVE_URL, params={"search": keywords, "limit": limit}, timeout=10)
        jobs = []
        for j in r.json().get("jobs", [])[:limit]:
            jobs.append({
                "source":      "Remotive",
                "title":       j.get("title", "N/A"),
                "description": _strip_html(j.get("description", ""))[:350] + "...",
                "link":        j.get("url", ""),
                "published":   j.get("publication_date", "N/A"),
                "budget":      j.get("salary", "Not specified"),
                "tags":        j.get("tags", []),
            })
        return jobs
    except Exception as e:
        print(f"[Remotive] {e}")
        return []


# ─────────────────────────────────────────
# HIMALAYAS (free, no auth)
# ─────────────────────────────────────────

HIMALAYAS_URL = "https://himalayas.app/jobs/api"

def fetch_himalayas_jobs(keywords: str, limit: int) -> list[dict]:
    try:
        r    = requests.get(HIMALAYAS_URL, params={"q": keywords, "limit": limit}, timeout=10)
        jobs = []
        for j in r.json().get("jobs", [])[:limit]:
            jobs.append({
                "source":      "Himalayas",
                "title":       j.get("title", "N/A"),
                "description": j.get("description", "N/A")[:350] + "...",
                "link":        j.get("applicationLink", ""),
                "published":   j.get("createdAt", "N/A"),
                "budget":      j.get("salaryRange", "Not specified"),
                "tags":        j.get("skills", []),
            })
        return jobs
    except Exception as e:
        print(f"[Himalayas] {e}")
        return []


# ─────────────────────────────────────────
# AGGREGATOR
# ─────────────────────────────────────────

def fetch_all_jobs(keywords: str = "python", limit_per_source: int = 5) -> list[dict]:
    """Fetch from all sources and return combined list."""
    print(f"[JobFetcher] Searching: '{keywords}' | {limit_per_source} per source")
    all_jobs = (
        fetch_upwork_jobs(keywords, limit_per_source)
        + fetch_freelancer_jobs(keywords, limit_per_source)
        + fetch_remoteok_jobs(keywords, limit_per_source)
        + fetch_remotive_jobs(keywords, limit_per_source)
        + fetch_himalayas_jobs(keywords, limit_per_source)
    )
    print(f"[JobFetcher] Total: {len(all_jobs)} jobs")
    return all_jobs


def format_jobs_for_display(jobs: list[dict]) -> str:
    """Markdown for Gradio display."""
    if not jobs:
        return "⚠️ No jobs found. Try different keywords."
    lines = [f"### 🔎 Found {len(jobs)} Jobs\n"]
    for i, j in enumerate(jobs, 1):
        tags = ", ".join(j.get("tags", [])[:5]) or "N/A"
        lines.append(f"""
---
**{i}. {j['title']}** &nbsp; `{j['source']}`

| Field | Value |
|-------|-------|
| 💰 Budget | {j['budget']} |
| 📅 Posted | {j['published']} |
| 🏷️ Tags | {tags} |

{j['description']}

🔗 [View Job]({j['link']})
""")
    return "\n".join(lines)


def format_jobs_for_ai(jobs: list[dict]) -> str:
    """Plain text for AI matcher prompt."""
    if not jobs:
        return "No jobs fetched."
    lines = []
    for i, j in enumerate(jobs, 1):
        lines.append(
            f"Job {i} [{j['source']}]: {j['title']}\n"
            f"Budget: {j['budget']}\n"
            f"Tags: {', '.join(j.get('tags', [])[:5])}\n"
            f"Description: {j['description']}\n---"
        )
    return "\n".join(lines)


# ─────────────────────────────────────────
# UTILITY
# ─────────────────────────────────────────

def _strip_html(text: str) -> str:
    clean = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", clean).strip()