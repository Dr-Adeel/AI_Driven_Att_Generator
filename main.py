# from modules.description_generator import generate_description

# def chatbot():
#     print("Shopora Chatbot (type 'quit' to exit)")
#     print("Use command: desc: <product title>\n")

#     while True:
#         query = input("You: ")
#         if query.lower() == "quit":
#             break

#         if query.startswith("desc:"):
#             title = query.replace("desc:", "").strip()
#             lang = input("Language? (en/fr): ").strip().lower()
#             lang = "French" if lang == "fr" else "English"

#             print("\n Generating description...\n")
#             desc = generate_description(title, lang)
#             print(desc)
#             print("\n" + "="*60)

#         else:
#             print("I only handle `desc:` for now (description generator).")

# if __name__ == "__main__":
#     chatbot()

from modules.description_generator import generate_description
from modules.price_recommendation import recommend_price

print("🤖 Shopora Chatbot (type 'quit' to exit)")
print("Commands: desc: <product title>, price: <product title>")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "quit":
        break

    if user_input.startswith("desc:"):
        title = user_input.replace("desc:", "").strip()
        print("👉 Generating description...")
        print(generate_description(title))

    elif user_input.startswith("price:"):
        title = user_input.replace("price:", "").strip()
        print("👉 Recommending price...")
        print(recommend_price(title))

    else:
        print("👉 Use `desc:` for description or `price:` for price recommendation.")

