from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_flyer_image(flyer_plan: str) -> str:
    prompt = f"""
    A flyer in digital graphic design announces a Virtual Employer Information Session.
    Include the following:
    - Title: "Virtual Employer Information Session"
    - Subheading: "Learn more about employer"
    - Date: April 25, 2025
    - Time: 3PM - 4PM
    - Location: ZoomCall

    Design style:
    - Use a clean, modern layout
    - Background color: GSU Blue (#0039A6)
    - Text should be sharp and readable
    - Include university-style visual branding
    - Add room for logos and CTA
    """

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    return response.data[0].url
