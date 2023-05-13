import socket
import pickle # let us send objects also
import os
import time
from colorama import Fore,Back,Style

HEADER = 64
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "address ip that you put in the server.py"
ADDR = (SERVER,PORT)
NAME=""

os.system("cls")

chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def timeToRestart(seconds):
    """
    Function that restarting tries to connect every give period

    params:
    seconds: a period of time in what you want to ask the the server to connection again
    """
    for x in range(seconds,-1,-1):
        time.sleep(1)
        print("Trying connect again in {} seconds".format(x))


def tries(ADDR:tuple,FORMAT:str):
    """
    Function that lets the program to try to connect to the selected server

    params:
    ADDR: parameters to what server do you want to connect (IP, PORT)
    FORMAT: in this case that is the quick shortcut ("utf-8")
    """
    while True:
        try:
            chat.connect(ADDR)
            print(Fore.GREEN + chat.recv(2048).decode(FORMAT))
            break
        except Exception :
            print(Fore.RED + "The SERVER {} {} does not respond to the connection asks".format(ADDR[0],ADDR[1]))
            timeToRestart(3)
            os.system("cls")
            continue

def timer(seconds:int):
    """
    Function that measures the time elapsed in seconds

    params:
    seconds:  a period of time in what you want to clear the console
    """
    for x in range(seconds,-1,-1):
        time.sleep(1)
        print(Fore.YELLOW+"Clearing the console in {} seconds".format(x))

def connection(SERVER:str,PORT:str,NAME):
    """
    Function  that is asking what do we want to send to the server

    params:
    SERVER: that is the ip of the server with which the program is currently connected
    PORT: port on which server is listening
    """
    global i
    while True:
            try:

                message = chat.recv(2048).decode(FORMAT)
                if "left" in message:
                    print(Fore.RED + message)
                else:
                    print(Fore.GREEN + message)
            except Exception as e:
                print(Fore.RED + "The SERVER {} {} aborted the connection".format(SERVER,PORT))
                # print("ERROR: {}".format(e))
                i=1
                break
def send(msg:str):
    """
    This function is responsible for proper sending of messages to the server with which the program is currently connected

    params:
    msg: message that we want to send to the server
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    chat.send(send_length)
    chat.send(message)
    if msg=="?online?":
        online = chat.recv(2048).decode(FORMAT)
        if online=="1":
            print(Fore.WHITE + "There are currently {} person online".format(online))
        else:
            print(Fore.WHITE + "There are currently {} people online".format(online))
    else:
        print(Fore.GREEN + chat.recv(2048).decode(FORMAT))

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)


tries(ADDR,FORMAT)
print(chat.recv(2048).decode(FORMAT))
connection(SERVER,PORT,NAME)

if i==1:

    pass

else:

    send(DISCONNECT_MESSAGE)

timer(3)
os.system("cls")

print(Fore.WHITE)

