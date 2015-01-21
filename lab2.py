# A Socket server using threads derived from http://www.binarytides.com/python-socket-server-code-example/
import socket
import sys
from thread import *
 
HOST = ''   
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
# Try to bind to specified host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Binding failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind completed'
s.listen(10)
print 'Socket now listening'
 
# Handles connections, create threads
def clientthread(conn):
    conn.send('Connected. Type something and hit enter\n') #send to connected client
     
    # Lasts forever to keep thread alive
    while 1: # = while True, while 1 is faster than while True
         
        #Receiving from client
        data = conn.recv(1024)
        reply = data + "Brian\n"
        if not data: 
            break
     
        conn.sendall(reply)
     
    conn.close()
 
# now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()