import pygame
import Car_old
from Roads_old import allRoads

class Intersection:
    def __init__(self, x, y, width, height):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.center = (round((x+width)/2), round((y+height)/2))
       # self.distancetravelled = 0

I1 = Intersection(251,325,192,192)
I2 = Intersection(662,325,192,192)

Intersections = [I1, I2]