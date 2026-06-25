import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from datetime import datetime
import random
import string
def chatbot_response(message):

    message = message.lower().strip()

    # Remove punctuation
    message = message.translate(
        str.maketrans('', '', string.punctuation)
    )

    if "name is" in message:
        user_name = message.split("name is")[-1].strip().title()
        return f"Nice to meet you, {user_name}! How can I help you today?"

    greetings = [
        "Hello! Nice to meet you.",
        "Hi there! How can I help you?",
        "Hey! Nice to see you."
    ]

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did Python go to school? To improve its class!",
        "Why was the computer cold? It left its Windows open!"
    ]

    motivation = [
        "Success is the sum of small efforts repeated every day.",
        "Keep learning. Every expert was once a beginner.",
        "Believe in yourself and keep moving forward."
    ]

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(greetings)

    elif message in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking."

    elif message == "who are you":
        return "I'm a Rule-Based Chatbot developed using Python."

    elif message == "what is your name":
        return "My name is ChatBot."

    elif message == "who created you":
        return "I was created using Python programming."

    elif message == "good morning":
        return "Good morning! Have a wonderful day."

    elif message == "good afternoon":
        return "Good afternoon!"

    elif message == "good evening":
        return "Good evening!"

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message == "what can you do":
        return ("I can answer predefined questions, tell jokes, "
                "provide motivation, and display date & time.")

    elif message == "where are you from":
        return "I live inside a Python program."

    elif any(word in message for word in ["date", "today"]):
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "time" in message:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    elif "joke" in message:
        return random.choice(jokes)

    elif "motivate" in message or "motivation" in message:
        return random.choice(motivation)

    elif message == "help":
        return (
            "Available Commands:\n\n"
            "• hello / hi / hey\n"
            "• my name is <name>\n"
            "• how are you\n"
            "• who are you\n"
            "• what is your name\n"
            "• who created you\n"
            "• good morning\n"
            "• good afternoon\n"
            "• good evening\n"
            "• thank you\n"
            "• what can you do\n"
            "• where are you from\n"
            "• date\n"
            "• time\n"
            "• joke\n"
            "• motivate me\n"
            "• help"
        )

    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."
    
def send_message():

    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_area.insert(tk.END, f"You: {user_message}\n")

    bot_reply = chatbot_response(user_message)

    chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")

    entry.delete(0, tk.END)

    chat_area.see(tk.END)


# ---------------------------------
# GUI Window
# ---------------------------------
root = tk.Tk()

root.title("Interactive Rule-Based Chatbot")
root.geometry("800x750")
root.resizable(False, False)

# ---------------------------------
# Robot Logo
# ---------------------------------
image = Image.open("robot.png")
image = image.resize((170, 170))

robot_img = ImageTk.PhotoImage(image)

logo_label = tk.Label(root, image=robot_img)
logo_label.pack(pady=10)

# ---------------------------------
# Title
# ---------------------------------
title_label = tk.Label(
    root,
    text="Interactive Rule-Based Chatbot",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=5)

# ---------------------------------
# Chat Area
# ---------------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=22,
    font=("Arial", 11)
)

chat_area.pack(padx=15, pady=15)

chat_area.insert(
    tk.END,
    "🤖 Bot: Welcome to the Interactive Rule-Based Chatbot!\n"
    "🤖 Bot: Type 'help' to see available commands.\n\n"
)

# ---------------------------------
# Input Box
# ---------------------------------
entry = tk.Entry(
    root,
    width=60,
    font=("Arial", 12)
)

entry.pack(pady=10)

# ---------------------------------
# Send Button
# ---------------------------------
send_button = tk.Button(
    root,
    text="Send",
    command=send_message,
    width=15,
    font=("Arial", 12)
)

send_button.pack(pady=5)

# Press Enter to Send Message
entry.bind("<Return>", lambda event: send_message())

# ---------------------------------
# Run Application
# ---------------------------------
root.mainloop()