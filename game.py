import sys
from units import *
from interface.menu import *
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
        self.grid = [list([None] * ARENA_TILE_WIDTH) for i in range(ARENA_TILE_HEIGHT)]
        ###########################################################
        ###########################################################

        # Sprites

        self.all_sprites = pg.sprite.Group()
        self.defences = pg.sprite.Group()
        self.attackers = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.defence_center = DefenceCenter(self)
        self.attack_center = AttackCenter(self)
        self.menu = InGameMenu(self)


    def load_assets(self):
        self.defence_mode_btn_image = DefenceModeBtnImg().get_image()
        self.attack_mode_btn_image = AttackModeBtnImg().get_image()

        self.defence_center_img = DefenceCenterImg().get_image()
        self.attack_center_img = AttackCenterImg().get_image()
        self.arrow_tower_img = ArrowTowerImg().get_image()
        self.arrow_img = ArrowImg().get_image()
        self.hood_warrior_img = HoodWarriorImg().get_image()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
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
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
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
