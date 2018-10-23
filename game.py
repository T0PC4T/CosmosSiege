import sys
from units import *
from interface.menu import *
from assets import *
from random import randint


class Game:
    def __init__(self, screen, clock, server_connection=None):
        self.screen = screen
        self.clock = clock
        self.playing = True
        self.assets = list()
        self.load_assets()
        self.grid = [list([None] * ARENA_TILE_WIDTH) for i in range(ARENA_TILE_HEIGHT)]
        ###########################################################
        ###########################################################

        # Sprites

        self.all_sprites = pg.sprite.Group()
        self.structures = pg.sprite.Group()
        self.defences = pg.sprite.Group()
        self.attackers = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.menu_items = pg.sprite.Group()
        self.menu = InGameMenu(self)
        self.defence_center = DefenceCenter(self)
        self.attack_center = AttackCenter(self)
        self.null_focus = Unit(self)
        self.menu.set_focus(self.null_focus)
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
        self.global_info = ["[C] {} ({})".format(*self.defence_center.get_global_info())]
        self.all_sprites.update()

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.background_image, (0, 0))
        self.projectiles.draw(self.screen)
        self.structures.draw(self.screen)
        self.defences.draw(self.screen)
        self.attackers.draw(self.screen)
        self.menu_items.draw(self.screen)
        self.defence_center.draw_effects()
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

        if pg.mouse.get_pressed()[2]:
            self.defence_center.not_building()
            self.menu.set_focus(self.null_focus)
