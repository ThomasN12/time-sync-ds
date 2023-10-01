from socket import *
import time
import sys

serverName = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
studentId = 1234
serverPort = 10000 + studentId  # Update this to match your student ID port
bufferSize = 1024


def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    try:
        clientSocket.connect((serverName, serverPort))

        timeSent = time.time()
        clientSocket.send(str(timeSent).encode())
        while True:
            received_msg = clientSocket.recv(bufferSize).decode()
            if "ADJUSTED TIME" in received_msg:
                timeReceived = time.time()
                localTime = time.time() * 1000
                adjustedTime = float(received_msg.split(":")[1])
                # timeDifference = adjustedTime - localTime

                rttEstimate = (timeReceived - timeSent) * 1000

                print(f"REMOTE_TIME {adjustedTime:.0f}")
                print(f"LOCAL_TIME {localTime:.0f}")
                print(f"RTT_ESTIMATE {rttEstimate:.0f}")
            else:
                break
    except Exception as e:
        clientSocket.close()


if __name__ == "__main__":
    main()
