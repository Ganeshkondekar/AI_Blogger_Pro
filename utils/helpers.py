import os


def save_blog(topic: str, content: str):
    os.makedirs("output", exist_ok=True)

    filename = topic.lower().replace(" ", "_") + ".md"
    filepath = os.path.join("output", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath