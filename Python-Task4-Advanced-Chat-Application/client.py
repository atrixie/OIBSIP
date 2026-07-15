from tkinter import filedialog
import os
from protocol import create_message
from protocol import read_message
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

root = tk.Tk()
root.title("💬 Advanced Chat Application")
root.geometry("850x700")
root.configure(bg="#F4F6F8")

username = simpledialog.askstring(
    "Login",
    "Enter your username:",
    parent=root
)

if not username:
    messagebox.showerror("Error", "Username cannot be empty.")
    exit()

title = tk.Label(
    root,
    text=f"💬 Welcome, {username}",
    font=("Segoe UI",20,"bold"),
    bg="#1F3B73",
    fg="white",
    pady=12
)

title.pack(fill="x")

chat_box = scrolledtext.ScrolledText(
    root,
    width=70,
    height=25,
    font=("Consolas",11),
    bg="white",
    fg="black",
    insertbackground="black",
    state="disabled"
)
chat_box.pack(
    padx=15,
    pady=10
)

try:

    with open(
        "chat_history.txt",
        "r",
        encoding="utf-8"
    ) as file:

        chat_box.config(state="normal")

        chat_box.insert(
            tk.END,
            file.read()
        )

        chat_box.config(state="disabled")

        chat_box.see(tk.END)

except FileNotFoundError:

    pass

bottom_frame = tk.Frame(
    root,
    bg="#F4F6F8"
)

bottom_frame.pack(
    fill="x",
    pady=10
)

message_entry = tk.Entry(
    bottom_frame,
    font=("Segoe UI",12),
    width=55
)

message_entry.pack(
    side="left",
    padx=10,
    pady=10,
    fill="x",
    expand=True
)

def receive():

    while True:

        try:

            message = client.recv(1024).decode()

            if message == "USERNAME":

                client.send(username.encode())

            else:

                current = datetime.now().strftime("%H:%M")

                formatted = f"[{current}] {message}\n"

                chat_box.config(state="normal")

                chat_box.insert(
                    tk.END,
                    formatted
                )

                root.bell()

                with open(
                    "chat_history.txt",
                    "a",
                    encoding="utf-8"
                ) as file:

                    file.write(formatted)

                chat_box.config(state="disabled")

                chat_box.see(tk.END)

        except:

            break

def send_message():

    message = message_entry.get().strip()

    if message == "":
        return

    client.send(f"{username}: {message}".encode())

    message_entry.delete(0, tk.END)

def clear_chat():

    chat_box.config(state="normal")

    chat_box.delete("1.0", tk.END)

    chat_box.config(state="disabled")

    open("chat_history.txt", "w").close()
    
send_btn = tk.Button(
    bottom_frame,
    text="Send",
    font=("Segoe UI",12,"bold"),
    bg="#1F3B73",
    fg="white",
    width=10,
    command=send_message
)

send_btn.pack(
    side="left",
    padx=10
)

emoji_btn = tk.Button(
    bottom_frame,
    text="😊",
    font=("Segoe UI",13),
    command=lambda: message_entry.insert(
        tk.END,
        "😊"
    )
)

emoji_btn.pack(
    side="left",
    padx=5
)

clear_btn = tk.Button(
    bottom_frame,
    text="🗑",
    font=("Segoe UI",12),
    command=clear_chat
)

clear_btn.pack(
    side="left",
    padx=5
)

message_entry.bind(
    "<Return>",
    lambda event: send_message()
)
receive_thread = threading.Thread(
    target=receive
)

receive_thread.daemon = True

receive_thread.start()

message_entry.focus()

root.mainloop()