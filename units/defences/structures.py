import pygame as pg
from settings import *
from .shared import Defence, Projectile, Structure
from ..shared import Unit


class Barricade(Structure):
    price = 5
    def __init__(self, game, pos):
        Structure.__init__(self, game, game.barracade_img, pos)
        self.groups = game.all_sprites, game.defences
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    def get_title(self):
        return "Barricade"

    def get_options(self):
        return self._get_options()

    def update(self):
        self.defence_update()

