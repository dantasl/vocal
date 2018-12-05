import socket

HOST = '192.168.0.24'  # Standard loopback interface address (localhost)
PORT = 65431           # Port to listen on (non-privileged ports are > 1023)

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command)
        data = s.recv(1024)
        print('Received: ', repr(data))
