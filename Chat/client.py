import socket
import pickle # let us send objects also
import os
import time
from colorama import Fore,Back,Style

global i
i=0
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.24"
ADDR = (SERVER,PORT)
NAME=""

def timer(seconds:int):
    """
    Function that measures the time elapsed in seconds

    params:
    seconds:  a period of time in what you want to clear the console
    """
    for x in range(seconds,-1,-1):
        time.sleep(1)
        print(Fore.YELLOW + "Clearing the console in {} seconds".format(x))


def timeToRestart(seconds):
    """
    Function that restarting tries to connect every give period

    params:
    seconds: a period of time in what you want to ask the the server to connection again
    """
    for x in range(seconds,0,-1):
        time.sleep(1)
        print("Trying connect again in {} seconds".format(x))

os.system("cls")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def tries(ADDR:tuple,FORMAT:str):
    """
    Function that lets the program to try to connect to the selected server

    params:
    ADDR: parameters to what server do you want to connect (IP, PORT)
    FORMAT: in this case that is the quick shortcut ("utf-8")
    """
    while True:
        try:
            client.connect(ADDR)
            print(Fore.GREEN + client.recv(2048).decode(FORMAT))
            break
        except Exception :
            print(Fore.RED + "The SERVER {} {} does not respond to the connection asks".format(ADDR[0],ADDR[1]))
            timeToRestart(5)
            os.system("cls")
            continue

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
    client.send(send_length)
    client.send(message)
    if msg=="?online?":
        online = client.recv(2048).decode(FORMAT)
        if online=="1":
            print(Fore.WHITE + "There are currently {} person online".format(online))
        else:
            print(Fore.WHITE + "There are currently {} people online".format(online))
    else:
        print(Fore.GREEN + client.recv(2048).decode(FORMAT))

def connection(SERVER:str,PORT:str,NAME):
    """
    Function  that is asking what do we want to send to the server

    params:
    SERVER: that is the ip of the server with which the program is currently connected
    PORT: port on which server is listening
    """
    global i
    online = client.recv(2048).decode(FORMAT)
    print("You can now chat with your friends")
    print("There are {} people online".format(online))
    while True:
            message = input(Fore.WHITE + "{}: ".format(NAME))
            if message == "exit":
                break
            try:
                if message == "cls":
                    os.system("cls")

                else:
                    send(message)

            except Exception as e:
                print(Fore.RED + "The SERVER {} {} aborted the connection".format(SERVER,PORT))
                # print("ERROR: {}".format(e))
                i=1
                break

def configuration(SERVER:str,PORT:str,NAME=""):
    print(Fore.GREEN + client.recv(2048).decode(FORMAT))
    NAME = input (Fore.WHITE +"".format(SERVER))
    send(NAME)
    return NAME
ADDR2 =(SERVER,5060)
tries(ADDR,FORMAT)



NAME = configuration(SERVER,PORT,NAME)

time.sleep(2)
os.system("cls")

connection(SERVER,PORT,NAME)


if i==1:

    pass

else:

    send(DISCONNECT_MESSAGE)

timer(3)
os.system("cls")

print(Fore.WHITE)


os.system("cls")





