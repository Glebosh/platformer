import pygame as pg
from setting import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT // 2)
        self.pos = vec(WIDTH / 2, HEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.vy = 0

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -=1
        # прыжок ток с платформы
        if hits:
            self.vel.y = PLAYER_JUMP


    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keystate[pg.K_UP]:
            pass
        if keystate[pg.K_DOWN]:
            pass

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc * 0.5

        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

