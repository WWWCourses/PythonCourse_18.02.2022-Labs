import socket
import threading

PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())


def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")
  connected = True

  while connected:
    msg_length = conn.recv(BUFF_SIZE)

    if msg_length:
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)
    if msg == DISCONNECT_MESSAGE:
    connected = False

    print(f"[{addr}] {msg}")
    conn.send("Msg received".encode(FORMAT))

    conn.close()


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
server.bind((SERVER_IP, PORT))

server.listen()
print(f"Server is listening on {SERVER_IP}")


while True:
  conn, addr = s.accept()
  # better to do with threading
  handle_client(conn, addr)

#   print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")