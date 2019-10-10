import socket
import sys

port = int(sys.argv[1])  # initiate port no above 1024
server_socket = socket.socket() 
server_socket.bind(('', port))
file = open("chats.txt","w")
file.close()
while True:
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    data = conn.recv(1024).decode()
    data="-->> "+data+"\n"
    file = open('chats.txt','a') 
    file.write(data) 
    file.close() 
    conn.close()  # close the connection

