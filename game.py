import sys
from units.defence_center import *
from interface.menus import *
from assets import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.playing = True
        self.assets = list()
        self.load_assets()
        self.load_sprites()
        ###########################################################
        ###########################################################

    def load_assets(self):
        self.defence_mode_btn_image = DefenceModeBtnImg().get_image()
        self.attack_mode_btn_image = AttackModeBtnImg().get_image()

        self.defence_center_img = DefenceCenterImg().get_image()

        self.arrow_tower_image = ArrowTowerImg().get_image()
        self.hood_warrior_image = HoodWarriorImg().get_image()



    def load_sprites(self):
        self.all_sprites = pg.sprite.Group()
        self.defences = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.defence_center = DefenceCenter(self, tile_x=13, tile_y=11)
        self.menu = InGameMenu(self)

    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.defence_center.draw_effects()
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

        if pg.mouse.get_pressed()[2]:
            self.defence_center.not_building()
