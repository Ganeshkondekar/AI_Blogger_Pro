import requests
from config import API_KEY, MODEL, BASE_URL


def chat(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "max_tokens": 2000,
    }

    response = requests.post(
        BASE_URL,
        headers=headers,
        json=payload,
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]