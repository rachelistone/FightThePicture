import socket
import threading

HEADER = 64   # the maximum size of a massage from the client, if he wants he can send another 64 bytes massage to continue the massage, like packages
DISCONNECT_MASSAGE = 'disconnect'
PORT = 5050  # avalible port in my machine
SERVER = socket.gethostbyname(socket.gethostname())  # get the ip adress of the machine I would run the socket on
ADDR = (SERVER, PORT)  # represent the server address
FORMAT = 'utf-8'

# the server is a socket object getting the type of ip adress to wait for, and the type of data it gets
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server to my adress, so that the things that will connect to this address would hit the socket
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")

    connected  = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MASSAGE:
                connected = False
            print(f"[{addr}]: {msg}")
            conn.send('msg recieved'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING]: server is listening on {ADDR}")
    while True:
        # will wait for the client connection and get an object to send him information through - his socket, and his details about the connection e.g. address
        conn, addr = server.accept()
        # initialize a new thread for that client request, the target is the function that will serve him in that thread and the args - passed to the thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # start running the thred
        thread.start()
        # prints how many threads does the server have, -1 is besides the main which listens
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount()-1}")

print("[STARTING]: the server is starting")
start()