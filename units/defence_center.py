import pygame as pg
from settings import *
from .defences import *
from random import randint
vec = pg.math.Vector2
from .shared import Unit
from assets import Images

class DefenceCenter(Unit, pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.structures
        pg.sprite.Sprite.__init__(self, self.groups)
        Unit.__init__(self, game)


        self.image = pg.Surface((TILE_SIZE*2, TILE_SIZE*2))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        random_y = randint(0, ARENA_HEIGHT - TILE_SIZE)
        tile_y = (random_y - (random_y % TILE_SIZE)) // TILE_SIZE
        tile_x = ARENA_TILE_WIDTH-2
        self.rect.x = tile_x * TILE_SIZE
        self.rect.y = tile_y * TILE_SIZE

        pg.draw.circle(self.image, (randint(1, 255), randint(1, 255), randint(1, 255)), (TILE_SIZE, TILE_SIZE), TILE_SIZE)
        self.image.set_colorkey(BLACK)

        self.src_img = self.image
        # Restrict grid

        self.game.grid[tile_y][tile_x] = self
        self.game.grid[tile_y][tile_x+1] = self
        self.game.grid[tile_y+1][tile_x+1] = self
        self.game.grid[tile_y+1][tile_x] = self

        # Defence Center variables

        self.lives = 100
        self.credits = 300
        self.income = 10
        self.building = False
        self.defences = Defenders(self.game)

        # Grid Variables

    @staticmethod
    def get_type():
        return "defence_center"

    def get_title(self):
        return "Planet"

    def get_info(self):
        return {"Lives": str(self.lives),
                "Level": 0,
                "Credits": int(self.credits),
                "Income": int(self.income),
                }

    def get_options(self):
        return [[[Images.barracade_img, "Barricade ({})".format(Barricade.get_price(Barricade))], [self.game.defence_center.build, Barricade]],
                [[Images.basic_turret_img, "Beam ({})".format(BasicTurret.get_price(BasicTurret))], [self.game.defence_center.build, BasicTurret]],
                [[Images.spitter_img, "Spitter ({})".format(SpitterTurret.get_price(SpitterTurret))], [self.game.defence_center.build, SpitterTurret]]]

    def get_global_info(self):
        return self.credits, self.income

    def buy_option(self, cost, income=0):
        if self.credits >= cost:
            self.credits -= cost
            self.income += income
            return True
        return False

    def sell_structure(self, defence_cls):
        self.add_credits(defence_cls.get_sell_value())
        x, y = defence_cls.get_tile_x_tile_y()
        self.game.grid[y][x] = None
        defence_cls.die()

    def add_credits(self, credits, income=0):
        self.credits += credits
        self.income += income

    def end_round(self):
        self.credits += int(self.income)

    def subtract_life(self, amount=1):
        self.lives -= amount
        if self.lives == 0:
            self.kill()

    def not_building(self):
        self.building = False

    def build(self, defence_cls):
        if not self.game.attack_center.round_active():
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
        self.btn_update()

        # BUILDING

        if self.building and pg.mouse.get_pressed()[0]:
            clean_x, clean_y = self.get_blueprint_pos()
            tile_x, tile_y = clean_x//TILE_SIZE, clean_y//TILE_SIZE
            if tile_x < ARENA_TILE_WIDTH and tile_y < ARENA_TILE_HEIGHT:
                if self.game.grid[tile_y][tile_x] is None:
                    self.game.grid[tile_y][tile_x] = True
                    ways = self.game.attack_center.generate_paths(self.game.grid)
                    round_active = self.game.attack_center.round_active()
                    if ways and not round_active and self.buy_option(self.defence_cls.get_price(self.defence_cls)):
                        defence_init = self.defence_cls(self.game, vec(tile_x, tile_y) * TILE_SIZE)
                        self.game.grid[tile_y][tile_x] = self.defences.add_defence(defence_init)
                        self.not_building()
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
