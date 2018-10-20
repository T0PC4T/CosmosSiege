import pygame as pg
from .shared import Attacker
from .shared import Unit


class ScoutShip(Attacker, pg.sprite.Sprite):
    price = 10
    income = 2
    name = "Scout"

    def __init__(self, game):
        Attacker.__init__(self, game, 1.2, 15, game.scoutship_img)
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables



class RedShip(Attacker, pg.sprite.Sprite):
    price = 15
    income = 3
    name = "R.E.D"

    def __init__(self, game):
        Attacker.__init__(self, game, 0.8, 30, game.red_ship_img)
        pg.sprite.Sprite.__init__(self, self.groups)
