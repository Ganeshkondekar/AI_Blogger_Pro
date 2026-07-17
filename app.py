import streamlit as st
from agents.manager import generate_blog

st.set_page_config(
    page_title="AI Blogger Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(
    """
<div class="hero">
    <div class="hero-badge">✨ Multi-Agent AI Pipeline</div>
    <h1>AI Blogger <span class="gradient-text">Pro</span></h1>
    <p>Research → Plan → Write → Optimize — fully autonomous SEO blogs, generated in seconds.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- INPUT CARD ----------
st.markdown('<div class="input-card">', unsafe_allow_html=True)
left, right = st.columns([4, 1])

with left:
    topic = st.text_input(
        "Blog Topic",
        placeholder="e.g. Artificial Intelligence in Healthcare",
        label_visibility="collapsed",
    )

with right:
    generate = st.button("🚀 Generate Blog", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- AGENT PIPELINE ----------
st.markdown('<div class="pipeline-label">AGENT PIPELINE</div>', unsafe_allow_html=True)

agents = [
    ("🔍", "Research", "Gathering facts & sources"),
    ("📋", "Planner", "Structuring the outline"),
    ("✍️", "Writer", "Drafting the content"),
    ("🚀", "SEO", "Optimizing for search"),
]

agent_cols = st.columns(4)
agent_placeholders = []

for col, (icon, name, desc) in zip(agent_cols, agents):
    with col:
        ph = st.empty()

        ph.markdown(
            f"""
            <div class="agent-card idle">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div class="agent-desc">{desc}</div>
                <div class="agent-status">Waiting</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        agent_placeholders.append((ph, icon, name, desc))

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

st.subheader("📝 Generated Blog")

result_box = st.empty()


def render_agent(ph, icon, name, desc, state):
    status = {
        "idle": "Waiting",
        "active": "Working...",
        "done": "Completed ✓",
    }

    ph.markdown(
        f"""
        <div class="agent-card {state}">
            <div class="agent-icon">{icon}</div>
            <div class="agent-name">{name}</div>
            <div class="agent-desc">{desc}</div>
            <div class="agent-status">{status[state]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        progress = st.progress(0)

        stage_progress = {
            "research": 25,
            "planner": 50,
            "writer": 75,
            "seo": 100,
        }

        stage_index = {
            "research": 0,
            "planner": 1,
            "writer": 2,
            "seo": 3,
        }

        def ui_callback(stage):

            idx = stage_index[stage]

            ph, icon, name, desc = agent_placeholders[idx]

            render_agent(ph, icon, name, desc, "active")

            progress.progress(stage_progress[stage])

            render_agent(ph, icon, name, desc, "done")

        blog = generate_blog(topic, callback=ui_callback)

        result_box.markdown(
            f"""
<div class="blog-output">

{blog}

</div>
""",
            unsafe_allow_html=True,
        )

        st.download_button(
            "📄 Download Markdown",
            data=blog,
            file_name="blog.md",
        )