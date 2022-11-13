import socket

PORT = 5050
SERVER_NAME = 'localhost'
SERVER_IP = '127.0.0.1'

BUFF_SIZE = 4096

DISCONNECT_MESSAGE = ""


def send(msg):
  message = msg.encode('utf-8')
  msg_length = len(message)
  send_length = str(msg_length).encode('utf-8')

  # pad message to be send to BUFF_SIZE
  send_length += b' ' * (BUFF_SIZE - len(send_length))

  client.send(send_length)
  client.send(message)
  print(client.recv(BUFF_SIZE))

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the server given with (SERVER_IP, PORT) tupple:
client.connect((SERVER_IP, PORT))
print(f'Client is conected to {(SERVER_IP, PORT)} ')


# send some messages:
while True:
  msg = input("Enter a message:")
  if msg == '':
    send(DISCONNECT_MESSAGE)
  else:
    send(msg)