import pygame as pg


class Entity:
    def __init__(self, image, x, y, speed):
        self.img = pg.image.load(image)
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
