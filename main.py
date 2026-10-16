# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def chatbot():
    print("Bot: Hello! I'm PythonBot.")
    print("Bot: You can talk to me! Type 'bye' to exit.")

    while True:
        # Get input from the user
        user_input = input("You: ").lower().strip()

        # Respond to the user's input
        if user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How are you?")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Bot: My name is PythonBot!")

        elif "help" in user_input:
            print("Bot: You can say hello, ask my name, or ask how I'm doing.")

        elif "python" in user_input:
            print("Bot: Python is a popular programming language!")

        elif "joke" in user_input:
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        else:
            print("Bot: Sorry, I don't understand that yet.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Start the chatbot
    chatbot()