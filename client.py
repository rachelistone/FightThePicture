import socket

HEADER = 64 # the maximum size of a massage from the client, if he wants he can send another 64 bytes massage to continue the massage, like packages
DISCONNECT_MASSAGE = 'disconnect'
PORT = 5050 # avalible port in my machine
SERVER = '192.168.56.1' # get the ip adress of the machine I would run the socket on
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    padded_massage = send_length + b' ' * (HEADER - len(send_length))
    client.send(padded_massage)
    client.send(message)
    print(client.recv(len('msg recieved')).decode(FORMAT))

send('hello wourld!')
send(DISCONNECT_MASSAGE)