import pygame as pg
from .shared import Attacker

class ScoutShip(Attacker, pg.sprite.Sprite):
    def __init__(self, game):
        Attacker.__init__(self, game, 1.2, 15, game.scoutship_img)
        self.groups = game.all_sprites, game.attackers
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    # def update(self):
    #     self.attacker_update()


class RedShip(Attacker, pg.sprite.Sprite):
    def __init__(self, game):
        Attacker.__init__(self, game, 0.8, 30, game.red_ship)
        self.groups = game.all_sprites, game.attackers
        pg.sprite.Sprite.__init__(self, self.groups)

