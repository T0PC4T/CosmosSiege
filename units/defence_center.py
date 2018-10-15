import pygame as pg
from settings import *
from .defences import *
from random import randint

class DefenceCenter(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.defence_center_img
        self.rect = self.image.get_rect()

        random_y = randint(0, ARENA_HEIGHT - TILE_SIZE)
        tile_y = (random_y - (random_y % TILE_SIZE)) // TILE_SIZE
        tile_x = ARENA_TILE_WIDTH-2
        self.rect.x = tile_x * TILE_SIZE
        self.rect.y = tile_y * TILE_SIZE

        # Restrict grid

        self.game.grid[tile_y][tile_x] = self
        self.game.grid[tile_y][tile_x+1] = self
        self.game.grid[tile_y+1][tile_x+1] = self
        self.game.grid[tile_y+1][tile_x] = self

        # Defence Center variables

        self.lives = 100
        self.gold = 100
        self.building = False
        self.defences = Defenders(self.game)

        # Grid Variables

    @staticmethod
    def get_type():
        return "defence_center"

    def subtract_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.kill()

    def not_building(self):
        self.building = False

    def build(self, defence_cls):
        self.defence_cls = defence_cls

        self.building_image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.building_image.fill(GREEN)

        pg.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))
        self.building = True

    def draw_effects(self):

        # BUILDING

        if self.building:
            self.draw_grid()
            tile_x, tile_y = self.get_blueprint_pos()
            self.game.screen.blit(self.building_image, (tile_x, tile_y))

        # OTHER STUFF

    def get_blueprint_pos(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        clean_x = mouse_x - (mouse_x % TILE_SIZE)
        clean_y = mouse_y - (mouse_y % TILE_SIZE)
        return clean_x, clean_y

    def draw_grid(self):
        for x in range(0, ARENA_WIDTH, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (x, 0), (x, ARENA_HEIGHT))

        for y in range(0, ARENA_HEIGHT, TILE_SIZE):
            pg.draw.line(self.game.screen, LIGHTGREY, (0, y), (ARENA_WIDTH, y))

    def set_ready(self):
        pass

    def update(self):

        # BUILDING

        if self.building and pg.mouse.get_pressed()[0]:
            clean_x, clean_y = self.get_blueprint_pos()
            tile_x, tile_y = clean_x//TILE_SIZE, clean_y//TILE_SIZE
            if tile_x < ARENA_TILE_WIDTH and tile_y < ARENA_TILE_HEIGHT:
                if not self.game.grid[tile_y][tile_x]:
                    self.game.grid[tile_y][tile_x] = True
                    r = self.game.attack_center.generate_paths(self.game.grid)

                    if r:
                        self.game.grid[tile_y][tile_x] = self.defences.add_defence(self.defence_cls(self.game, tile_x, tile_y))
                        # self.not_building()
                    else:
                        self.game.grid[tile_y][tile_x] = None

        # OTHER STUFF



class Defenders():
    def __init__(self, game):
        self.game = game
        self.defenders = list()

    def add_defence(self, defender):
        self.defenders.append(defender)
        return defender

    def try_build(self):
        pass

    def update(self):
        pass


class Enemies():
    def __init__(self, game):
        self.game = game
        self.attackers = list()

    def add_enemy(self, attacker):
        self.attackers.append(attacker(self.game))

    def start_round(self):
        pass

    def update(self):
        pass