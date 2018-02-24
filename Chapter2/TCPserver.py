import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set ip and port
server.bind((bind_ip, bind_port))

# start waiting (max queue = 5)
server.listen(5)
print("Listening on {ip}:{port}".format(ip=bind_ip, port=bind_port))


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("Recieved: {}".format(request))
    client_socket.send("ACK!".encode())
    client_socket.close()


while True:
    client, addr = server.accept()  # connection start
    print("Accepted connection from: {ip}:{port}".format(
        ip=addr[0], port=addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
