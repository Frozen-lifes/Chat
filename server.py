import socket
import threading

HOST = '127.0.0.1'  # Listen on all interfaces
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
            print(f"[RECEIVED] {message.decode()}")
        except:
            clients.remove(client)
            client.close()
            break

print(f"Server listening on {HOST}:{PORT}")
while True:
    client, addr = server.accept()
    print(f"Connected with {addr}")
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()