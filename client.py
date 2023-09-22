from socket import socket, AF_INET, SOCK_STREAM

hots, port = 'localhost', 8080

client = socket(AF_INET, SOCK_STREAM)
client.connect((hots, port))

print('Conectado al servidor')
client.send('Hola cliente desde el servidor'.encode())

message = client.recv(1024)
print(f'Mensaje: {message.decode("utf-8")}')

client.close()
print('Desconectado del servidor')
