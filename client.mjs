import net from 'node:net'

const client = new net.Socket()

client.connect(3000, 'localhost', () => {
  console.log('Conectado al servidor')
  console.log('Hola Servidor')
})

client.on('data', (data) => {
  console.log('Mensaje: ', data.toString())
  client.end()
})

client.on('end', () => {
  console.log('Desconectado del servidor')
})
