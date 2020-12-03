import threading
import socket
import sys
import time

class ServerThread :
    data = ""
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    
    def startServer(self):
        
        # Bind the socket to the port
        server_address = ('localhost', 4538)
        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)
        # Listen for incoming connections
        self.sock.listen(3)
        # Wait for a connection
        print('waiting for a connection')
        while True:
            #connection, client_address = self.sock.accept()
            serverThread = threading.Thread(target=self.receiveData,args=self.sock.accept())
            serverThread.start()

    def receiveData(self,connection,client_address):
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            while True:
            
                temp = (connection.recv(32)).decode("utf-8")
                if(temp!=""):
                    ServerThread.data = temp.lower()
        except:
            pass







