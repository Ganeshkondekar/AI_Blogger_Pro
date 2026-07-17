from utils.search import web_search


def research_topic(topic):
    data = web_search(topic)

    research = ""

    if "results" in data:
        for item in data["results"][:5]:
            research += f"""
Title: {item.get("title","")}

Content:
{item.get("content","")}

Source:
{item.get("url","")}

------------------------------------
"""

    return research