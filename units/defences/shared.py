from settings import *
import pygame as pg
vec = pg.math.Vector2

class Defence():

    def __init__(self, game, pos, min_range, max_range):
        self.game = game
        self.pos = vec(pos)
        self.min_range = min_range
        self.max_range = max_range
        self.target = None

    @staticmethod
    def get_type():
        return "defence"

    def vec_in_range(self, d):
        return d > self.min_range and d < self.min_range

    def defence_update(self):
        if self.target:
            d = (self.pos - self.target.get_pos()).lengh()
            if not self.vec_in_range(d):
                self.target = None

        if not self.target:
            for attacker in self.game.attackers:
                d = (self.pos - attacker.get_pos()).lengh()
                if self.vec_in_range(d):
                    self.target = attacker
                    break

        if self.target:
            pass




    def update(self):
        self.defence_update()