#!/usr/bin/env python3
import socket
import sys

def start_server():
    # The server will listen on all interfaces at port 5000.
    host = ''  # '' means all available interfaces.
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except Exception as e:
        print(f"Error binding server: {e}")
        sys.exit(1)

    s.listen(1)
    print(f"Server listening on port {port}...")

    while True:
        conn, addr = s.accept()
        print(f"Connection established from {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            print("Received:", data.decode())
            conn.sendall(f"ACK: {data.decode()}".encode())

        conn.close()
        print("Connection closed.")


def start_client():
    # The client connects to the server at the specified host and port.
    host = '127.0.0.1'  # Replace with server IP if running on different machines.
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except Exception as e:
        print(f"Unable to connect to the server: {e}")
        sys.exit(1)

    message = "Hello from client!"
    print("Sending message:", message)
    s.sendall(message.encode())

    data = s.recv(1024)
    print("Received from server:", data.decode())
    s.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 network_script.py [server|client]")
        sys.exit(1)

    if sys.argv[1].lower() == "server":
        start_server()
    elif sys.argv[1].lower() == "client":
        start_client()
    else:
        print("Invalid option. Use 'server' or 'client'.")
