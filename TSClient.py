from socket import *
import time

SERVER_NAME = 'localhost'  # Change to your server's IP when testing on a remote server
SERVER_PORT = 12000
BUFFER_SIZE = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))

local_time = time.time()
clientSocket.send(str(local_time).encode())

adjusted_time = float(clientSocket.recv(BUFFER_SIZE).decode())
time_difference = adjusted_time - local_time
print(f"Time Difference from Server: {time_difference}")

clientSocket.close()