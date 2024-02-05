import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 12345)

# Get the Caesar cipher key from the user
key = int(input('Enter the Caesar cipher key: '))

# Send the key to the server
client_socket.sendto(str(key).encode('utf-8'), server_address)

while True:
    # Get user input
    message = input('Enter a message: ')

    # Send the message to the server
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Receive the encrypted response from the server
    data, _ = client_socket.recvfrom(1024)
    print('Received encrypted response: {}'.format(data.decode('utf-8')))
