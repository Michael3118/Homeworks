import socket
import multiprocessing


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()


def echo_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(5)
    print("[INFO] Server listening on port 8888")

    while True:
        client_socket, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr}")

        # Create a new process to handle the client
        client_handler = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    echo_server()
