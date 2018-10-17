from interface.buttons import ButtonBase
import pygame as pg

class Unit(ButtonBase):
    def __init__(self, game):
        ButtonBase.__init__(self)
        self.game = game
        self.set_action(self.game.menu.set_focus, self)