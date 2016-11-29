from Server import Server

server = Server('127.0.0.1', '8080')


def openAndChunkFile(fileName):
    chunks = []
    try:
        f = open(fileName, 'r')
    except:
        # server.serverSocket.send("404 Not Found")
        server.serverSocke.close()
        return
    while True:
        data = f.readline(512)
        if not data:
            break
        chunks.append(data)
    return chunks


while 1:
    msg = server.serverSocket.recvfrom(1024)
    fileName = msg[0]
    addr = msg[1]

    if not fileName:
        break

    reply = 'OK...' + fileName

    server.serverSocket.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + fileName.strip()

server.serverSocket.close()
