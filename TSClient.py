from socket import *
import time
import sys

serverName = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
serverPort = 101234  # Update this to match your student ID port
bufferSize = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
startTime = time.time()
clientSocket.connect((serverName, serverPort))
endTime = time.time()

localTime = time.time()
clientSocket.send(str(localTime).encode())

adjustedTime = float(clientSocket.recv(bufferSize).decode())
timeDifference = adjustedTime - localTime

RTT_ESTIMATE = (endTime - startTime) * 1000  # Convert seconds to milliseconds

print(f"REMOTE_TIME {adjustedTime:.0f}")
print(f"LOCAL_TIME {localTime:.0f}")
print(f"RTT_ESTIMATE {RTT_ESTIMATE:.0f}")

clientSocket.close()