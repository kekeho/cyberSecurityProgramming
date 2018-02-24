import socket

target_host = "0.0.0.0"
target_port = 8090

# make client object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect((target_host, target_port))

# send data
client.send("GET / HTTP/1.1\r\nHost: google.co.jp\r\n\r\n".encode())

# receive data
response = client.recv(4096)

print(response.decode())
