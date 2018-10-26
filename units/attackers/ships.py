import pygame as pg
from .shared import Attacker
from .shared import Unit
from assets import Images
from settings import *

class ScoutShip(Attacker, pg.sprite.Sprite):
    name = "Scout"
    src_img = Images.scout_ship_img
    price = 12
    income = 3
    speed = 1.3
    hp = 20
    hit_box_dim = TILE_SIZE // 4


class RedShip(Attacker):
    name = "R.E.D"
    src_img = Images.red_ship_img
    price = 15
    income = 15
    speed = 0.9
    hp = 35
    hit_box_dim = TILE_SIZE // 3


class FleeShip(Attacker):
    name = "Flee"
    src_img = Images.flee_ship_img
    price = 20
    income = 5
    speed = 1.2
    hp = 15
    hit_box_dim = TILE_SIZE // 6


class CargoShip(Attacker):
    name = "Cargo"
    src_img = Images.cargo_ship_img
    price = 50
    income = 25
    speed = 0.5
    hp = 50
    hit_box_dim = TILE_SIZE//2


class JetShip(Attacker):
    name = "Jet"
    src_img = Images.jet_ship_img
    price = 60
    income = 15
    speed = 1.9
    hp = 50
    hit_box_dim = TILE_SIZE // 3

class ScoutII(Attacker):
    name = "ScoutII"
    src_img = Images.scout_ship_img
    price = 150
    income = 75
    speed = 1.6
    hp = 150
    hit_box_dim = TILE_SIZE // 3

class CargoII(Attacker):
    name = "CargoII"
    src_img = Images.cargo_ship_img
    price = 200
    income = 180
    speed = 0.5
    hp = 300
    hit_box_dim = TILE_SIZE // 2

class Cruiser(Attacker):
    name = "Cruiser"
    src_img = Images.cruiser_img
    price = 250
    income = 175
    speed = 1.5
    hp = 250
    hit_box_dim = TILE_SIZE // 2

class Ghost(Attacker):
    name = "Ghost"
    src_img = Images.jet_ship_img
    price = 400
    income = 200
    speed = 1.5
    hp = 200
    hit_box_dim = TILE_SIZE // 2

class MotherShip(Attacker):
    name = "Mother"
    src_img = Images.cargo_ship_img
    price = 750
    income = 400
    speed = 0.5
    hp = 1000
    hit_box_dim = TILE_SIZE * 1.2
