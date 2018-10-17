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

        self.defence_menu_button = ModeButton(self.game, DEFENCE_MODE_X, MODE_Y, self.game.defence_mode_btn_img)
        self.defence_menu_button.set_action(lambda: self.set_defence_mode())

        self.attack_menu_button = ModeButton(self.game, ATTACK_MODE_X, MODE_Y, self.game.attack_mode_btn_img)
        self.attack_menu_button.set_action(lambda: self.set_attack_mode())

        ################################################################################################################

        self.unit_btns = list()

        for i in range(UNIT_BTN_NUM):
            self.unit_btns.append(UnitButton(self.game, i))

        self.prev_page_btn = PageButton(self.game, self, True)
        self.next_page_btn = PageButton(self.game, self, False)

        ################################################################################################################

        self.ready_btn = ReadyButton(self.game)

    def set_focus(self, *args, **kwargs):
        return self.menu_info.set_focus(*args, **kwargs)

    def next_page(self):
        if len(self.units) > UNIT_BTN_NUM*(self.page+1):
            self.page +=1
            self.set_btns()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.set_btns()

    def set_attack_mode(self):
        self.mode = "attack"
        self.page = 0

        self.units = [[self.game.scoutship_img, [self.game.attack_center.attack, ScoutShip]],
                      [self.game.red_ship, [self.game.attack_center.attack, RedShip]]]

        self.set_btns()

    def set_defence_mode(self):
        self.mode = "defence"
        self.page = 0

        self.units = [[self.game.basic_turret_img, [self.game.defence_center.build, BasicTurret]],
                     [self.game.basic_turret_img, [self.game.defence_center.build, BasicTurret]]]

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
        self.image.fill(MENU_READY_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.x = MENU_READY_X
        self.rect.y = MENU_READY_Y

    def update(self):
        self.btn_update()
        if self.game.attack_center.round_active():
            self.image = pg.Surface((MENU_READY_WIDTH, MENU_READY_HEIGHT))
            self.image.fill(MENU_COLOUR)
        else:
            self.image = pg.Surface((MENU_READY_WIDTH, MENU_READY_HEIGHT))
            self.image.fill(MENU_READY_COLOUR)



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

        self.set_clean_image()

        self.rect = self.image.get_rect()
        self.rect.x = MENU_INFO_X
        self.rect.y = MENU_INFO_Y

        self.text_font = pg.font.Font(FONT_DIR, MENU_INFO_TEXT_SIZE)

    def set_focus(self, focus_cls):
        self.focus_cls = focus_cls


    def update_focus(self):
        if self.focus_cls:
            self.set_clean_image()
            self.set_info(self.focus_cls.get_info())

    def set_clean_image(self):
        self.image = pg.Surface((MENU_INFO_WIDTH, MENU_INFO_HEIGHT))
        self.image.fill((20, 20, 20))

    def set_info(self, info_dict):
        i = 0
        for key, value in info_dict.items():

            textsurface = self.text_font.render('{}: {}'.format(key, value), False, (51, 255, 0))
            self.image.blit(textsurface, (0+MENU_BORDER, ((MENU_INFO_TEXT_SIZE)*i + MENU_BORDER)))
            i +=1

    def update(self):
        self.update_focus()