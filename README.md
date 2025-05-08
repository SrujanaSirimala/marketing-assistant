# 🎨 Marketing Assistant App

An AI-powered Streamlit web app that creates **branded marketing flyers** and **captions** in seconds.

Just upload your **brand guidelines** and describe your event — this app takes care of the design, layout, and tone using GPT-4o and DALL·E.

---

## ⚡ What It Does

- 📥 Accepts a brand guideline PDF
- 🧠 Uses GPT-4o to generate:
  -  **flyer plan**
  -  **caption for social media**
- 🎨 Generates a full flyer image using **DALL·E 3**
- 💾 Lets you **view, download, and share** the final design

---

## 🧪 Tech Stack

| Feature         | Technology        |
|----------------|-------------------|
| UI              | Streamlit         |
| AI Planner      | OpenAI GPT-4o     |
| Flyer Image     | OpenAI DALL·E 3   |
| PDF Parsing     | PyPDF2            |
| Image Layout    | Pillow (PIL)      |

---

## 🛠️ Setup Instructions

### 🔑 1. API Key

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
