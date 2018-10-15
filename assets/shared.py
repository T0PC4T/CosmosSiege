import pygame as pg
from settings import *


class ImageBuilder(object):
    width = TILE_SIZE
    height = TILE_SIZE
    row_pixels = 20
    col_pixels = 20
    data = [[]]

    def get_data(self):
        data = self.data
        return data

    def get_pixels(self):
        return len(self.data[0])

    def get_image(self):
        self.canvas = pg.Surface((self.width, self.height))
        self.canvas.fill(BLACK)

        pixel_dim = self.width // self.get_pixels()

        for row_i, row in enumerate(self.get_data()):
            for cell_i, cell_colour in enumerate(row):
                x = cell_i*pixel_dim
                y = row_i*pixel_dim
                px = pg.Surface((pixel_dim, pixel_dim))
                px.fill(cell_colour)
                self.canvas.blit(px, (x, y))

        self.canvas.set_colorkey(BLACK)

        return self.canvas
