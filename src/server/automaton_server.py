import socket
import subprocess
import board_assets as assets
from threading import *

HOST = "10.99.9.26"
PORT = 65432

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
            if (int(data) % 2 == 0):
                assets.turn_all_on()
            else:
                assets.turn_all_off()    
            self.sock.sendall(b'Instruction received.')


while True:
    clientSocket, address = serverSocket.accept()
    Client(clientSocket, address)