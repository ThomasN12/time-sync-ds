from socket import *
import time
import sys

serverName = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
studentId = 1234
serverPort = 10000 + studentId
bufferSize = 1024


def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # Timestamp when client send request
    t1 = time.time()
    clientSocket.send("Sending request for time...".encode())

    # Retrieve timestamps from server
    message = clientSocket.recv(bufferSize).decode()
    t2 = float(message.split(",")[0])
    t3 = float(message.split(",")[1])

    # Timestamp when client receive response from server
    t4 = time.time()

    # RTT & Offset calculation
    rtt = (t4 - t1) - (t3 - t2)
    offset = ((t2 - t1) + (t3 - t4)) / 2

    # Adjust the client's time
    adjustedTime = t4 + offset

    print(f"REMOTE_TIME {adjustedTime * 1000:.0f}")
    print(f"LOCAL_TIME {t4 * 1000:.0f}")
    print(f"RTT_ESTIMATE {rtt * 1000:.0f}")

    clientSocket.close()


if __name__ == "__main__":
    main()
