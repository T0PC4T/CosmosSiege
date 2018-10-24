from settings import *
import pygame as pg
vec = pg.math.Vector2
import random
from ..shared import Unit
from assets import Images

class Structure(Unit, pg.sprite.Sprite):
    def __init__(self, game, src_img, pos):
        Unit.__init__(self, game)
        self.groups = game.all_sprites, game.defences
        pg.sprite.Sprite.__init__(self, self.groups)
        self.src_img = src_img
        self.image = src_img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = vec(pos)
        self.price = getattr(self, "price", 0)
        self.sell_value = getattr(self, "price", 0)

    @staticmethod
    def get_type():
        return "defence"

    def die(self):
        self.kill()

    def get_info(self):
        return {"Value": self.sell_value}

    def _get_options(self):
        return [[[Images.blue_add_img, "Sell"], [self.game.defence_center.sell_structure, self]]]

    def get_sell_value(self):
        return getattr(self, "sell_value", 0)

    def defence_update(self):
        self.btn_update()

    def update(self):
        self.defence_update()

class Defence(Structure):

    def __init__(self, game, pos, min_range, max_range, fire_rate,
                 projectile):

        Structure.__init__(self, game, self.src_img, pos)
        self.min_range = min_range
        self.max_range = max_range
        self.projectile = projectile
        self.target = None
        self.fire_rate = fire_rate
        self.next_shot = 0

    def get_range(self):
        if self.max_range > TILE_SIZE*7:
            return "LONG"
        else:
            return "SHORT"

    def get_info(self):
        return {"Dmg": self.projectile.damage,
                "Rate": self.fire_rate,
                "Rng": self.get_range(),
                "Value": self.sell_value}

    def get_projectile_pos(self):
        return vec(self.rect.center)

    def vec_in_range(self, d):
        return d > self.min_range and d < self.max_range

    def defence_update(self):
        self.btn_update()
        if self.next_shot > 0:
            self.next_shot -= 1

        if self.target:
            if not self.target.can_shoot:
                self.target = None
            else:
                d = (self.target.get_pos() - self.pos).length()
                if not self.vec_in_range(d):
                    self.target = None

        if not self.target:
            attackers = list(self.game.attackers)
            random.shuffle(attackers)
            for attacker in attackers:
                if not attacker.can_shoot:
                    continue
                d = (self.pos - attacker.get_pos()).length()
                if self.vec_in_range(d):
                    self.target = attacker
                    break

        if self.target and not self.next_shot:
            self.shoot()

    def shoot(self):
        self.projectile(self.game, self, self.target)
        self.next_shot = self.fire_rate




class Projectile(pg.sprite.Sprite):
    def __init__(self, game, turret, target, bullet_alg="predictive"):
        self.game = game
        self.groups = game.all_sprites, game.projectiles
        pg.sprite.Sprite.__init__(self, self.groups)

        self.turret = turret
        self.pos = vec(turret.get_projectile_pos())

        self.target = target

        if bullet_alg == "predictive":
            if target.get_velocity().length() == 0:
                self.target_pos = target.get_pos()
            else:
                current_target_pos = target.get_pos()
                current_distance = current_target_pos - self.pos
                distance_frames = current_distance.length() / self.speed
                target_distance = target.get_velocity() * distance_frames

                moved_target_pos = current_target_pos + target_distance
                moved_distance = moved_target_pos - self.pos
                distance_multiplier = moved_distance.length() / current_distance.length()
                multiplied_frames = distance_frames * distance_multiplier
                moved_target_vec = target.get_velocity() * multiplied_frames
                self.target_pos = current_target_pos + moved_target_vec
        else:
            self.target_pos = target.get_pos()

        self.bullet_alg = bullet_alg

        self.set_projectile(self.target_pos)
        self.rect.center = self.pos
        self.hit_rect = pg.Rect(*self.pos, 4, 4)
        self.hit_rect.center = self.rect.center

    def set_projectile(self, target_pos):
        self.velocity = target_pos - self.pos
        self.velocity.scale_to_length(self.speed)
        self.rotation = self.velocity.angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.src_img, self.rotation)
        self.rect = self.image.get_rect()

    @staticmethod
    def hit_hit_rect(one, two):
        return one.hit_rect.colliderect(two.hit_rect)

    def die(self):
        self.kill()

    def hit(self, hit):
        hit.subtract_hp(self.damage)
        self.die()

    def bullet_update(self):
        if self.bullet_alg == "homing" and self.target.can_shoot:
            self.set_projectile(self.target.get_pos())

        self.pos = self.pos + self.velocity
        self.rect.center = self.pos
        self.hit_rect.center = self.rect.center
        self.duration -= 1

        if self.duration <= 0:
            self.die()

        for hit in pg.sprite.spritecollide(self, self.game.attackers, False, Projectile.hit_hit_rect):
            self.hit(hit)




    def update(self):
        self.bullet_update()