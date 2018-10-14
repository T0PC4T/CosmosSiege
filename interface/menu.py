import pygame as pg
from settings import *
from .buttons import ButtonBase
from units import *

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
        self.page = 0

    def load_menus(self):
        self.menu_info = MenuUnitInfo(self.game)

        ################################################################################################################

        self.defense_menu_button = ModeButton(self.game, DEFENCE_MODE_X, MODE_Y, self.game.defence_mode_btn_image)
        self.defense_menu_button.set_action(lambda: self.set_defence_mode())

        self.attack_menu_button = ModeButton(self.game, ATTACK_MODE_X, MODE_Y, self.game.attack_mode_btn_image)
        self.attack_menu_button.set_action(lambda: self.set_attack_mode())

        ################################################################################################################

        self.unit_btns = list()

        for i in range(6):
            self.unit_btns.append(UnitButton(self.game, i))

        self.set_defence_mode()

        ################################################################################################################

        self.ready_btn = ReadyButton(self.game)


    def next_page(self):
        pass

    def prev_page(self):
        pass

    def set_attack_mode(self):
        self.mode = "attack"
        self.page = 0

        units = [[self.game.hood_warrior_image, [self.game.attack_center.attack, HoodWarrior]]]

        self.set_btns(units)

    def set_defence_mode(self):
        self.mode = "defence"
        self.page = 0

        units = [[self.game.arrow_tower_image, [self.game.defence_center.build, ArrowTower]],
                 [self.game.arrow_tower_image, [self.game.defence_center.build, ArrowTower]]]

        self.set_btns(units)

    def set_btns(self, units):
        num_change = 0
        for i, u in enumerate(units):
            num_change += 1
            if i > len(self.unit_btns):
                break

            self.unit_btns[i].set_unit_btn(u[0])
            self.unit_btns[i].set_action(*u[1])

        null_image = pg.Surface((DATA_RECORD_WIDTH, DATA_RECORD_HEIGHT))
        null_image.fill(DARK_GREY)
        for j in range(num_change % len(self.unit_btns)):
            unit_btn_index = j+num_change
            self.unit_btns[unit_btn_index].set_unit_btn(null_image)
            self.unit_btns[unit_btn_index].set_action(lambda: None)


    def update(self):
        pass


class ReadyButton(pg.sprite.Sprite, ButtonBase):

    def __init__(self, game):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self)

        self.game = game

        self.image = pg.Surface((MENU_READY_WIDTH, MENU_READY_HEIGHT))
        self.image.fill(DARK_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = MENU_READY_X
        self.rect.y = MENU_READY_Y

        self.ready = False
        self.set_action(self.game.defence_center.set_ready)

    def update(self):
        self.btn_update()


class UnitButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, game, i, **kwargs):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self)

        self.game = game
        self.i = i

        image = pg.Surface((DATA_RECORD_WIDTH, DATA_RECORD_HEIGHT))
        image.fill(BLACK)
        self.set_unit_btn(image)

    def update(self):
        self.btn_update()

    def set_unit_btn(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = DATA_LIST_X
        self.rect.y = DATA_LIST_Y + (self.i * DATA_RECORD_HEIGHT)


class ModeButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, game, x, y, image):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.mouse_down: bool = False
        self.button_action: tuple = (lambda: None, [], {})

    def update(self):
        self.btn_update()


class MenuUnitInfo(pg.sprite.Sprite):
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

