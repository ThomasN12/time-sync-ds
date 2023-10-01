from socket import *
import time

studentId = 1234
serverPort = 10000 + studentId
bufferSize = 1024

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"Server is listening on port {serverPort}")

    while True:
        connectionSocket, addr = serverSocket.accept()
        
        # t1: Server's timestamp when the request is received
        t1 = time.time()
        
        # t2: Server's timestamp when sending the reply
        t2 = time.time()
        message = f"{t1},{t2}"
        connectionSocket.send(message.encode())
        connectionSocket.close()

if __name__ == "__main__":
    main()
