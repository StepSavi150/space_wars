import pygame as pg
from math import sqrt
from entity import Entity
from player import Player
from asteroid import Asteroid
from random import randint

# Initing pg.
pg.init()


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Constant variables/variables
keys = []
pos = [10, 10]
fps = 60
WIDTH = 300
HEIGHT = 600
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Space Wars")
pg.display.set_icon(pg.image.load("icon.png"))
clock = pg.time.Clock()

# Timer
number_iter = 0
time = 0

skull = pg.image.load('skull.png')
pause = pg.image.load('pause_button.png')
retry = pg.image.load('retry.png')

asteroids = [Asteroid("asteroid.png", randint(0, WIDTH - 32), HEIGHT // 2, 2), Asteroid("asteroid.png", randint(0, WIDTH - 32), HEIGHT // 2, 2), Asteroid("asteroid.png", randint(0, WIDTH - 32), HEIGHT // 2, 2), Asteroid("asteroid.png", randint(0, WIDTH - 32), HEIGHT // 2, 2)]
plr = Player("player.png", WIDTH // 2, HEIGHT - 50, 2)

# Fonts
font = pg.font.Font('font.ttf', 24)
lose_text = font.render('You lost', False, (0, 0, 0))
time_text = font.render(str(time), False, (0, 0, 0))
lose_width = lose_text.get_width()
lose_height = lose_text.get_height()

# Flags
game_run = True
game_loss = False

while game_run:
    # Logic
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()

    keys = pg.key.get_pressed()
    move = keys[pg.K_d] - keys[pg.K_a]
    shoot = keys[pg.K_SPACE]

    clock.tick(fps)

    # Draw
    screen.fill((255, 255, 255))
    pg.draw.line(screen, (0, 0, 0), (0, 50), (WIDTH, 50), 5)
    plr.update(move)
    plr.draw(screen)
    for e in asteroids:
        e.draw(screen)
        e.move()
    pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, 50))
    screen.blit(time_text, (16, 16))
    if game_loss == False:
        time_text = font.render(str(time), False, (0, 0, 0))

    if game_loss == True:
        # Drawing Death Screen
        screen.fill((255, 255, 255))
        screen.blit(lose_text, (WIDTH // 2 - lose_width // 2, HEIGHT // 2 - lose_height))
        screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 - time_text.get_height() - 50))
        screen.blit(skull, (WIDTH // 2 - 16, HEIGHT // 2 + 50))
        screen.blit(retry, (WIDTH // 2 - 16, HEIGHT // 2 + 100))

        # Reseting
        plr.x = WIDTH // 2
        plr.y = HEIGHT - 50
        time = 0
        number_iter = 0
        for e in asteroids:
            e.x = randint(0, WIDTH - 16)
            e.y = 18
    else:
        time = number_iter // fps
        number_iter += 1

    if (WIDTH // 2 - 16 <= pos[0] <= WIDTH // 2 - 16 + 32 and HEIGHT // 2 + 100 <= pos[1] <= HEIGHT // 2 + 100 + 32):
        game_loss = False

    pg.display.flip()

    # Maths
    for e in asteroids:
        if e.y == HEIGHT:
            e.y = 18
            e.x = randint(0, WIDTH - 16)
        if distance(plr.x, plr.y, e.x, e.y) <= 16:
            game_loss = True
pg.quit()
