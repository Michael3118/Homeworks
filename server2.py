import socket

def caesar_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('UDP server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a message from the client
    data, client_address = server_socket.recvfrom(1024)

    # Process the received data using Caesar cipher
    key = int(data.decode('utf-8'))
    response = caesar_cipher('Hello, client!', key)

    # Send the encrypted response back to the client
    server_socket.sendto(response.encode('utf-8'), client_address)
