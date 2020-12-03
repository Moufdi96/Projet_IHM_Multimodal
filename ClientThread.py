import threading
import socket
import sys
import time

class ClientThread :
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectToServer()
        pass
    def connectToServer(self):
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 4538)
        print('connecting to {} port {}'.format(*server_address))
        self.sock.connect(server_address)

    def send(self,data):
        try:
        # Send data
            message = ''
            if(len(message)>=0):
                #message = input("enter the name\n")
                message = data.lower()
                print('sending {!r}'.format(message))
                self.sock.sendall(message.encode())
        except:
            pass
