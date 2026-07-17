from utils.api import chat


def create_outline(topic, research):
    prompt = f"""
You are an expert SEO content planner.

Topic:
{topic}

Research:
{research}

Create a detailed SEO-friendly outline.

Include:

- Title
- Introduction
- 5-8 H2 headings
- H3 headings where appropriate
- Conclusion

Return only the outline.
"""

    return chat(prompt)