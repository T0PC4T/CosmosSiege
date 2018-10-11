import pygame as pg
from settings import *


class DefenceCenter(pg.sprite.Sprite):
    def __init__(self, game, tile_x, tile_y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = pg.Surface((TILE_SIZE*2, TILE_SIZE*2))

        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = tile_x * TILE_SIZE
        self.rect.y = tile_y * TILE_SIZE

    def update(self):
        pass

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
