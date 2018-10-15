import pygame as pg
from settings import *
from random import randint, choice


class AttackCenter(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.attack_center_img
        self.rect = self.image.get_rect()

        random_y = randint(0, ARENA_HEIGHT - TILE_SIZE)
        self.tile_y = (random_y - (random_y % TILE_SIZE)) // TILE_SIZE
        self.tile_x = 0
        self.rect.x = self.tile_x * TILE_SIZE
        self.rect.y = self.tile_y * TILE_SIZE

        # Restrict grid

        self.game.grid[self.tile_y][self.tile_x] = self
        self.game.grid[self.tile_y+1][self.tile_x] = self

        # Attack Center variables

        self.attackers = Attackers(self.game)
        self.paths = list()

        # Grid Variables

        self.generate_paths(self.game.grid)

    @staticmethod
    def get_type():
        return "attack_center"

    def attack(self, unit_cls):
        unit_cls(self.game)

    def get_path(self):
        return choice(self.paths)

    def generate_paths(self, cur_grid):
        start_path = [self.tile_x, self.tile_y]
        pathfinders = [PathFinder(self.game, cur_grid, start_path, list())]
        paths = list()
        visited_cells = list()
        while len(paths) == 0 and pathfinders:
            lost_pathfinders = list()
            new_pathfinders = list()
            for pf in pathfinders:
                r_code, r_data = pf.take_step(visited_cells)
                visited_cells.append(pf.current_position)

                if r_code == "new_possibilities":
                    new_pathfinders.extend(r_data)
                elif r_code == "no_paths":
                    lost_pathfinders.append(pf)
                elif r_code == "defence_center":
                    paths.append(r_data)

            for pf in lost_pathfinders:
                pathfinders.remove(pf)

            for pf in new_pathfinders:
                pathfinders.append(pf)

        if paths:
            self.paths = paths
            return self.paths
        return False

    def set_ready(self):
        pass

    def update(self):

        # OTHER STUFF
        pass


class PathFinder():
    def __init__(self, game, grid, start_pos: list, path: list):
        self.grid = grid
        self.game = game
        self.current_position = start_pos
        self.possibilities = list()
        path.append(start_pos)
        self.path = path

    def _ways(self):
        return [[self.current_position[0]+1, self.current_position[1]],
                [self.current_position[0]-1, self.current_position[1]],
                [self.current_position[0], self.current_position[1]+1],
                [self.current_position[0], self.current_position[1]-1]]

    def get_ways(self, visited_cells):
        possible_ways = list()
        for way in self._ways():
            if way[0] < 0 or way[0] >= len(self.grid[0]) or way[1] < 0 or way[1] >= len(self.grid):
                continue

            b = False
            for p in self.path + visited_cells:
                if way == p:
                    b = True
                    break
            if b:
                continue

            if self._get_grid_cell(way) is None or self._get_grid_cell(way) is self.game.defence_center:
                possible_ways.append(way)

        return possible_ways

    def _get_grid_cell(self, way):
        return self.grid[way[1]][way[0]]

    def take_step(self, visited_cells):
        ways = self.get_ways(visited_cells)
        if len(ways) == 0:
            return "no_paths", None

        elif len(ways) == 1:
            self.current_position = ways[0]
            self.path.append(ways[0])
            if self._get_grid_cell(ways[0]) is self.game.defence_center:
                return "defence_center", self.get_path()
            else:
                return "new_possibilities", list()
        else:
            new_pathfinders = list()
            for way in ways[1:]:
                if self._get_grid_cell(ways[0]) is self.game.defence_center:
                    return "defence_center", self.path + [way]
                else:
                    new_pathfinders.append(PathFinder(self.game, self.grid, way, list(self.path)))

            self.current_position = ways[0]
            self.path.append(ways[0])
            if self._get_grid_cell(ways[0]) is self.game.defence_center:
                return "defence_center", self.get_path()

            return "new_possibilities", new_pathfinders

    def get_path(self):
        return self.path

class Attackers():
    def __init__(self, game):
        self.game = game
        self.attackers = list()

    def add_enemy(self, attacker):
        self.attackers.append(attacker(self.game))

    def start_round(self):
        pass

    def update(self):
        pass