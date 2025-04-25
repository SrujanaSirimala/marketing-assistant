import streamlit as st
import os
from PIL import Image
from io import BytesIO
import requests
from dotenv import load_dotenv

# Import utilities
from utils.pdf_reader import extract_text_from_pdf
from utils.gpt4o_planner import generate_flyer_plan
from utils.caption_generator import generate_caption
from utils.image_creator import generate_flyer_image

# Load API key from .env
load_dotenv()

st.set_page_config(page_title="Marketing Assistant", layout="centered")
st.title("🎨 Marketing Assistant")

# Sidebar - Uploads
st.sidebar.header("📂 Upload Brand Materials")
brand_pdf = st.sidebar.file_uploader("Upload Brand Guideline PDF", type=["pdf"])



# Event description
st.header("📝 Describe Your Event")
event_description = st.text_area("Enter event details (e.g., Virtual Info Session on April 25 at 4:30 PM)")

# Generate button
if st.button("🚀 Generate Flyer and Caption"):
    if brand_pdf and event_description:
        # Extract text from PDF
        with st.spinner("📖 Reading brand guideline..."):
            brand_text = extract_text_from_pdf(brand_pdf)

        # Generate flyer plan (prompt for DALL·E)
        with st.spinner("🧠 Generating flyer plan with GPT-4o..."):
            flyer_plan = generate_flyer_plan(brand_text, event_description)
            st.subheader("📋 Flyer Plan (from GPT-4o)")
            st.text(flyer_plan)

        # Generate caption
        with st.spinner("✍️ Generating social media caption..."):
            caption = generate_caption(event_description)
            st.subheader("📣 Suggested Caption")
            st.write(caption)

        # Generate flyer image with DALL·E
        with st.spinner("🎨 Creating flyer image with DALL·E..."):
            flyer_url = generate_flyer_image(flyer_plan)
            response = requests.get(flyer_url)
            flyer = Image.open(BytesIO(response.content)).convert("RGBA")

        # Resize flyer to match display area
        flyer = flyer.resize((1024, 1024))

        # Save flyer alone
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        flyer_path = "outputs/generated_flyer.png"
        flyer.save(flyer_path)
        
# ✅ Display the flyer
        st.image(flyer_path, caption="✅ Generated Flyer", use_column_width=False)


    

        # Download button
        with open(flyer_path, "rb") as f:
            st.download_button("📥 Download Flyer", f, file_name="robinson_flyer.png")
    else:
        st.warning("⚠️ Please upload a brand guideline and enter your event description.")
