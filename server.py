import socket
import sys


class Server:
    host = None
    server = None
    threadsArray = []
    serverSocket = None

    def initializeServerSocket(self):
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.serverSocket.settimeout(1)
            print 'Socket created'
        except socket.error, msg:
            print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

    def bindSocket(self):
        try:
            self.serverSocket.bind((self.host, self.port))
        except socket.error, msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        print 'Socket bind complete'

    def __init__(self, host, port):
        self.threadsArray = []
        self.host = host
        self.port = int(port)
        self.initializeServerSocket()
        self.bindSocket()
