from socket import *
import time
import threading

# Constants
SERVER_PORT = 12000
BUFFER_SIZE = 1024
clients = []


def handle_client(connectionSocket):
    client_time = float(connectionSocket.recv(BUFFER_SIZE).decode())
    clients.append(client_time)

    # Sleep to simulate processing and wait for potential other clients
    time.sleep(5)

    avg_difference = (sum(clients) - len(clients) * time.time()) / len(clients)
    adjusted_time = time.time() + avg_difference

    connectionSocket.send(str(adjusted_time).encode())
    connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', SERVER_PORT))
serverSocket.listen(5)

print("TSServer is waiting for client connections...")

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(
        target=handle_client, args=(connectionSocket,))
    client_thread.start()
