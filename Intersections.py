import pygame
import Car
from Roads import allRoads

class Intersection:
    def __init__(self, x, y, width, height):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.center = (round((x+width)/2), round((y+height)/2))

    def carCollision(self, carlist):
        if self.hitbox.collidelist(carlist) >= 0:
            print(self.hitbox.collidelist(carlist))

I1 = Intersection(252,326,192,192)
I2 = Intersection(662,325,192,192)

Intersections = [I1, I2]