import pygame as pg
from settings import *
from .shared import Defence, Projectile
from ..shared import Unit
from assets import Images
import random

class BeamTurret(Defence):
    price = 20
    src_img = Images.beam_turret_img

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*4,
                         max_range=TILE_SIZE*24,
                         fire_rate=120,
                         projectile=Beam)

        # Defence Center variables

    def upgrade_fire_rate(self):
        if self.fire_rate > 10 and self.game.defence_center.buy_option(20):
            self.fire_rate -= 5

    def get_title(self):
        return "Beam lvl:1"

    def get_options(self):
        return self._get_options() + [[[Images.blue_add_img, "Fire rate"], [self.upgrade_fire_rate]]]

    def update(self):
        self.defence_update()
        if self.target:
            self.rotation = (self.target.get_pos() - self.pos).angle_to(pg.Vector2(1, 0))
            self.image = pg.transform.rotate(self.src_img, self.rotation)



class SpitterTurret(Defence):
    price = 30
    src_img = Images.spitter_img

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*1,
                         max_range=TILE_SIZE*15,
                         fire_rate=7,
                         projectile=Ball)

        self.lvl = 1
        # Defence Center variables

    def upgrade_to(self, lvl):
        if lvl == 2:
            self.lvl = 2
            self.projectile_damage = 4
            self.fire_rate = 9

    def get_lvl_options(self):
        if self.lvl == 1:
            return [[[Images.blue_add_img, "Level 2"], [self.upgrade_to, 2]]]
        else:
            return list()

    def get_title(self):
        return "Spitter lvl:{}".format(self.lvl)

    def get_options(self):
        return self._get_options() + self.get_lvl_options()

    def update(self):
        self.defence_update()
        if self.target:
            self.rotation = (self.target.get_pos() - self.pos).angle_to(pg.Vector2(1, 0))
            self.image = pg.transform.rotate(self.src_img, self.rotation)


class MissileTurret(Defence):
    price = 35
    src_img = Images.missile_turret_img

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*7,
                         max_range=WIDTH,
                         fire_rate=250,
                         projectile=Missile)

        self.lvl = 1
        # Defence Center variables

    def upgrade_to(self, lvl):
        if lvl == 2:
            self.lvl = 2
            self.fire_rate = 200

    def get_lvl_options(self):
        if self.lvl == 1:
            return [[[Images.blue_add_img, "Level 2"], [self.upgrade_to, 2]]]
        else:
            return list()

    def get_title(self):
        return "Missile lvl:{}".format(self.lvl)

    def get_options(self):
        return self._get_options() + self.get_lvl_options()

    def update(self):
        self.defence_update()
        if self.target:
            self.rotation = (self.target.get_pos() - self.pos).angle_to(pg.Vector2(1, 0))
            self.image = pg.transform.rotate(self.src_img, self.rotation)



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

