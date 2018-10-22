from game import Game
from pregame import PreGame
import pygame as pg
from settings import *
import socket

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
pg.font.init()
clock = pg.time.Clock()

connected = False
while not connected:
    p = PreGame(screen, clock)
    ipaddress_port = p.run()

    try:
        ipaddr, port = ipaddress_port.split(":")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipaddr, int(port)))
        s.sendall(b'1')
        data = s.recv(1024)
        print(data)
        print(data.decode("utf-8"))

        s.close()

        connected = True
    except Exception as e:
        print(e)



g = Game(screen, clock)
g.run()
