import socket
import subprocess
import board_assets as assets
from threading import *

HOST = "192.168.0.24"
PORT = 65430

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

assets.init_leds()

class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            data = self.sock.recv(1024).decode()
            if not data:
                break
            print("Instruction: {}".format(data))
            assets.decode_command(data)    
            self.sock.sendall(b'Instruction received.')


while True:
    clientSocket, address = serverSocket.accept()
    Client(clientSocket, address)