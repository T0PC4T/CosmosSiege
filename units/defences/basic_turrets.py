import pygame as pg
from settings import *
from .shared import Defence, Projectile
from ..shared import Unit


class BasicTurret(Defence, pg.sprite.Sprite):
    price = 20

    def __init__(self, game, pos):
        Defence.__init__(self, game=game,
                         src_img=game.basic_turret_img,
                         pos=pos,
                         min_range=TILE_SIZE*4,
                         max_range=TILE_SIZE*24,
                         fire_rate=FPS*2,
                         projectile=Ball,
                         projectile_speed=5,
                         projectile_duration=FPS*7,
                         projectile_damage=5)
        self.groups = game.all_sprites, game.defences
        pg.sprite.Sprite.__init__(self, self.groups)

        # Defence Center variables

    def upgrade_fire_rate(self):
        if self.fire_rate > 10 and self.game.defence_center.buy_option(20):
            self.fire_rate -= 5

    def get_title(self):
        return "Basic Turret"

    def get_options(self):
        return [[[self.game.blue_add_img, "Fire rate"], [self.upgrade_fire_rate]]]

    def update(self):
        self.defence_update()
        if self.target:
            self.rotation = (self.target.get_pos() - self.pos).angle_to(pg.Vector2(1, 0))
            self.image = pg.transform.rotate(self.src_img, self.rotation)


class Ball(Projectile, pg.sprite.Sprite):
    def __init__(self, game, pos, target, speed, duration, damage):
        image = pg.Surface((TILE_SIZE//4, TILE_SIZE//4))
        image.fill(BLACK)
        pg.draw.circle(image, RED, (TILE_SIZE//8, TILE_SIZE//8), TILE_SIZE//8)
        image.set_colorkey(BLACK)
        Projectile.__init__(self, game, image, pos, target, speed, duration, damage)
        self.groups = game.all_sprites, game.projectiles
        pg.sprite.Sprite.__init__(self, self.groups)




