import socket
import threading
import os

myprotocol = socket.AF_INET

myFamilyNetworkName = socket.SOCK_DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )

ip = "192.168.43.224"
port = 1235

ip1 = input("Enter the OS whom you want to chat ")
os.system("tput setaf 6")
port2 = 1234


os.system("clear")
print("CHAT PROGRAM")
print("-------------")
os.system("tput setaf 3")
def sendToAll1():
    while True:
        x = input("")
        s.sendto("{}".format(x).encode(), (ip1, port2))
def sendToAll2():
   
    while True:
       
        x = input("")
     
        s.sendto("{}".format(x).encode(), (ip1, port2))

def recieve1():
  
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

    s.bind(( ip, port ))
    while True:
        
        x = s.recvfrom(1024)
        msg = "Message from {} : {}".format(x[1][0],x[0].decode())
      
        os.system("tput setaf 2")
        print("\t\t\t\t",end='')
        print(msg)
        os.system("tput setaf 3")

recieving1 = threading.Thread( target = recieve1 )

sendChat1 = threading.Thread( target = sendToAll1 )
sendChat2 = threading.Thread( target = sendToAll2 )


sendChat1.start()
sendChat2.start()
recieving1.start()
