# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_description(title: str, lang="English"):
#     """Generate short, detailed and bullet point description for a product"""
#     prompt = f"""
#     You are an expert e-commerce copywriter.
#     Write a {lang} product description for the following:

#     Product: {title}

#     Format:
#     Short Description: ...
#     Detailed Description: ...
#     Bullet Points:
#     - ...
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#     )

#     return response.choices[0].message.content.strip()

# prompt updated later
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(title: str,
                         category: str,
                         condition: str,
                         lang: str = "English",
                         tone: str = "friendly",
                         bullets: int = 4):
    """
    Generate a short product description + bullet points for the provided product.
    Returns a single string (suitable for printing).
    """

    # Normalize small inputs
    condition_clean = condition.capitalize() if condition else "Unknown"
    lang = "French" if lang.lower().startswith("f") else "English"

    # Prompt instructions
    prompt = f"""
You are an expert e-commerce copywriter. Create a concise, persuasive product description and clear bullet points
optimized for conversions and readability.Must describe product condition clearly.

Requirements:
- Language: {lang}
- Tone: {tone}
- Output format (exactly like below; do not add extra fields):
Description: <one or two sentences>
Key Features:
- <bullet 1>
- <bullet 2>
- ...
SEO Keywords: <comma-separated keywords>
Suggested Tags: <comma-separated tags>

Product information:
Title: {title}
Category: {category}
Condition: {condition_clean}

Guidelines:
- Short description: 15–30 words (focus on benefit +condition of product+ a key feature).
- Bullet points: provide {bullets} concise bullets (feature + user benefit).
- Include 4–6 SEO keywords relevant to the product.
- Keep language natural and suitable for product pages.
- If language is French, produce text entirely in French.

Return only the formatted output (no preface or explanation).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert e-commerce copywriter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=350
        )
        text = response.choices[0].message.content.strip()
        return text

    except Exception as e:
        # Simple error handling 
        return f"Error generating description: {e}"
