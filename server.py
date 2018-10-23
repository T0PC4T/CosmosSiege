import select, socket, sys
from queue import Queue, Empty
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 50000))
server.listen(5)
inputs = [server]
outputs = []

player_connections = dict()
players_ready = 0


while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, list())
    print(writable)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(False)
            inputs.append(connection)
            print("CONNECTION RECEIVED !")
            player_connections[connection] = Queue()
            outputs.append(connection)
        else:
            data = s.recv(1024)
            if data == b'echo':
                player_connections[s].put(b'echo')
            elif data == b"ready":
                players_ready +=1
            else:
                pass

    for s in writable:
        try:
            next_msg = player_connections[s].get_nowait()
        except Empty:
            s.sendall(b"0000")
        else:
            s.sendall(next_msg)


    for s in exceptional:
        pass

    if len(player_connections.keys()) > 1:
        if players_ready == len(player_connections.keys()):
            for key in player_connections.keys():
                player_connections[key].put(b"all ready")
