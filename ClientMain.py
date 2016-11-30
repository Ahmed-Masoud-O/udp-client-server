from Client import Client
from Packet import Packet
from Ack import Ack
import cPickle as pickle
import sys

client = Client('127.0.0.1', 8888)
recievedSize = 0

def recieveFile():
    global recievedSize
    msg = client.clientSocket.recvfrom(1024)
    totalSize = msg[0]
    text_file = open("response.jpg", "w+")
    seqNo = 0
    while totalSize != str(recievedSize):
        msg = client.clientSocket.recvfrom(1024)
        if not msg:
            return
        serialized_data = msg[0]
        packet = pickle.loads(serialized_data)
        print(packet.data)
        text_file.write(packet.data)
        ack = Ack(sys.getsizeof(seqNo), 0)
        data_string = pickle.dumps(ack, -1)
        client.clientSocket.sendto(data_string, (client.host, client.port))
        recievedSize += packet.length
    text_file.close()
    client.clientSocket.close()
    sys.exit()

while 1:
    msg = raw_input('Enter file name to request : ')

    try:
        client.clientSocket.sendto(msg, (client.host, client.port))

        # receive data from client (data, addr)
        msg = client.clientSocket.recvfrom(1024)
        reply = msg[0]
        addr = msg[1]

        print 'Server reply : ' + reply

    except client.clientSocket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    recieveFile()
