import pygame as pg
from settings import *
from random import randint
from .shared import Attacker

class HoodWarrior(pg.sprite.Sprite, Attacker):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites, game.attackers
        Attacker.__init__(self, game, 1, 15, game.hood_warrior_img)
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    def update(self):
        self.attacker_update()
