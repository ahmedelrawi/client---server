import socket

# # Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',9090))

file = open('dpfd.jpg','rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)


file.close()
client.close()