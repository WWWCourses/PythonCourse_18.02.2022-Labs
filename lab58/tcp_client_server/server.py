import socket
import threading

PORT = 5050
SERVER_IP = '127.0.0.1'
BUFF_SIZE = 4096

DISCONNECT_MESSAGE=""


def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")
  connected = True

  while connected:
    msg_length = conn.recv(BUFF_SIZE)

    if msg_length:
      # print(f'msg_length: {msg_length}')
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode('utf-8')
      if msg == DISCONNECT_MESSAGE:
        connected = False

    print(f"[{addr}] {msg}")
    conn.send("Msg received".encode('utf-8'))

    # conn.close()


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
server.bind((SERVER_IP, PORT))

server.listen()
print(f"Server is listening on {SERVER_IP}")


while True:
  conn, addr = server.accept()
  # better to do with threading
  handle_client(conn, addr)

#   print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")