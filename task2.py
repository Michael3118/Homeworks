import socket
import threading

def handle_client(client_socket):
    # Receive and echo back data
    data = client_socket.recv(1024)
    client_socket.send(data)
    client_socket.close()

def echo_server():
    # Set up the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)

    print("[*] Listening on 127.0.0.1:8080")

    try:
        while True:
            # Accept a connection and start a new thread to handle it
            client, addr = server.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")
        server.close()

if __name__ == "__main__":
    echo_server()
