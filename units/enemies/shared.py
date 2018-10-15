from settings import *
import pygame as pg
vec = pg.math.Vector2

class Attacker():
    def __init__(self, game, speed):
        self.image = None
        self.rect = None
        self.game = game
        self.speed = speed
        self.pos = vec(self.game.attack_center.rect.x, self.game.attack_center.rect.y)
        self.path = self.game.attack_center.get_path()
        self.moving_pos_index = 0
        self.moving = False
        self.rotation = 0
        self.vel = vec(0, 0)

    @staticmethod
    def get_type():
        return "attackers"

    def affects_update(self):
        pass

    def attacker_update(self):
        if not self.moving:
            self.moving = True
            if self.moving_pos_index == len(self.path):
                self.game.defence_center.subtract_life()
                self.kill()
            else:
                self.target = vec(self.path[self.moving_pos_index])*TILE_SIZE
                self.rotation = (self.target - self.pos).angle_to(vec(1, 0))
                self.image = pg.transform.rotate(self.game.hood_warrior_image, self.rotation)
        else:
            self.vel = vec(self.speed, 0).rotate(-self.rotation)
            self.pos = self.pos + self.vel

            if (self.pos - self.target).length() <= self.speed:
                self.rect.topleft = self.target
                self.moving = False
                self.moving_pos_index+=1
            else:
                self.rect.topleft = self.pos






