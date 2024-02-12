import tkinter as tk
from tkinter import scrolledtext

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")
        master.configure(background='green')  # Set background color to green

        self.chat_history = scrolledtext.ScrolledText(master, width=50, height=20)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.user_input = tk.Entry(master, width=30)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.chat_history.insert(tk.END, "Chatbot: Welcome! How can I help you?\n")
        self.user_input.focus()

        self.question = None
        self.response_entry = None

    def ask_question(self, question):
        if self.response_entry:
            self.response_entry.grid_forget()  # Remove previous response entry widget

        self.question = question
        self.chat_history.insert(tk.END, "Chatbot: {}\n".format(question))
        self.user_input.delete(0, tk.END)

    def show_response_entry(self):
        self.response_entry = tk.Entry(self.master, width=30)
        self.response_entry.grid(row=2, column=0, padx=10, pady=10)
        self.response_entry.focus()

    def send_message(self):
        user_message = self.user_input.get()
        self.chat_history.insert(tk.END, "You: {}\n".format(user_message))
        self.user_input.delete(0, tk.END)

        if self.question:
            response = self.response_entry.get()
            self.chat_history.insert(tk.END, "Response: {}\n".format(response))
            self.question = None
            self.show_response_entry()
        else:
            # Replace this with your chatbot logic
            response = "Chatbot: Sorry, I am a dummy chatbot. I don't know how to respond yet!\n"
            self.chat_history.insert(tk.END, response)

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    app.show_response_entry()  # Initially show the response entry widget
    root.mainloop()

if __name__ == "__main__":
    main()
