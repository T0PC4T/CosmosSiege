import pygame as pg
from settings import *
from random import randint

class ImageAssets():
    def __init__(self):
        self.background_image = pg.Surface((ARENA_WIDTH, ARENA_HEIGHT))
        self.background_image.fill(BGCOLOUR)

        for i in range(70):
            pos_x = randint(TILE_SIZE, ARENA_WIDTH-TILE_SIZE)
            pos_y = randint(TILE_SIZE, ARENA_WIDTH-TILE_SIZE)
            size = randint(1, 3)
            pg.draw.circle(self.background_image, WHITE, (pos_x, pos_y), size)



    def add_image(self, name, cls):
        setattr(self, name, cls().get_image())


class ImageBuilder(object):
    width = TILE_SIZE
    height = TILE_SIZE
    row_pixels = 20
    col_pixels = 20
    data = [[]]
    canvas = None

    def get_data(self):
        data = self.data
        return data

    def get_pixels(self):
        return len(self.data[0])

    def __init__(self):
        self.canvas = pg.Surface((self.width, self.height))
        self.canvas.fill(BGCOLOUR)

        pixel_dim = self.width // self.get_pixels()

        for row_i, row in enumerate(self.get_data()):
            for cell_i, cell_colour in enumerate(row):
                x = cell_i*pixel_dim
                y = row_i*pixel_dim
                px = pg.Surface((pixel_dim, pixel_dim))
                px.fill(cell_colour)
                self.canvas.blit(px, (x, y))

        self.canvas.set_colorkey(BGCOLOUR)

    def get_image(self):
        return self.canvas
