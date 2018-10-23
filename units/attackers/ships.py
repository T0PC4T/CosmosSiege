import pygame as pg
from .shared import Attacker
from .shared import Unit
from assets import Images

class ScoutShip(Attacker, pg.sprite.Sprite):
    name = "Scout"
    src_img = Images.scoutship_img
    price = 10
    income = 3
    speed = 1.3
    hp = 15


class RedShip(Attacker):
    name = "R.E.D"
    src_img = Images.red_ship_img
    price = 15
    income = 7
    speed = 0.8
    hp = 30



class FleeShip(Attacker):
    name = "Flee"
    src_img = Images.flee_ship_img
    price = 20
    income = 5
    speed = 1.2
    hp = 10



class CargoShip(Attacker):
    name = "Cargo"
    src_img = Images.cargo_ship_img
    price = 50
    income = 22
    speed = 0.5
    hp = 50
