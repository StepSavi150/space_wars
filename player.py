from entity import Entity
import pygame as pg


class Player(Entity):
    def move_right(self):
        if self.x < 300 - 32:
            self.x += self.speed

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def update(self, move_dir):
        if move_dir == 1:
            self.move_right()
        if move_dir == -1:
            self.move_left()
