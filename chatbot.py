# Define the chatbot
def chatbot():

# Getting input from user  
    user = input("User: ").lower()

# Uses conditional statements to evaluate user input and display appropriate responses
    if user == "goodbye":
        print("Chatbot: Goodbye! Have a nice day!")
        return
    elif user == "hi" or user == "hello":
        print("Chatbot: Hi there! How can I help you?")
    elif user == "how are you?":
        print("Chatbot: I'm just a program, but thanks for asking!")
    elif user == "what is your name?":
        print("Chatbot: I'm Chatbot, your virtual assistant.")
    elif user == "what is python?":
        print("Chatbot: Python is an high level, Interpreted Language")
    else:
        print("Chatbot: I'm not sure how to respond to that.")

# Calling the chatbot function
    chatbot()

chatbot()
