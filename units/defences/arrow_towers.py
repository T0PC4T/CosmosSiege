import pygame as pg
from settings import *


class ArrowTower(pg.sprite.Sprite):
    def __init__(self, game, tile_x, tile_y):
        self.groups = game.all_sprites, game.defences
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.arrow_tower_image
        self.rect = self.image.get_rect()
        self.rect.x = tile_x * TILE_SIZE
        self.rect.y = tile_y * TILE_SIZE

        # Defence Center variables

    def update(self):
        pass