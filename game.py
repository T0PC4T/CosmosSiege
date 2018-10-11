# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import sys
from settings import *
from sprites import *
from menus import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100, 100)
        self.load_data()
        self.load_sprites()
        ###########################################################
        ###########################################################

    def load_data(self):
        pass

    def load_sprites(self):
        self.all_sprites = pg.sprite.Group()
        self.menu = InGameMenu(self)
        self.defence_center = DefenceCenter(self, tile_x=13, tile_y=11)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            # self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_interface(self):
        self.draw_grid()

    def draw_grid(self):
        for x in range(0, ARENA_WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, ARENA_HEIGHT))

        for y in range(0, ARENA_HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (ARENA_WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)

        self.draw_interface()

        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_ESCAPE:
            #         self.quit()
            #     if event.key == pg.K_LEFT:
            #         self.player.move(dx=-1)
            #     if event.key == pg.K_RIGHT:
            #         self.player.move(dx=1)
            #     if event.key == pg.K_UP:
            #         self.player.move(dy=-1)
            #     if event.key == pg.K_DOWN:
            #         self.player.move(dy=1)

# create the game object
g = Game()
g.run()
