import re
import random
from datetime import datetime, date

def get_current_time():
    return datetime.now().strftime("%I:%M %p")

def get_current_date():
    return date.today().strftime("%B %d, %Y")

def greet_user():
    greetings = [
        "Hello, how can I help you today?",
        "Hi, what can I do for you?",
        "Hey, how may I assist you?"
    ]
    return random.choice(greetings)

def goodbye_message():
    farewells = [
        "Goodbye, take care.",
        "See you soon.",
        "Bye, have a good day."
    ]
    return random.choice(farewells)

def rule_based_chatbot(user_input):
    user_input = user_input.lower().strip()

    if re.search(r"\b(hi|hello|hey|hai|heyy)\b", user_input):
        return greet_user()

    if "your name" in user_input:
        return "I am a chatbot created for the CODSOFT internship project."

    if "time" in user_input:
        return f"The current time is {get_current_time()}"

    if "date" in user_input:
        return f"Today's date is {get_current_date()}"

    if "how are you" in user_input:
        return "I am functioning well. What about you?"

    if "i am fine" in user_input:
        return "Good to hear. How can I assist you?"

    if "codsoft" in user_input:
        return "CODSOFT is an internship platform offering hands-on experience."

    if "what can you do" in user_input:
        return (
            "I can:\n"
            "- Tell you the date and time\n"
            "- Answer simple questions\n"
            "- Respond to basic text inputs\n"
            "- Demonstrate rule-based AI"
        )

    if "who created you" in user_input:
        return "I was created by Shaik Mehaboob Sania."

    if "joke" in user_input:
        jokes = [
            "Why don't programmers like nature? Because it has too many bugs.",
            "Debugging is solving a mystery where you are the culprit."
        ]
        return random.choice(jokes)

    if user_input in ["bye", "exit", "quit", "goodbye"]:
        return goodbye_message()

    return "I did not understand that. Try rephrasing."

def chatbot():
    print("Chatbot: Hello, I am your CODSOFT Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot:", goodbye_message())
            break
        print("Chatbot:", rule_based_chatbot(user_input))

if __name__ == "__main__":
    chatbot()
