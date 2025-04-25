from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ✅ Correct usage

def generate_flyer_plan(brand_text, event_description):
    prompt = f"""
You are a branding and marketing expert.
Using the following brand guide, generate a flyer plan for the event below.

Brand Guidelines:
{brand_text}

Event:
{event_description}

Output:
- Title
- Subtitle
- Color Theme
- Layout Suggestions
- Font Style
- Taglines
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
