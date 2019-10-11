import socket
from termcolor import colored

hold = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("Enter host IP address to scan: ")

def portscanner(port):
    if(hold.connect_ex((host,port))):
        print(colored("Port %d is closed!" % (port),'red'))
    else:
        print(colored("Port %d is open!" % (port),'green'))

for port in range(1,1001):
    portscanner(port)