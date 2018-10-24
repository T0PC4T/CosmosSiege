import pygame as pg
from settings import *
from .shared import Defence
from assets import Images
import random
from .projectiles import Missile, Ball, Beam

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


class ZapTurret(Defence):
    price = 40
    src_img = Images.zap_turret_img

    def __init__(self, game, pos):
        self.damage = 0.07

        Defence.__init__(self, game=game,
                         pos=pos,
                         min_range=TILE_SIZE*7,
                         max_range=WIDTH,
                         fire_rate=0,
                         projectile=None)

        self.lvl = 1
        # Defence Center variables

    def upgrade_to(self, lvl):
        if lvl == 2:
            self.lvl = 2
            self.damage = 0.15

    def get_lvl_options(self):
        if self.lvl == 1:
            return [[[Images.blue_add_img, "Level 2"], [self.upgrade_to, 2]]]
        else:
            return list()

    def get_title(self):
        return "Zap lvl:{}".format(self.lvl)

    def get_options(self):
        return self._get_options() + self.get_lvl_options()

    def defence_update(self):
        self.btn_update()

        if self.target:
            if not self.target.can_shoot:
                self.target = None
            else:
                d = (self.target.get_pos() - self.pos).length()
                if not self.vec_in_range(d):
                    self.target = None

        if not self.target:
            attackers = list(self.game.attackers)
            random.shuffle(attackers)
            for attacker in attackers:
                if not attacker.can_shoot:
                    continue
                d = (self.pos - attacker.get_pos()).length()
                if self.vec_in_range(d):
                    self.target = attacker
                    break

        if self.target and not self.next_shot:
            self.shoot()

    def shoot(self):
        self.rotation = (self.target.get_pos() - self.pos).angle_to(pg.Vector2(1, 0))
        self.image = pg.transform.rotate(self.src_img, self.rotation)
        pg.draw.line(self.game.screen, RED, self.target.get_pos(), self.get_pos())
        self.target.subtract_hp(self.damage)

    def update(self):
        self.defence_update()
