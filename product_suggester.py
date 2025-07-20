# product_suggester.py

class SmartStoreAgent:
    def __init__(self):
        self.product_database = {
            "headache": {
                "product": "Panadol Extra",
                "category": "Medicine",
                "reason": "It helps relieve headaches and contains paracetamol for fast pain relief."
            },
            "fever": {
                "product": "Disprin",
                "category": "Medicine",
                "reason": "Disprin reduces fever and provides quick relief from body pain."
            },
            "dry skin": {
                "product": "Nivea Soft Cream",
                "category": "Skincare",
                "reason": "It moisturizes dry skin and keeps it soft throughout the day."
            },
            "sore throat": {
                "product": "Strepsils",
                "category": "Medicine",
                "reason": "Strepsils help soothe and treat sore throat symptoms quickly."
            },
            "dandruff": {
                "product": "Head & Shoulders Anti-Dandruff Shampoo",
                "category": "Haircare",
                "reason": "It removes dandruff and keeps your scalp healthy."
            }
        }

    def suggest_product(self, user_input: str):
        user_input = user_input.lower()
        for keyword, info in self.product_database.items():
            if keyword in user_input:
                return (
                    f"✅ Suggested Product: {info['product']}\n"
                    f"🛍️ Category: {info['category']}\n"
                    f"💡 Reason: {info['reason']}"
                )
        return "❌ Sorry, I couldn't find a product for your need. Please try describing it differently."


# ------------------- Run Example -------------------
if __name__ == "__main__":
    agent = SmartStoreAgent()
    print("🤖 Smart Store Agent\n")
    while True:
        user_need = input("🧑 What do you need help with? (type 'exit' to quit): ")
        if user_need.lower() == "exit":
            break
        response = agent.suggest_product(user_need)
        print(response + "\n")
