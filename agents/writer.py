from utils.api import chat


def write_blog(outline: str) -> str:
    prompt = f"""
You are a professional blog writer.

Using the outline below, write a complete, engaging, SEO-friendly blog article.

Outline:

{outline}

Return only the final blog.
"""

    return chat(prompt)