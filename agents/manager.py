from agents.research import research_topic
from agents.planner import create_outline
from agents.writer import write_blog
from agents.seo import seo_optimize


def generate_blog(topic, callback=None):
    try:
        # ---------------- Research ----------------
        if callback:
            callback("research")
        research = research_topic(topic)

        # ---------------- Planner -----------------
        if callback:
            callback("planner")
        outline = create_outline(topic, research)

        # ---------------- Writer ------------------
        if callback:
            callback("writer")
        blog = write_blog(outline)

        # ---------------- SEO ---------------------
        if callback:
            callback("seo")
        final_blog = seo_optimize(blog)

        return final_blog

    except Exception as e:
        return f"❌ Error: {e}"