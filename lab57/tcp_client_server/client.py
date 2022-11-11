import socket

PORT = 5050
SERVER_NAME = 'localhost'
SERVER_IP = socket.gethostbyname(SERVER_NAME)

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# now connect to the server given with (SERVER_IP, PORT) tupple:
client.connect((SERVER_IP, PORT))
print(f'Client is conected to {(SERVER_IP, PORT)} ')