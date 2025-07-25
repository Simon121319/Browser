import socket

# Create a socket and connect to the server
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('example.com', 80))  # Using HTTP (port 80)

# Send a properly formatted HTTP GET request
cmd = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'.encode()  # Correct format
mysock.send(cmd)

# Receive and print the response
while True:
    data = mysock.recv(512)  # Read 512 bytes at a time
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()  # Close the connection