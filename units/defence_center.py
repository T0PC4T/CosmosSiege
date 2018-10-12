import pygame as pg
from settings import *
from .defences import *

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
        self.defences = list()

        # Grid Variables

        grid_row = range(0, ARENA_TILE_WIDTH)
        grid_collumn = range(0, ARENA_TILE_HEIGHT)
        self.grid_sector_dict = dict()

        for c in grid_collumn:
            for r in grid_row:
                self.grid_sector_dict[self._gk(c, r)] = None

        self.grid_sector_dict[self._gk(tile_x, tile_y)] = True
        self.grid_sector_dict[self._gk(tile_x+1, tile_y)] = True
        self.grid_sector_dict[self._gk(tile_x+1, tile_y+1)] = True
        self.grid_sector_dict[self._gk(tile_x, tile_y+1)] = True

    def _gk(self, x, y):
        return "{}-{}".format(x, y)

    def create_enemy_path(self):
        pass

    def not_building(self):
        self.building = False

    def build(self, unit_id):
        self.unit_id = unit_id

        self.building_image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.building_image.fill(GREEN)

        pg.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))
        self.building = True

    def draw_effects(self):
        if self.building:
            self.draw_grid()
            x, y = self.draw_building_blueprint()
            if pg.mouse.get_pressed()[0]:
                if not self.grid_sector_dict.get(self._gk(x, y), True):
                    self.grid_sector_dict[self._gk(x, y)] = ArrowTower(self.game, x, y)
                    self.not_building()

    def draw_building_blueprint(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        tile_x = mouse_x - (mouse_x % TILE_SIZE)
        tile_y = mouse_y - (mouse_y % TILE_SIZE)
        self.game.screen.blit(self.building_image, (tile_x, tile_y))
        return tile_x//TILE_SIZE, tile_y//TILE_SIZE

    def draw_grid(self):
        for x in range(0, ARENA_WIDTH, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (x, 0), (x, ARENA_HEIGHT))

        for y in range(0, ARENA_HEIGHT, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (0, y), (ARENA_WIDTH, y))

    def update(self):
        pass