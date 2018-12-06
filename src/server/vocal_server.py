import socket
import threading
import board_assets as assets
from time import sleep

HOST = "192.168.0.24"
PORT = 6001


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60) uncomment to kill client after a while
            threading.Thread(target = self.listenToClient, args = (client,address)).start()
            threading.Thread(target = self.sendStatusToClient, args = (client, address)).start()

    def sendStatusToClient(self, client, address):
        while True:
            sleep(60) # Put this any value
            try:
                print("Sending status: {}".format(assets.compose_status()))
                client.send(assets.compose_status().encode())
            except:
                client.close()
                return False    

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    print("Instruction: {}".format(data))
                    if assets.decode_command(data): 
                        client.send(b'COMMAND PERFORMED.')
                    else:
                        client.send(b'ERROR WHILE PERFORMING COMMAND.')
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False


if __name__ == "__main__":
    assets.init_leds()
    ThreadedServer(HOST, PORT).listen()
