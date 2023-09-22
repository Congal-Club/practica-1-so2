import net from 'node:net'

const server = net.createServer((socket) => {
  console.log('Cliente conectado')

  socket.on('data', (data) => {
    console.log('Mensaje: ', data.toString())
    socket.write('Hola cliente desde el servidor')
  })

  socket.on('end', () => {
    console.log('Cliente desconectado')
  })
})

server.listen(3000, () => {
  console.log('Servidor escuchando en el puerto 3000')
})
