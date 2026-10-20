import re


responses={
    "hours":"Our business hours are Monday to Friday, 9 AM to 6 PM.",
    "delivery":"Delivery usually takes 3 to 5 working days.",
    "return":"Products can be returned within 30 days.",
    "price":"Please provide the product name to know the price."
}

def get_response(message):
    message = message.lower()
    if re.search(r"hour|time|open",message):
        return responses["hours"]
    elif re.search(r"delivery|shipping|arrive",message):
        return responses["delivery"]
    elif re.search(r"return|refund|exchange",message):
        return responses["return"]
    elif re.search(r"price|cost|amount",message):
        return responses["price"]
    else:
        return None

def chatbot():
    print("Bot:Hello! Welcome to Customer Support.")
    print("Bot:How can I help you today?")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ["bye","exit","quit"]:
            print("Bot: Thank you for contacting us. Goodbye!")
            break

        response=get_response(user_input)
        if response:
            print("Bot:",response)
        else:
            print("Bot: Sorry, I couldn't understand your request.")

chatbot()