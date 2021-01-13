import socket
import threading
import pyfiglet as py
import os
from colorama import init
init()
from colorama import Fore, Back, Style
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
myprotocol = socket.AF_INET

myFamilyNetworkName = socket.SOCK_DGRAM

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

ip = "192.168.43.5"
port = 1234

ip2 = input("Enter IP of OS whom you want to chat")
port2 = 1235

os.system("cls")
print("CHAT PROGRAM")
print("-------------")
print(Fore.GREEN)
def sendToAll1():
   
    while True:
        
        x = input("")
        print(Fore.GREEN)
        s.sendto("{}".format(x).encode(), (ip2, port2))
        

def sendToAll2():
    while True:
        x = input("")
        print(Fore.GREEN)
        s.sendto("{}".format(x).encode(), (ip2, port2))
       
def recieve1():
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    s.bind(( ip, port ))
    while True:
        x = s.recvfrom(1024)
        msg = "Message from {} : {}".format(x[1][0],x[0].decode())
        print("\t\t\t\t\t\t\t\t\t\t\t\t",end=' ' )
        print(Fore.YELLOW,msg)
        print(Fore.GREEN)

recieving1 = threading.Thread( target = recieve1 )
sendChat1 = threading.Thread( target = sendToAll1 )
  
sendChat1.start()
recieving1.start()
