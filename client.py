import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
for i in range(1):
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print(data)

s.close()
