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
        self.image.fill(MENU_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.x = ARENA_WIDTH
        self.rect.y = 0
        self.mode = "defence"
        self.load_menus()
        self.page = 0
        self.units = list()

    def load_menus(self):
        self.menu_info = MenuUnitInfo(self.game)

        ################################################################################################################

        self.defense_menu_button = ModeButton(self.game, DEFENCE_MODE_X, MODE_Y, self.game.defence_mode_btn_img)
        self.defense_menu_button.set_action(lambda: self.set_defence_mode())

        self.attack_menu_button = ModeButton(self.game, ATTACK_MODE_X, MODE_Y, self.game.attack_mode_btn_img)
        self.attack_menu_button.set_action(lambda: self.set_attack_mode())

        ################################################################################################################

        self.unit_btns = list()

        for i in range(UNIT_BTN_NUM):
            self.unit_btns.append(UnitButton(self.game, i))


        self.set_defence_mode()

        self.prev_page_btn = PageButton(self.game, self, True)
        self.next_page_btn = PageButton(self.game, self, False)

        ################################################################################################################

        self.ready_btn = ReadyButton(self.game)

    def next_page(self):
        if len(self.units) > UNIT_BTN_NUM*(self.page+1):
            self.page +=1
            self.set_btns()

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.set_btns()

    def set_attack_mode(self):
        self.mode = "attack"
        self.page = 0

        self.units = [[self.game.hood_warrior_img, [self.game.attack_center.attack, HoodWarrior]],
                 [self.game.element_warrior_img, [self.game.attack_center.attack, ElementWarrior]],
                 [self.game.element_warrior_img, [self.game.attack_center.attack, ElementWarrior]],
                 [self.game.element_warrior_img, [self.game.attack_center.attack, ElementWarrior]],
                 [self.game.element_warrior_img, [self.game.attack_center.attack, ElementWarrior]]]

        self.set_btns()

    def set_defence_mode(self):
        self.mode = "defence"
        self.page = 0

        self.units = [[self.game.arrow_tower_img, [self.game.defence_center.build, ArrowTower]],
                     [self.game.arrow_tower_img, [self.game.defence_center.build, ArrowTower]]]

        self.set_btns()

    def set_btns(self):
        unit_btns = list()
        null_image = pg.Surface((DATA_RECORD_WIDTH, DATA_RECORD_HEIGHT))
        null_image.fill(DARK_GREY)

        for i in range(UNIT_BTN_NUM):
            if len(self.units) > i+self.page*UNIT_BTN_NUM:
                unit_btns.append(self.units[i + (self.page*UNIT_BTN_NUM)])
            else:
                unit_btns.append([null_image, [lambda: None]])

        for i, b in enumerate(unit_btns):
            self.unit_btns[i].set_unit_btn(b[0])
            self.unit_btns[i].set_action(*b[1])

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
        self.set_action(self.game.attack_center.set_ready)

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


class ModeButton(ButtonBase, pg.sprite.Sprite):
    def __init__(self, game, x, y, image):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self)

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

class PageButton(ButtonBase, pg.sprite.Sprite):
    def __init__(self, game, menu, prev):
        ButtonBase.__init__(self)
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.menu = menu

        if prev:
            self.image = pg.transform.flip(self.game.page_btn_img, True, False)
        else:
            self.image = self.game.page_btn_img

        self.rect = self.image.get_rect()
        if prev:
            self.rect.x = PAGE_PREV_X
        else:
            self.rect.x = PAGE_NEXT_X

        self.rect.y = PAGE_Y

        if prev:
            self.set_action(self.menu.prev_page)
        else:
            self.set_action(self.menu.next_page)



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

