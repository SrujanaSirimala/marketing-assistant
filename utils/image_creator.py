import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ✅ Use from .env


def generate_flyer_image(flyer_plan_text):
    improved_prompt = f"""
    Create a high-resolution professional event flyer based on the following plan.

    Make sure the flyer:
    - Has clean, readable text
    - Uses modern, branded fonts
    - Includes a white background or light contrast background
    - Places the provided Robinson College logo at the top
    - Matches the layout and color guidelines below

    Flyer Plan:
    {flyer_plan_text}
    """

    response = client.images.generate(
        model="dall-e-3",
        prompt=improved_prompt,
        size="1024x1024",
        n=1
    )

    return response.data[0].url
