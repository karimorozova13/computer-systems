from threading import Thread
from socket_server import echo_server
from client_socket import simple_client

HOST = '127.0.0.1'
PORT = 55555

server = Thread(target=echo_server, args=(HOST, PORT))
client = Thread(target=simple_client, args=(HOST, PORT))

server.start()
client.start()
server.join()
client.join()
print('Done!')
