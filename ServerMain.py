from Server import Server
from Packet import Packet
import sys
import cPickle as pickle

server = Server('127.0.0.1', '8888')
totalSize = 0

def toggleSeqNo(seqNo):
    if seqNo == 0:
        seqNo = 1
    else:
        seqNo = 0
    return seqNo

def createPackets(chunk,seqNo):
    global totalSize
    size = sys.getsizeof(chunk) + sys.getsizeof(seqNo)
    packet = Packet(size, seqNo, chunk)
    toggleSeqNo(seqNo)
    totalSize += size
    return packet

def openAndChunkFile(fileName):
    chunks = []
    try:
        f = open(fileName, 'r')
    except:
        # server.serverSocket.send("404 Not Found")
        server.serverSocket.close()
        return
    while True:
        data = f.readline(512)
        if not data:
            break
        chunks.append(data)
    return chunks


def waitForAck(seqNo):
    msg = server.serverSocket.recvfrom(1024)
    serialized_data = msg[0]
    Ack = pickle.loads(serialized_data)
    if Ack.ackNumber == seqNo:
        return 0
    else:
        return 1


def handleRequest(fileName):
    global totalSize
    totalSize = 0
    dataChunks = openAndChunkFile(fileName)
    finalPackets = []
    seqNo = 0
    for chunk in dataChunks:
        finalPackets.append(createPackets(chunk, seqNo))
        toggleSeqNo(seqNo)
    server.serverSocket.sendto(str(totalSize), addr)
    for packet in finalPackets:
        data_string = pickle.dumps(packet, -1)
        server.serverSocket.sendto(data_string, addr)
        ackResponse = waitForAck(packet.seqNo)
        while ackResponse:
            print "waiting for Ack\n"
            ackResponse = waitForAck(packet.seqNo)
        print "Ack Recieved"


while 1:
    msg = server.serverSocket.recvfrom(1024)
    fileName = msg[0]
    addr = msg[1]

    if not fileName:
        break

    reply = 'OK...' + fileName

    server.serverSocket.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + fileName.strip()
    handleRequest(fileName)


