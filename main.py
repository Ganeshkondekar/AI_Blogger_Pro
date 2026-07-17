from agents.manager import generate_blog


def show_header():
    print("\n" + "=" * 60)
    print("🤖 AI Blogger Pro")
    print("=" * 60)


def main():
    show_header()

    topic = input("\nEnter blog topic: ").strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    print("\n🔍 Researching...")
    print("📝 Creating outline...")
    print("✍️ Writing blog...")
    print("🚀 Optimizing SEO...\n")

    result = generate_blog(topic)

    print("\n" + "=" * 60)
    print("📄 FINAL BLOG")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()