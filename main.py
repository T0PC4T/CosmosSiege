from game import Game
from pregame import PreGame
import pygame as pg
from settings import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
pg.font.init()
clock = pg.time.Clock()

# p = PreGame(screen, clock)
# s = p.run()

g = Game(screen, clock, None)
g.run()
