import pygame as pg
from .shared import Attacker


class ScoutShip(Attacker, pg.sprite.Sprite):
    def __init__(self, game):
        Attacker.__init__(self, game, 1.2, 15, game.scoutship_img)
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    def get_title(self):
        return "Flee Ship"

class RedShip(Attacker, pg.sprite.Sprite):
    def __init__(self, game):
        Attacker.__init__(self, game, 0.8, 30, game.red_ship)
        pg.sprite.Sprite.__init__(self, self.groups)

    def get_title(self):
        return "Hull Ship"