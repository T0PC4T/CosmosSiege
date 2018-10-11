import pygame as pg
from settings import *

class InGameMenu(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((MENU_WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = ARENA_WIDTH
        self.rect.y = 0
        self.mode = "defence"
        self.load_menus()

    def load_menus(self):
        self.defense_menu_button = ModeButton(self.game, DEFENCE_MODE_X, MODE_Y)
        self.defense_menu_button.set_action(lambda game: game.menu.set_defence_mode(), self.game)
        self.load_defence_menu()

    def set_defence_mode(self):
        self.mode = "defence"

    def load_defence_menu(self):
        self.defence_menu_items = []

    def update(self):
        if self.mode == "defence":
            pass



class ButtonBase(object):

    def set_action(self, func, *args, **kwargs):
        self.button_action = (func, args, kwargs)

    def run_action(self):
        self.button_action[0](*self.button_action[1], **self.button_action[2])

    def is_mouse_over(self):
        mouse = pg.mouse.get_pos()
        if self.rect.x + self.rect.width > mouse[0] > self.rect.x - self.rect.width and self.rect.y + self.rect.height > mouse[1] > self.rect.y - self.rect.height:
            return True
        return False


class ModeButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, game, x, y, **kwargs):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        if kwargs.get("image"):
            self.image = kwargs.get("image")
        else:
            self.image = pg.Surface((MODE_BUTTON_SIZE, MODE_BUTTON_SIZE))
            self.image.fill(BLUE)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.mouse_down: bool = False
        self.button_action: tuple = (lambda: None, [], {})


    def update(self):
        if not self.mouse_down:
            if self.is_mouse_over():
                if pg.mouse.get_pressed()[0]:
                    self.mouse_down = True
        else:
            if not pg.mouse.get_pressed()[0]:
                self.mouse_down = False
                self.run_action()
