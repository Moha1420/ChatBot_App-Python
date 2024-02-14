import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")
        master.configure(background='#87CEEB')  # Set background color to sky blue

        frame = tk.Frame(master, background='#87CEEB')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame in the window

        self.chat_history = scrolledtext.ScrolledText(frame, width=50, height=20, font=("Arial", 16, "bold"))
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.user_input = tk.Entry(frame, width=30, font=("Arial", 16, "bold"))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(frame, text="Send", command=self.send_message, font=("Arial", 16, "bold"))
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.chat_history.insert(tk.END, "Chatbot: Welcome! How can I help you?\n")
        self.user_input.focus()

        self.chatbot = Chat(self.get_chatbot_pairs(), reflections)

    def send_message(self):
        user_message = self.user_input.get()
        self.chat_history.insert(tk.END, "You: {}\n".format(user_message))
        self.user_input.delete(0, tk.END)

        response = self.chatbot.respond(user_message)
        self.chat_history.insert(tk.END, "Chatbot: {}\n".format(response))

    def get_chatbot_pairs(self):
        pairs = [
            [
                r"hi|hello|hey",
                ["Hello!", "Hey there!", "Hi! How can I help you today?"]
            ],
            [
                r"how are you ?",
                ["I'm doing well, thank you!", "I'm good, thanks for asking!"]
            ],
            [
                r"What is your name ?",
                ["You can call me Chatbot.", "I'm Chatbot!"]
            ],
            [
                r"your name should be (.*)",
                ["Sure! From now on, you can call me %1.", "Okay, I'll go by %1."]
            ],
            [
                r"what can you do ?",
                ["I can provide information, chat with you, and more. Feel free to ask me anything!"]
            ],
            [
                r"(.*) help (.*)",
                ["I can assist you with various tasks. Please specify what you need help with."]
            ],
            [
                r"quit",
                ["Bye for now. Take care!", "Goodbye!"]
            ],
            [
                r"(.*)",
                ["Sorry, I am a basic chatbot. I didn't understand your message."]
            ]
        ]
        return pairs

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
