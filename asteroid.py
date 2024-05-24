from entity import Entity


class Asteroid(Entity):
    def move(self):
        self.y += self.speed * 1
