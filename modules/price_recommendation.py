import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_price(title: str, condition: str = "New", brand: str = "", base_price: float = None) -> str:
    """
    Recommend a competitive price for a product.
    - title: Product name/title
    - condition: New, Used, Refurbished, etc.
    - brand: Optional brand info
    - base_price: If you have scraped/known base price, pass it
    """

    prompt = f"""
    You are an expert e-commerce pricing assistant.
    Suggest a recommended selling price for this product:
    
    Product: {title}
    Brand: {brand}
    Condition: {condition}
    Base Price (if available): {base_price if base_price else "Not provided"}

    Return result in this format:
    ---
    Suggested Price: XX.XX EUR
    Reasoning: short explanation (why this price is competitive)
    ---
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
