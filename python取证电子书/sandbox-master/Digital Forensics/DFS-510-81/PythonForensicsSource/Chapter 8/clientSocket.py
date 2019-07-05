import socket

MAX_BUFFER = 1024
# Create a Socket

myClientSocket = socket.socket()

# Get my local host address

localHost = socket.gethostname()

# Specify a local Port to attempt a connection

localPort = 5555

# Attempt a connection to my localHost and localPort

myClientSocket.connect((localHost, localPort))

# If connection is successful, wait for a reply

msg = myClientSocket.recv(MAX_BUFFER)
print msg

myClientSocket.close()




