import pygame as pg
from .shared import Attacker
from .shared import Unit


class ScoutShip(Attacker, pg.sprite.Sprite):
    name = "Scout"
    price = 10
    income = 2
    speed = 1.3
    hp = 15

    def __init__(self, game):
        Attacker.__init__(self, game, game.scoutship_img)

        # Defence Center variables


class RedShip(Attacker):
    name = "R.E.D"
    price = 15
    income = 3
    speed = 0.8
    hp = 30

    def __init__(self, game):
        Attacker.__init__(self, game, game.red_ship_img)


class FleeShip(Attacker):
    name = "Flee"
    price = 20
    income = 2
    speed = 1.2
    hp = 10

    def __init__(self, game):
        Attacker.__init__(self, game, game.flee_ship_img)


class CargoShip(Attacker):
    name = "Cargo"
    price = 25
    income = 10
    speed = 0.5
    hp = 50

    def __init__(self, game):
        Attacker.__init__(self, game, game.flee_ship_img)
