
# CodeAlpha Internship - Task 4
# Basic Chatbot
# Developed by Sunil Balmani

def chatbot():

    print("=" * 40)
    print("       SUNIL'S PYTHON CHATBOT")
    print("=" * 40)

    print("Bot: Hello! Welcome to my chatbot.")
    print("Bot: Type 'bye' to exit the conversation.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I'm Sunil's Python Chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created by Sunil Balmani.")

        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that message.")

    print("\nChat session ended.")


# Start the chatbot
chatbot()
