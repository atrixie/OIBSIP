from protocol import read_message
from protocol import create_message
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle(client):

    while True:

        try:

            message = client.recv(1024)

            broadcast(message)

        except:

            if client in clients:

                index = clients.index(client)

                clients.remove(client)

                username = usernames[index]

                usernames.remove(username)

                broadcast(f"{username} left the chat.".encode())

                client.close()

            break


def receive():

    print("Server Started...")

    while True:

        client, address = server.accept()

        print(f"Connected with {address}")

        client.send("USERNAME".encode())

        username = client.recv(1024).decode()

        usernames.append(username)

        clients.append(client)

        print(f"{username} Joined")

        broadcast(f"{username} joined the chat.".encode())

        client.send("Connected Successfully!".encode())

        thread = threading.Thread(target=handle, args=(client,))

        thread.start()


receive()