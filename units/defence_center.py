import pygame as pg
from settings import *


class DefenceCenter(pg.sprite.Sprite):
    def __init__(self, game, tile_x, tile_y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = pg.Surface((TILE_SIZE*2, TILE_SIZE*2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = tile_x * TILE_SIZE
        self.rect.y = tile_y * TILE_SIZE

        # Defence Center variables

        self.gold = 100
        self.building = False

    def not_building(self):
        self.building = False

    def build(self, unit_id):
        if unit_id == 1:
            self.building_image = pg.Surface((TILE_SIZE, TILE_SIZE))
            self.building_image.fill(GREEN)
        elif unit_id == 2:
            self.building_image = pg.Surface((TILE_SIZE, TILE_SIZE))
            self.building_image.fill(RED)

        self.building = True

    def draw_effects(self):
        if self.building:
            pg.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))
            self.draw_grid()
            self.draw_building_blueprint()

    def draw_building_blueprint(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        tile_x = mouse_x - (mouse_x % TILE_SIZE)
        tile_y = mouse_y - (mouse_y % TILE_SIZE)
        self.game.screen.blit(self.building_image, (tile_x, tile_y))

    def draw_grid(self):
        for x in range(0, ARENA_WIDTH, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (x, 0), (x, ARENA_HEIGHT))

        for y in range(0, ARENA_HEIGHT, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (0, y), (ARENA_WIDTH, y))

    def update(self):
        pass