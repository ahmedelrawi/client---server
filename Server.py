import socket






server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',9090))
server.listen(1)

client_socket, client_address = server.accept()
file = open('received_dpfd.jpg','wb')
image_data = client_socket.recv(2048)



while image_data:
    file.write(image_data)
    image_data = client_socket.recv(2048)


file.close()
client_socket.close()

