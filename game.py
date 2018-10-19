import sys
from units import *
from interface.menu import *
from assets import *
from random import randint


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.font.init()
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
        self.menu = InGameMenu(self)
        self.defence_center = DefenceCenter(self)
        self.attack_center = AttackCenter(self)
        self.menu.set_focus(Unit(self))
        ###########################################################
        # CIRCLE REFERENCE #
        ###########################################################

        self.menu.ready_btn.set_action(self.attack_center.set_ready)

    def load_assets(self):

        self.background_image = pg.Surface((ARENA_WIDTH, ARENA_HEIGHT))
        self.background_image.fill(BGCOLOUR)

        for i in range(70):
            pos_x = randint(TILE_SIZE, ARENA_WIDTH-TILE_SIZE)
            pos_y = randint(TILE_SIZE, ARENA_WIDTH-TILE_SIZE)
            size = randint(1, 3)
            pg.draw.circle(self.background_image, WHITE, (pos_x, pos_y), size)

        # Other assets
        self.page_btn_img = PageBtnImg().get_image()
        self.defence_center_img = DefenceCenterImg().get_image()
        self.attack_center_img = AttackCenterImg().get_image()
        self.basic_turret_img = BasicTurret().get_image()
        self.scoutship_img = ScoutShipImg().get_image()
        self.red_ship_img = RedShipImg().get_image()
        self.blue_add_img = BlueAddImg().get_image()
        # FONTS


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
        credits, income = self.defence_center.get_global_info()
        self.global_info = ["[C] {} ({})".format(credits, income)]
        self.all_sprites.update()

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.background_image, (0, 0))
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
