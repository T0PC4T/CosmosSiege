import pygame as pg
from settings import *
from .shared import Defence, Projectile
from assets import ArrowImg


class ArrowTower(Defence, pg.sprite.Sprite):
    def __init__(self, game, pos):
        Defence.__init__(self, game, game.arrow_tower_img, pos, TILE_SIZE*4, TILE_SIZE*24, FPS*2, Arrow)
        self.groups = game.all_sprites, game.defences
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    def update(self):
        self.defence_update()


class Arrow(Projectile, pg.sprite.Sprite):
    def __init__(self, game, pos, target):
        Projectile.__init__(self, game, game.arrow_img, pos, target, 5, FPS*6, 5)
        self.groups = game.all_sprites, game.projectiles
        pg.sprite.Sprite.__init__(self, self.groups)

