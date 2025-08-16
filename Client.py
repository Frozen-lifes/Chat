import socket
import threading

HOST = '127.0.0.1' # Change to server IP if remote
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break
username = input("Enter your name: ")
client.send(f"{username} has joined the chat.".encode())

def send():
    while True:
        message = input()
        full_message = f"{username}: {message}"
        client.send(full_message.encode())
        print(f"Sending: {full_message}")

threading.Thread(target=receive).start()
threading.Thread(target=send).start()