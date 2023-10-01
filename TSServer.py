from socket import *
import time
import threading

# Constants
studentId = 1234  # Change to your last 4 digits of student ID
serverPort = 10000 + studentId
bufferSize = 1024
clients = []


def handleClient(connectionSocket):
    clientTime = float(connectionSocket.recv(bufferSize).decode())
    clients.append(clientTime)

    # Sleep to simulate processing and wait for potential other clients
    # time.sleep(5)

    # avgDifference = sum(clients) / len(clients) - time.time()
    # adjustedTime = time.time() + avgDifference
    curTime = time.time()
    avgDifference = (sum(clients) - curTime * len(clients)) / len(clients)
    adjustedTime = curTime + avgDifference
    msg = f"ADJUSTED TIME:{adjustedTime}"
    connectionSocket.send(msg.encode())
    connectionSocket.close()


def main():

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    print(f"TSServer is listening on port {serverPort} and waiting for client connections...")
    while True:
        connectionSocket, addr = serverSocket.accept()
        clientThread = threading.Thread(
            target=handleClient, args=(connectionSocket,))
        clientThread.start()


if __name__ == "__main__":
    main()
