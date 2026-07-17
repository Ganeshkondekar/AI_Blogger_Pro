from utils.api import chat


def seo_optimize(blog: str) -> str:
    prompt = f"""
You are an SEO expert.

Improve the following blog for SEO.

Tasks:
- Improve the title
- Improve headings
- Add a meta description
- Improve readability
- Keep the meaning unchanged

Blog:

{blog}

Return only the optimized blog.
"""

    return chat(prompt)