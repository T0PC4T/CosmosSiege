import pygame as pg
from settings import *
from .buttons import ButtonBase

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
        self.menu_image = MenuPicture(self.game)
        self.defense_menu_button = ModeButton(self.game, DEFENCE_MODE_X, MODE_Y)
        self.defense_menu_button.set_action(lambda game: game.menu.set_defence_mode(), self.game)
        self.load_defence_menu()

    def set_defence_mode(self):
        self.mode = "defence"

    def load_defence_menu(self):
        self.defence_menu_items = [
            UnitDataButton(self.game, 0)
        ]
        self.defence_menu_items[0].set_action(self.game.defence_center.build, 1)

    def update(self):
        if self.mode == "defence":
            pass



class UnitData(pg.sprite.Sprite):
    def __init__(self, game, i, **kwargs):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        if kwargs.get("image"):
            self.image = kwargs.get("image")
        else:
            self.image = pg.Surface((DATA_RECORD_WIDTH, DATA_RECORD_HEIGHT))
            self.image.fill(BLUE)

        self.rect = self.image.get_rect()

        self.rect.x = DATA_LIST_X
        self.rect.y = DATA_LIST_Y + (i * DATA_RECORD_HEIGHT)

    def update(self):
        pass


class UnitDataButton(ButtonBase, UnitData):
    def __init__(self, game, i, **kwargs):
        UnitData.__init__(self, game, i, **kwargs)
        ButtonBase.__init__(self)


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
            self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.mouse_down: bool = False
        self.button_action: tuple = (lambda: None, [], {})


class MenuButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, game, i, **kwargs):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = pg.Surface((MODE_BUTTON_SIZE, MODE_BUTTON_SIZE))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y


class MenuPicture(pg.sprite.Sprite):
    def __init__(self, game):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = pg.Surface((MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = MENU_IMAGE_X
        self.rect.y = MENU_IMAGE_Y

