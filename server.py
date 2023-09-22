from socket import socket, AF_INET, SOCK_STREAM

hots, port = 'localhost', 8080

server = socket(AF_INET, SOCK_STREAM)
server.bind((hots, port))
server.listen(5)

print('Servidor esperando conexiones...')
client, addr = server.accept()
print(f'Cliente conectado desde: {addr}')

while True:
    data = client.recv(1024)

    if not data:
        break
    
    print(f'Mensaje: {data.decode("utf-8")}')
    client.send('Hola cliente desde el servidor'.encode())

print('Cliente desconectado')

client.close()
server.close()
