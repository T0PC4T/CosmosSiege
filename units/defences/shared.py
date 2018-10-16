from settings import *
import pygame as pg
vec = pg.math.Vector2

class Defence():

    def __init__(self, game, src_img, pos, min_range, max_range, fire_rate, projectile):
        self.game = game
        self.image = src_img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = vec(pos)
        self.min_range = min_range
        self.max_range = max_range
        self.projectile = projectile
        self.target = None
        self.fire_rate = fire_rate
        self.next_shot = 0

    @staticmethod
    def get_type():
        return "defence"

    def vec_in_range(self, d):
        return d > self.min_range and d < self.max_range

    def defence_update(self):
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
            for attacker in self.game.attackers:
                if not attacker.can_shoot:
                    continue
                d = (self.pos - attacker.get_pos()).length()
                if self.vec_in_range(d):
                    self.target = attacker
                    break

        if self.target and not self.next_shot:
            self.shoot()

    def shoot(self):
        self.projectile(self.game, self.pos, self.target)
        self.next_shot = self.fire_rate

    def update(self):
        self.defence_update()


class Projectile():
    def __init__(self, game, src_img, pos, target, speed, duration, damage, bullet_alg="predictive"):
        self.game = game
        self.pos = vec(pos)

        if bullet_alg == "predictive":
            current_target_pos = vec(target.get_pos())
            distance = current_target_pos - self.pos
            distance_frames = distance.length() / speed
            target_distance = target.get_velocity() * distance_frames
            moved_target_pos = current_target_pos + target_distance
            distance = moved_target_pos - self.pos
            distance_frames = distance.length() / speed
            moved_target_distance = target.get_velocity().scale_to_length(target.get_speed*distance_frames)
            self.target_pos = moved_target_pos + moved_target_distance
        else:
            self.target_pos = vec(target.get_pos())

        self.speed = speed
        self.duration = duration
        self.damage = damage

        self.velocity = self.target_pos - pos
        self.velocity.scale_to_length(speed)
        self.rotation = self.velocity.angle_to(vec(1, 0))

        self.image = pg.transform.rotate(src_img, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hit_rect = pg.Rect(*pos, 4, 4)

    @staticmethod
    def hit_hit_rect(one, two):
        return one.hit_rect.colliderect(two.hit_rect)

    def die(self):
        self.kill()

    def hit(self, hit):
        hit.subtract_health(self.damage)
        self.die()

    def bullet_update(self):
        self.pos = self.pos + self.velocity
        self.rect.topleft = self.pos
        self.hit_rect.topleft = self.rect.topleft
        self.duration -= 1

        if self.duration <= 0:
            self.die()

        for hit in pg.sprite.spritecollide(self, self.game.attackers, False, Projectile.hit_hit_rect):
            self.hit(hit)




    def update(self):
        self.bullet_update()