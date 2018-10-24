import pygame as pg
from settings import *
from .shared import Projectile
from assets import Images
import random

class Beam(Projectile):
    _image = pg.Surface((TILE_SIZE // 4, TILE_SIZE // 4))
    _image.fill(BLACK)
    pg.draw.rect(_image, RED, (0, TILE_SIZE // 8, TILE_SIZE, TILE_SIZE - TILE_SIZE // 8))
    _image.set_colorkey(BLACK)
    src_img = _image

    speed = 7
    duration = 300
    damage = 10

    def __init__(self, game, turret, target):
        Projectile.__init__(self, game, turret, target)


class Ball(Projectile):
    inaccuracy = 15
    speed = 4
    duration = 120
    damage = 2

    _image = pg.Surface((TILE_SIZE // 4, TILE_SIZE // 4))
    _image.fill(BLACK)
    pg.draw.circle(_image, GREEN, (TILE_SIZE // 8, TILE_SIZE // 8), TILE_SIZE // 8)
    _image.set_colorkey(BLACK)
    src_img = _image


    def __init__(self, game, turret, target):
        if self.turret.lvl == 2:
            self.damage = 4

        Projectile.__init__(self, game, turret, target)
        self.velocity = self.velocity.rotate((random.randint(0, self.inaccuracy) - random.randint(0, self.inaccuracy)))


class Missile(Projectile):
    src_img = Images.missile_img
    speed = 4
    duration = 400
    damage = 30

    def __init__(self, game, turret, target):
        Projectile.__init__(self, game, turret, target, "homing")
