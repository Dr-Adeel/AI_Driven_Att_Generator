import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(title: str, lang="English"):
    """Generate short, detailed and bullet point description for a product"""
    prompt = f"""
    You are an expert e-commerce copywriter.
    Write a {lang} product description for the following:

    Product: {title}

    Format:
    Short Description: ...
    Detailed Description: ...
    Bullet Points:
    - ...
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
