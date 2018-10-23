import pygame as pg
from .shared import Attacker
from .shared import Unit
from assets import Images

class ScoutShip(Attacker, pg.sprite.Sprite):
    name = "Scout"
    src_img = Images.scoutship_img
    price = 10
    income = 2
    speed = 1.3
    hp = 15
    #
    # def __init__(self, game):
    #     Attacker.__init__(self, game)

        # Defence Center variables


class RedShip(Attacker):
    name = "R.E.D"
    src_img = Images.red_ship_img
    price = 15
    income = 3
    speed = 0.8
    hp = 30



class FleeShip(Attacker):
    name = "Flee"
    src_img = Images.flee_ship_img
    price = 20
    income = 2
    speed = 1.2
    hp = 10



class CargoShip(Attacker):
    name = "Cargo"
    src_img = Images.flee_ship_img
    price = 25
    income = 10
    speed = 0.5
    hp = 50
