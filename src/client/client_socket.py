import socket

HOST = '10.9.99.26'  # Standard loopback interface address (localhost)
PORT = 65430           # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send_command(command):
    s.sendall(command)
