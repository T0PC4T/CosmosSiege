from settings import *
import pygame as pg
vec = pg.math.Vector2
from ..shared import Unit
import math


class Attacker(Unit, pg.sprite.Sprite):
    def __init__(self, game, destroy_lives=1):
        Unit.__init__(self, game)
        self.groups = game.all_sprites, game.attackers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = self.src_img
        self.rect = self.image.get_rect()
        self.rect.x = self.game.attack_center.rect.x
        self.rect.y = self.game.attack_center.rect.y
        self.hit_rect = pg.Rect(self.rect.centerx, self.rect.centery, self.hit_box_dim, self.hit_box_dim)

        self.original_speed = self.speed
        self.speed = self.speed
        self.max_hp = self.hp
        self.hp = self.hp

        self.destroy_lives = destroy_lives
        self.pos = vec(self.game.attack_center.rect.x, self.game.attack_center.rect.y)
        self.path = self.game.attack_center.get_path()
        self.moving_pos_index = 0
        self.moving = False
        self.rotation = 0
        self.target_rot = 0
        self.velocity = vec(0, 0)
        self.can_shoot = True
        # Affects

        self.affects = list()
        self.duration = 0

    @staticmethod
    def get_type():
        return "attackers"

    def get_info(self):
        return {"HP": "{}/{}".format(int(self.hp), self.max_hp),
                "SPEED": self.speed*10}

    def get_speed(self):
        return self.speed

    def get_velocity(self):
        return vec(self.velocity)

    def get_title(self):
        return "{} {}({})".format(self.name, self.price, self.income)

    def subtract_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        if self.hp <= 0:
            self.game.defence_center.add_credits(self.get_income())

        self.game.attack_center.attackers.i_died(self)
        self.can_shoot = False
        self.kill()

    def remove_affect(self, affect):
        pass

    def set_affect(self, affect, duration):
        if affect not in self.affects:
            self.affects.append(affect)
        self.duration = duration

        if affect == "frozen":
            pass

    def affects_update(self):
        pass

    def get_gradual_rotation(self):
        b = self.target_rot - self.rotation
        if b*b < 25:
            self.rotation = self.target_rot
        else:
            if self.target_rot > self.rotation:
                self.rotation += 5
            else:
                self.rotation -= 5

        return self.rotation

    def attacker_update(self):
        self.btn_update()
        self.image = pg.transform.rotate(self.src_img, self.get_gradual_rotation())
        if not self.moving:
            self.moving = True
            if self.moving_pos_index == len(self.path):
                self.game.defence_center.subtract_life(self.destroy_lives)
                self.die()
            else:
                self.target = vec(self.path[self.moving_pos_index])*TILE_SIZE
                self.target_rot = (self.target - self.pos).angle_to(vec(1, 0))
        else:
            self.velocity = vec(self.speed, 0).rotate(-self.target_rot)
            self.pos = self.pos + self.velocity

            if (self.pos - self.target).length() <= self.speed:
                self.rect.topleft = self.target
                self.moving = False
                self.moving_pos_index+=1
            else:
                self.rect.topleft = self.pos

        self.hit_rect.center = self.rect.center

    def update(self):
        self.attacker_update()




