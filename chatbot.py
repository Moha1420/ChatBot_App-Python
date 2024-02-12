import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'I\'m Chatbot.']),
    (r'quit', ['Bye, take care!', 'Goodbye, have a great day!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome to the chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'quit':
        break
