import pygame as pg
from settings import *

pg.init()
pg.font.init()
pg.mixer.init()


class GameSprite(pg.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pg.transform.scale(pg.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.move(coords)
    
    def reset(self):
        mw.blit(self.image, self.rect)


class Player(GameSprite):
    def __init__(self, filename, size, coords, speed=5, keys=[pg.K_UP, pg.K_DOWN]):
        super().__init__(filename, size, coords)
        self.speed = speed
        self.keys = keys
    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[self.keys[0]] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.keys[1]] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed


mw = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ping Pong")
clock = pg.time.Clock()

player_left = Player(PLAYER_LEFT_IMG, (40, 107), (0, 0), 12, keys=[pg.K_w, pg.K_s])
player_right = Player(PLAYER_RIGHT_IMG, (40, 107), (0, 0), 12, keys=[pg.K_UP, pg.K_DOWN])
player_right.rect.x = WIDTH - player_right.rect.width

game = True
finish = False
while game:
    if not finish:
        mw.fill(BACKGROUND_COLOR)

        player_left.update()
        player_right.update()

        player_left.reset()
        player_right.reset()

    else:
        pass

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    pg.display.update()
    clock.tick(FPS)