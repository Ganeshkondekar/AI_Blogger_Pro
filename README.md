# 🚀 AI Blogger Pro

> An intelligent multi-agent AI system that researches, plans, writes, and optimizes high-quality blog posts using Large Language Models and real-time web search.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-green)
![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 Overview

AI Blogger Pro automates the complete blog creation process through a **multi-agent pipeline**.

Instead of relying on a single AI prompt, specialized agents collaborate to produce well-structured, SEO-friendly blog posts.

The application features a modern Streamlit interface, real-time web research via Tavily, and LLM-powered content generation using OpenRouter.

---

# ✨ Features

- 🌐 Real-time web research
- 🤖 Multi-Agent AI Architecture
- 📝 Automatic blog outline generation
- ✍️ AI-powered blog writing
- 🔍 SEO optimization
- 📥 Download generated blogs
- 🎨 Modern Streamlit UI
- ⚡ Fast OpenRouter API integration

---

# 🏗️ Multi-Agent Workflow

```text
           User Topic
                │
                ▼
      ┌─────────────────┐
      │ Research Agent  │
      │ (Tavily Search) │
      └─────────────────┘
                │
                ▼
      ┌─────────────────┐
      │ Planner Agent   │
      │ Creates Outline │
      └─────────────────┘
                │
                ▼
      ┌─────────────────┐
      │ Writer Agent    │
      │ Generates Blog  │
      └─────────────────┘
                │
                ▼
      ┌─────────────────┐
      │ SEO Agent       │
      │ Optimizes Blog  │
      └─────────────────┘
                │
                ▼
          Final Blog
```

---

# 🖥️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| OpenRouter | LLM API |
| Tavily | Web Search |
| Requests | API Communication |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📂 Project Structure

```text
AI_Blogger_Pro/
│
├── agents/
│   ├── manager.py
│   ├── research.py
│   ├── planner.py
│   ├── writer.py
│   └── seo.py
│
├── utils/
│   ├── api.py
│   ├── helpers.py
│   └── search.py
│
├── app.py
├── main.py
├── config.py
├── style.css
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Ganeshkondekar/AI_Blogger_Pro.git
```

Go into the project

```bash
cd AI_Blogger_Pro
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENROUTER_API_KEY=YOUR_API_KEY
TAVILY_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

---

# 🚀 Future Improvements

- Token usage tracking
- Cost estimation
- Readability score
- Keyword density analysis
- Multiple LLM selection
- Blog history
- Export to PDF
- Export to DOCX
- One-click deployment
- AI image generation
- WordPress publishing
- Plagiarism detection

---

# 💡 Why Multi-Agent?

Instead of asking one AI model to perform every task, AI Blogger Pro separates responsibilities among specialized agents.

This results in:

- Better research
- Better organization
- Better writing quality
- Cleaner architecture
- Easier maintenance
- Scalable workflow

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ganesh Kondekar**

GitHub:
https://github.com/Ganeshkondekar

---

⭐ If you found this project useful, consider giving it a star!
