import pygame as pg
from settings import *
from .buttons import ButtonBase

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
        self.load_menus()


    def load_menus(self):
        self.menu_info = MenuUnitData(self.game)
        self.ready_btn = ReadyButton(self.game)

    def set_focus(self, *args, **kwargs):
        return self.menu_info.set_focus(*args, **kwargs)

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
    def __init__(self, game, i):

        # Sprite base

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self)

        self.game = game
        self.i = i

        self.null_image = pg.Surface((DATA_RECORD_WIDTH, DATA_RECORD_HEIGHT))
        self.null_image.fill(DARK_GREY)
        self.set_unit_btn()

    def update(self):
        self.btn_update()

    def set_unit_btn(self, image=None, func=(lambda:None,)):
        self.set_action(*func)
        self.image = image or self.null_image
        self.rect = self.image.get_rect()
        self.rect.x = DATA_LIST_X
        self.rect.y = DATA_LIST_Y + (self.i * DATA_RECORD_HEIGHT)

class MenuUnitData(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = pg.Surface((MENU_INFO_WIDTH, (TITLE_STRIP_HEIGHT + MENU_INFO_HEIGHT + DATA_LIST_HEIGHT)))
        self.image.fill(DARK_GREY)

        self.set_clean_info()

        self.rect = self.image.get_rect()
        self.rect.x = MENU_X
        self.rect.y = MENU_Y

        self.focus_cls = None

        self.title_font = pg.font.Font(FONT_DIR, MENU_INFO_TITLE)
        self.text_font = pg.font.Font(FONT_DIR, MENU_INFO_TEXT_SIZE)

        # MENU BTNS

        self.unit_btns = list()
        self.unit_options = list()

        for i in range(UNIT_BTN_NUM):
            self.unit_btns.append(UnitButton(self.game, i))

        self.prev_page_btn = PageButton(self.game, self, True)
        self.next_page_btn = PageButton(self.game, self, False)

        self.page = 0
        self.units = list()

    def set_focus(self, focus_cls):
        self.focus_cls = focus_cls
        self.set_unit(focus_cls.get_title(), focus_cls.get_img(), focus_cls.get_options())

    def update_focus(self):
        if self.focus_cls:
            self.set_clean_info()
            self.set_info(self.focus_cls.get_info())

    def set_clean_unit(self):
        title_image = pg.Surface((TITLE_STRIP_WIDTH, MENU_INFO_Y))
        title_image.fill(DARK_GREY)
        self.image.blit(title_image, (0, 0))

    def set_clean_info(self):
        info_image = pg.Surface((MENU_INFO_WIDTH, MENU_INFO_HEIGHT))
        info_image.fill(GREY)
        self.image.blit(info_image, (0, MENU_INFO_Y))

    def set_unit(self, title, img, unit_options):
        self.unit_options = unit_options
        self.set_clean_unit()
        scaled_img = pg.transform.scale(img, (UNIT_IMG_WIDTH-TEXT_PADDING*2, UNIT_IMG_HEIGHT-TEXT_PADDING*2))
        self.image.blit(scaled_img, (TEXT_PADDING, TITLE_STRIP_HEIGHT+TEXT_PADDING))
        textsurface = self.title_font.render(title, False, FONT_COLOUR)
        self.image.blit(textsurface, (TEXT_PADDING, TEXT_PADDING))

        # Unit Btns

        for i, unit_btn in enumerate(self.unit_btns):
            if len(self.unit_options) > i + (self.page * UNIT_BTN_NUM):
                unit_option = self.unit_options[i]
                unit_option_canvas = pg.Surface((DATA_RECORD_WIDTH, DATA_LIST_HEIGHT))
                unit_option_canvas.fill(DARK_GREY)
                unit_option_image = unit_option[0][0]
                unit_option_image = pg.transform.scale(unit_option_image, (DATA_RECORD_HEIGHT, DATA_RECORD_HEIGHT))
                unit_option_canvas.blit(unit_option_image, (0, 0))
                unit_option_text = unit_option[0][1]
                unit_option_text = self.text_font.render(unit_option_text, False, FONT_COLOUR)
                unit_option_canvas.blit(unit_option_text, (DATA_RECORD_HEIGHT + TEXT_PADDING, TEXT_PADDING))
                unit_btn.set_unit_btn(unit_option_canvas, unit_option[1])
            else:
                unit_btn.set_unit_btn()


    def set_info(self, info_dict):
        i = 0
        for key, value in info_dict.items():
            textsurface = self.text_font.render('{}: {}'.format(key, value), False, FONT_COLOUR)
            y = MENU_INFO_Y + (TILE_SIZE)*i
            self.image.blit(textsurface, (TEXT_PADDING, y))
            i +=1

    def next_page(self):
        if len(self.units) > UNIT_BTN_NUM*(self.page+1):
            self.page +=1
            self.set_btns()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
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
        self.update_focus()




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

