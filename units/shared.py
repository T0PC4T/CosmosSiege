from interface.buttons import ButtonBase
import pygame as pg
from settings import *

src_img = pg.Surface((TILE_SIZE, TILE_SIZE))
src_img.fill(WHITE)

class Unit(ButtonBase):
    def __init__(self, game):
        ButtonBase.__init__(self)
        self.game = game
        self.set_action(self.game.menu.set_focus, self)


    def get_options(self):
        return list()

    def get_img(self):
        return getattr(self, "src_img", src_img)

    def get_title(self):
        return "N/A"

    def get_info(self):
        return {"N/A": "N/A"}