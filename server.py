import select, socket, sys
from queue import Queue, Empty

class ServerSocket(object):
    def __init__(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.bind(('0.0.0.0', 50000))
        self.server.listen(5)
        self.inputs = [self.server]
        self.outputs = []

        self.player_connections = dict()
        self.players_ready = 0

        self.game_stage = 0

    def run_pregame_server(self):
        while self.inputs:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, list())
            print(writable)
            for s in readable:
                if s is self.server:
                    connection, client_address = s.accept()
                    connection.setblocking(False)
                    self.inputs.append(connection)
                    print("CONNECTION RECEIVED !")
                    self.player_connections[connection] = Queue()
                    self.outputs.append(connection)
                else:
                    data = s.recv(1024)
                    if data == b'echo':
                        self.player_connections[s].put(b'echo')
                    elif data == b"ready":
                        self.players_ready +=1
                    else:
                        pass

            for s in writable:
                try:
                    next_msg = self.player_connections[s].get_nowait()
                except Empty:
                    s.sendall(b"0000")
                else:
                    s.sendall(next_msg)


            for s in exceptional:
                pass

            if len(self.player_connections.keys()) > 1:
                if self.players_ready == len(self.player_connections.keys()):
                    for key in self.player_connections.keys():
                        self.player_connections[key].put(b"all ready")
                    self.game_stage = 1

    def clear_queues(self):
        for p, q in enumerate(self.player_connections):
            q.clear()

    def run_game_server(self):
        while self.inputs:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)

            for s in readable:
                if s is not server:
                    data = s.recv(1024)
                    print(data)

            for s in writable:
                try:
                    next_msg = self.player_connections[s].get_nowait()
                except Empty:
                    next_msg = b"0000"
                else:
                    s.send(next_msg)

            for s in exceptional:
                self.inputs.remove(s)
                if s in self.outputs:
                    self.outputs.remove(s)
                s.close()
                del self.player_connections[s]


server = ServerSocket()
server.run_pregame_server()
server.run_game_server()