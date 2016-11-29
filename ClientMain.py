from Client import Client
import sys

client = Client('127.0.0.1', 8080)

while(1):
    msg = raw_input('Enter message to send : ')

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