from queue import Queue, Empty
import json

class ClientConnection(object):
    def __init__(self, game, server_connection):
        self.game = game
        self.server_connection = server_connection
        self.data_queue = list()

    def send_units(self, attacker_list):
        atts = list()
        for a in attacker_list:
            atts.append(a.__name__)

        self.data_queue.append(bytes(json.dumps(atts), "utf-8"))

    def update(self):
        if len(self.data_queue) > 0:
            next_msg = self.data_queue.pop(0)
        else:
            next_msg = b"0000"

        self.server_connection.sendall(next_msg)
