from Server import Server

server = Server('127.0.0.1', '8080')
while 1:
    msg = server.serverSocket.recvfrom(1024)
    data = msg[0]
    addr = msg[1]

    if not data:
        break

    reply = 'OK...' + data

    server.serverSocket.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

server.serverSocket.close()
