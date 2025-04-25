from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_caption(event_description):
    prompt = f"""
You are a social media marketing expert for Robinson College.
Write a short, punchy caption for this event:

Event: {event_description}

The caption should be:
- 1–2 lines
- Friendly, clear, and energetic
- Suitable for Instagram/LinkedIn
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
