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

    # t0: Client's timestamp when sending the request
    t0 = time.time()
    clientSocket.send("Time request".encode())

    # Get server's response and parse t1 and t2
    message = clientSocket.recv(bufferSize).decode()
    t1, t2 = map(float, message.split(','))
    
    # t3: Client's timestamp when receiving the server's response
    t3 = time.time()

    # Calculate RTT and offset using NTP formulas
    rtt = (t3 - t0) - (t2 - t1)
    offset = ((t1 - t0) + (t2 - t3)) / 2

    # Adjust the client's time (for the purpose of this assignment, we're just calculating the adjusted time)
    adjusted_time = t3 + offset

    print(f"REMOTE_TIME {adjusted_time*1000:.0f}")
    print(f"LOCAL_TIME {t3*1000:.0f}")
    print(f"RTT_ESTIMATE {rtt*1000:.0f}")

    clientSocket.close()

if __name__ == "__main__":
    main()
