print("Customer Support Chatbot Started")
def chatbot():
    print("Bot: Hello! Welcome to Customer Support.")
    print("Bot: How can I help you today?")
    while True:
        user_input=input("You:").lower().strip()

        if user_input in ["bye","exit","quit"]:
            print("Bot: Thank you for contacting us. Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I assist you?")

        else:
            print("Bot:I am still learning. Please ask another question.")

chatbot()

responses = {
    "hours": "Our business hours are Monday to Friday, 9 AM to 6 PM.",
    "delivery": "Delivery usually takes 3 to 5 working days.",
    "return": "Products can be returned within 30 days.",
    "price": "Please provide the product name to know the price."
}