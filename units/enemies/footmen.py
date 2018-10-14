import pygame as pg
from settings import *
from random import randint


class HoodWarrior(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.hood_warrior_image
        self.rect = self.image.get_rect()
        self.rect.x = self.game.attack_center.rect.x
        self.rect.y = self.game.attack_center.rect.y

        # Defence Center variables

    def update(self):
        self.rect.x += 1