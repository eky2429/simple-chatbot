responses = {
    "hello": "Hello there!",
    "hi": "Hello there!",
    "how are you": "I'm doing great!",
    "your name": "My name is PythonBot!",
    "favorite language": "I like Python!",
    "bye": "Goodbye! Have a great day!",
    "python": "Python is a popular programming language!",
    "joke": ["Why do programmers prefer dark mode?", "Bot: Because light attracts bugs!"]
}

def chatbot():
    print("Bot: Hello! I'm PythonBot.")
    print("Bot: You can talk to me! Type 'bye' to exit.")

    while True:
        # Get input from the user
        user_input = input("You: ").lower().strip()

        # Respond to the user's input
        if user_input in responses:
            response = responses[user_input]
            if type(response) == str:
                print("Bot:", responses[user_input])
            elif type(response) == list:
                for i in response:
                    print("Bot:", i)
            else:
                print("Bot: I don't know how to respond to that yet.")
        else:
            print("Bot: Sorry, I don't understand that yet.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Start the chatbot
    chatbot()