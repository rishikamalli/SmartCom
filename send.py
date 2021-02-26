#this is to connect to the Android app

#socket represents a endpoint in the communication channel

import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) #used to accept incoming connections must be attached to operating system resources.
#it takes the port number from the bluetoot device to establish the connection

port = 1 #usually there is only one bluetooth adapter

server_sock.bind(("",port)) #empty string indicates any local bluetooth adapter can be used

server_sock.listen(1) #call to listen puts the socket into listening mode and ready to accept incoming connections

print "waiting for connection"

client_sock,address = server_sock.accept()#Server accepts connection request from a client

#client_socket is the socket used for communication with client and address the client's address.

print "Accepted connection from ",address


