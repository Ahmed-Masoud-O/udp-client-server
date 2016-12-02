import server
from Client import Client
from Packet import Packet
from Ack import Ack
import cPickle as pickle
import sys
from random import randrange
client = Client('127.0.0.1', randrange(3000,4000))
recievedSize = 0
expectedSeqNo = 0
lastSeqNo = 1


def toggleSeqNo():
    global expectedSeqNo
    if expectedSeqNo == 0:
        expectedSeqNo = 1
    else:
        expectedSeqNo = 0


def recieveFile():
    global recievedSize
    global expectedSeqNo
    global lastSeqNo
    totalSize, addr = client.clientSocket.recvfrom(1024)
    text_file = open("response.jpg", "w+")
    data_string = None
    while totalSize != str(recievedSize):
        msg = client.clientSocket.recvfrom(1024)
        serialized_data = msg[0]
        packet = pickle.loads(serialized_data)
        if packet.seqNo == lastSeqNo:
            client.clientSocket.sendto(data_string, addr)
            continue
        print(packet.data + str(packet.seqNo) + "\n")
        text_file.write(packet.data)
        ack = Ack(sys.getsizeof(expectedSeqNo), expectedSeqNo)
        data_string = pickle.dumps(ack, -1)
        client.clientSocket.sendto(data_string, addr)
        recievedSize += packet.length
        lastSeqNo = expectedSeqNo
        toggleSeqNo()
    text_file.close()
    client.clientSocket.close()
    sys.exit()


while 1:
    msg = raw_input('Enter file name to request : ')

    try:
        client.clientSocket.sendto(msg, ('127.0.0.1', 8888))

        # receive data from client (data, addr)
        reply, addr = client.clientSocket.recvfrom(1024)

        print 'Server reply : ' + reply

    except client.clientSocket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    recieveFile()
