import pygame as pg
from settings import *
from .shared import Defence, Projectile
from ..shared import Unit
from assets import Images
import random

class BasicTurret(Defence):
    price = 20
    src_img = Images.basic_turret_img

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*4,
                         max_range=TILE_SIZE*24,
                         fire_rate=int(FPS*2.5),
                         projectile=Beam,
                         projectile_speed=5,
                         projectile_duration=FPS*7,
                         projectile_damage=10)

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


class Beam(Projectile, pg.sprite.Sprite):
    def __init__(self, game, pos, target, speed, duration, damage):
        image = pg.Surface((TILE_SIZE//4, TILE_SIZE//4))
        image.fill(BLACK)
        pg.draw.rect(image, RED, (0, TILE_SIZE//8, TILE_SIZE, TILE_SIZE-TILE_SIZE//8))
        image.set_colorkey(BLACK)
        Projectile.__init__(self, game, image, pos, target, speed, duration, damage)
        self.groups = game.all_sprites, game.projectiles
        pg.sprite.Sprite.__init__(self, self.groups)


class SpitterTurret(Defence):
    price = 30
    src_img = Images.spitter_img

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*1,
                         max_range=TILE_SIZE*15,
                         fire_rate=10,
                         projectile=Ball,
                         projectile_speed=4,
                         projectile_duration=FPS*4,
                         projectile_damage=1)

        self.lvl = 1
        # Defence Center variables

    def upgrade_to(self, lvl):
        if lvl == 2:
            self.lvl = 2
            self.projectile_damage = 2

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


class Ball(Projectile):
    inaccuracy = TILE_SIZE
    def __init__(self, game, pos, target, speed, duration, damage):
        image = pg.Surface((TILE_SIZE//4, TILE_SIZE//4))
        image.fill(BLACK)
        pg.draw.circle(image, GREEN, (TILE_SIZE//8, TILE_SIZE//8), TILE_SIZE//8)
        image.set_colorkey(BLACK)
        Projectile.__init__(self, game, image, pos, target, speed, duration, damage)
        self.velocity = self.velocity.rotate((random.randint(0, self.inaccuracy) - random.randint(0, self.inaccuracy)))
        # self.velocity.rotation += (random.randint(0, self.inaccuracy) - random.randint(0, self.inaccuracy))



