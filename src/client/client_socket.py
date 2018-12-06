import socket
import logging
import datetime
from time import sleep


class ClientSocket(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        logging.basicConfig(filename='statusHouse.log', level=logging.DEBUG)

    def send_command(self, command):
        self.sock.sendall(command)
        data = self.sock.recv(1024)
        print('Received: ', repr(data))
    
    def check_status(self):
        while True:
            sleep(60)
            now = datetime.datetime.now()
            data = self.sock.recv(1024)
            if data:
                logging.info("{}/{}/{} - {}:{}:{} -> {}".format(
                    now.day, now.month, now.year, now.hour,
                    now.minute, now.second, repr(data)
                ))
