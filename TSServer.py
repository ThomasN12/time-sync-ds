from socket import *
import time
import threading

studentId = 1234
serverPort = 10000 + studentId
bufferSize = 1024


def handleClient(connectionSocket):
    # Message reception timestamp
    recv_time = time.time()

    # Sleep to simulate processing and wait for potential other clients
    # time.sleep(5)

    # Server's reply timestamp
    connectionSocket.send(f"{recv_time},{time.time()}".encode())
    connectionSocket.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"Server is listening on port {serverPort}")

    while True:
        connectionSocket, addr = serverSocket.accept()
        clientThread = threading.Thread(
            target=handleClient, args=(connectionSocket))
        clientThread.start()


if __name__ == "__main__":
    main()
