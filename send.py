import socket
import sys

host = sys.argv[1]  # as both code is running on same pc
port = int(sys.argv[2])  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = raw_input("")  # take input
file = open("chats.txt","a")
file.write("<<--"+message+"\n")
file.close()


client_socket.send(message.encode())  # send message


client_socket.close()  # close the connection
