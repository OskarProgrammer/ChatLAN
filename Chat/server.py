import socket
import threading
import time
import os
from colorama import Fore,Back,Style

global connected
global KONIEC
KONIEC = True
connected=True
HEADER = 64
PORT = 5050 #exactly this port number
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR2 =(SERVER,5060)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server2.bind(ADDR2)


print(Fore.WHITE)
os.system("cls")




def configuration(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
            msg_length = int(msg_length)            #calculating the size of the message
            name = conn.recv(msg_length).decode(FORMAT)
    return name

def checkCountActiveUsers():
    return str(threading.active_count()-1)


dict = {

}

def handle_client(conn:str,addr:list,):
    """
    Function that is working on a isolated thread to ensure the smooth flow of messages between the server and the client

    params:
    conn: socket
    addr: _RetAddress
    """
    global connected
    global KONIEC
    print(Fore.GREEN +"[NEW CONNECTION] {} {} connected".format(addr[0],addr[1]))

    conn.send("SUCCESFULLY CONNECTED TO {} {}".format(ADDR[0],ADDR[1]).encode(FORMAT))
    conn.send("Write your nickname: ".encode(FORMAT))
    name = configuration(conn)

    dict[name] = conn
    print(Fore.YELLOW + "{} {} SET THE NAME: {}".format(ADDR[0],ADDR[1],name))
    print(Fore.LIGHTCYAN_EX + "{} joined the chat".format(name))
    conn1.send("{} joined the chat".format(name).encode(FORMAT))
    conn.send("Your nickname is {}".format(name).encode(FORMAT))
    conn.send(str((threading.active_count()-1)).encode(FORMAT))


    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:

            msg_length = int(msg_length)                            #calculating the size of the message
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                print(Fore.RED + "{} left the chat".format(name))
                conn1.send("{} left the chat".format(name).encode(FORMAT))
                conn.send("Connection interrupted successfully".encode(FORMAT))
                connected = False
            elif msg == "?online?":
                print(Fore.YELLOW + "{} CHECKED HOW MUCH ARE USERS ON THE CHAT".format(name))
                conn.send(str((threading.active_count()-1)).encode(FORMAT))
                connected = True

            else:
                print(Fore.GREEN + "{}: {}".format(name,msg))
                conn1.send("{}: {}".format(name,msg).encode(FORMAT))
                # if KONIEC==False:
                #      conn.send("You were kicked by the admin".format(msg).encode(FORMAT))
                #      connected = False
                #      break
                # else:
                conn.send("Message received".format(msg).encode(FORMAT))
                connected = True

    conn.close()

# def commands():
#     global connected
#     global KONIEC
#     while KONIEC:
#         command = input(Fore.RED + "")
#         command = command.split(" ")
#         if command[0] == "KICK":
#             name = command[1]
#             print(Fore.RED + "{} was kicked".format(name))
#             conn = dict [name]
#             conn.send('You were kicked by the ADMIN!'.encode(FORMAT))
#             KONIEC=False
#             connected = False

#         else: KONIEC=True




def start():
    """
    Function that starts the listening on the server that is already started before calling this function

    """
    # thread1=threading.Thread(target = commands)
    # thread1.start()
    server.listen()#set server to listening
    print(Fore.GREEN +"[LISTENING] Server is listening on {} {}".format(SERVER,PORT))
    while True:
        conn, addr = server.accept() #will wait for a new connection to the server and collect data of who just connected
        thread = threading.Thread(target=handle_client, args = (conn,addr))#setting the thread to the handle_client with two arguments
        thread.start()#starting the thread
        print(Fore.WHITE + f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print(Fore.GREEN + "[STARTING] Server is starting ")


server2.listen()
conn1, addr1 = server2.accept()
conn1.send("CONNECTED TO THE CHAT".encode("utf-8"))

online = checkCountActiveUsers()

print(Fore.CYAN + "[CHAT ADDED] CHAT STARTED!")
start()

##AF_INET lets us to use our computer us server
