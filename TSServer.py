from socket import *
import time
import threading

studentId = 5187
serverPort = 10000 + studentId
bufferSize = 1024


def handleClient(connectionSocket):
    try:
        message = connectionSocket.recv(bufferSize).decode()
        print(f'Message: {message}')
        # Message reception timestamp
        recv_time = time.time()

        # Sleep to simulate processing
        time.sleep(2)

        # Server's reply timestamp
        connectionSocket.send(f"{recv_time},{time.time()}".encode())
        connectionSocket.close()
    except Exception as e:
        print(e)


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"Server is listening on port {serverPort}")

    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            clientThread = threading.Thread(
                target=handleClient, args=(connectionSocket,))
            clientThread.start()
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    main()
