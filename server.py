import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('UDP server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a message from the client
    data, client_address = server_socket.recvfrom(1024)

    # Process the received data
    print('Received message from {}: {}'.format(client_address, data.decode('utf-8')))

    # Send a response back to the client
    response = 'Hello, client!'
    server_socket.sendto(response.encode('utf-8'), client_address)
