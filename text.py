import tkinter as tk
from tkinter import ttk, Scrollbar
import random

# Your chatbot response function (simple example for demonstration)
def chatbot_response(user_input):
    # For this example, the bot will just echo the input.
    return f"Echo: {user_input}"

def send_message():
    message = user_input.get()
    if message:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {message}\n")
        chat_area.config(state=tk.DISABLED)

        response = chatbot_response(message)
        
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Bot: {response}\n")
        chat_area.config(state=tk.DISABLED)
        
        user_input.delete(0, tk.END)
        chat_area.yview(tk.END)  # Scroll to the bottom to see latest message
class SimpleChatbot:
    def __init__(self):
        # Create a dictionary of responses
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm good, thanks for asking.",
            "bye": "Goodbye!",
            "what is your name": "I'm a simple chatbot."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()  # Convert input to lowercase
        # Look for a response, return a default one if not found
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")
def chatbot_response(user_input):
    user_input = user_input.lower(user_input)

    # Define keywords and associated responses
    greetings = ['hello', 'hi', 'hey']
    farewells = ['bye', 'goodbye', 'see you']
    gratitude = ['thank', 'thanks', 'appreciate']
    how_are_you = ['how are you', 'how\'s it going', 'how have you been', "What's up"]

    if any(keyword in user_input for keyword in greetings):
        return "Hello! How can I help you today?"
    
    if any(keyword in user_input for keyword in farewells):
        return "Goodbye! If you have any more questions, feel free to ask. Take care!"
    
    if any(keyword in user_input for keyword in gratitude):
        return "You're welcome! Let me know if there's anything else."
    
    if any(keyword in user_input for keyword in how_are_you):
        return "I'm just a program, so I don't have feelings, but thanks for asking! How can I assist you further?"

    return "I'm not sure how to respond to that. Can you provide more information?"

# Example usage:
print(chatbot_response("Hey there!"))
print(chatbot_response("Thanks for the help!"))
print(chatbot_response("How's everything going?"))
print(chatbot_response("Goodbye!"))
print(chatbot_response("What's the capital of France?"))

# Example usage
bot = SimpleChatbot()

print(bot.get_response("Hello"))
print(bot.get_response("How are you"))
print(bot.get_response("What's up"))
print(bot.get_response("What is your name"))
print(bot.get_response("Bye"))


app = tk.Tk()
app.title("Chatbot")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

scrollbar = Scrollbar(frame)
chat_area = tk.Text(frame, wrap=tk.WORD, state=tk.DISABLED, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

user_input = ttk.Entry(app, width=50)
user_input.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

send_button = ttk.Button(app, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

user_input.bind("<Return>", lambda event=None: send_message())

app.mainloop()
