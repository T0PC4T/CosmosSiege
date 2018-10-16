import pygame as pg
from settings import *
from random import randint
from .shared import Attacker

class HoodWarrior(Attacker, pg.sprite.Sprite):
    def __init__(self, game):
        Attacker.__init__(self, game, 1, 15, game.hood_warrior_img)
        self.groups = game.all_sprites, game.attackers
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    # def update(self):
    #     self.attacker_update()
