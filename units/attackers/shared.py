from settings import *
import pygame as pg
vec = pg.math.Vector2

class Attacker():
    def __init__(self, game, speed, health, src_img, destroy_lives=1):
        self.game = game
        self.src_img = src_img
        self.image = src_img
        self.rect = self.image.get_rect()
        self.rect.x = self.game.attack_center.rect.x
        self.rect.y = self.game.attack_center.rect.y
        self.hit_rect = pg.Rect(self.rect.x, self.rect.y, TILE_SIZE // 2, TILE_SIZE // 2)

        self.speed = speed
        self.health = health
        self.destroy_lives = destroy_lives
        self.pos = vec(self.game.attack_center.rect.x, self.game.attack_center.rect.y)
        self.path = self.game.attack_center.get_path()
        self.moving_pos_index = 0
        self.moving = False
        self.rotation = 0
        self.velocity = vec(0, 0)
        self.can_shoot = True
        # Affects

        self.affects = list()
        self.duration = 0

    @staticmethod
    def get_type():
        return "attackers"

    def get_velocity(self):
        return vec(self.velocity)

    def get_pos(self):
        return self.pos

    def subtract_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
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

    def attacker_update(self):

        if not self.moving:
            self.moving = True
            if self.moving_pos_index == len(self.path):
                self.game.defence_center.subtract_life(self.destroy_lives)
                self.die()
            else:
                self.target = vec(self.path[self.moving_pos_index])*TILE_SIZE
                self.rotation = (self.target - self.pos).angle_to(vec(1, 0))
                self.image = pg.transform.rotate(self.src_img, self.rotation)
        else:
            self.velocity = vec(self.speed, 0).rotate(-self.rotation)
            self.pos = self.pos + self.velocity

            if (self.pos - self.target).length() <= self.speed:
                self.rect.topleft = self.target
                self.moving = False
                self.moving_pos_index+=1
            else:
                self.rect.topleft = self.pos

        self.hit_rect.topleft = self.rect.topleft





