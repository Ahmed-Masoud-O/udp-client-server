import socket
import sys

class Client:
    host = None
    server = None
    clientSocket = None

    def initializeClientSocket(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()

    def __init__(self, host, port):
        self.threadsArray = []
        self.host = host
        self.port = int(port)
        self.initializeClientSocket()
