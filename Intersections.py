import pygame
import Car
from Roads import allRoads

class Intersection:
    def __init__(self, x, y, width, height):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.center = (round((x+width)/2), round((y+height)/2))
       # self.distancetravelled = 0

    def carCollisionWithIntersection(self, cars):
        carHitboxes = [car.hitbox for car in cars]
        carsInIntersection = self.hitbox.collidelistall(carHitboxes)
        if carsInIntersection != []:
            print(self.hitbox.collidelistall(carHitboxes))
           # self.distancetravelled += 1
            
            #self.turnInIntersection(cars)
        else:
            print("Not colliding")
        
    def turnInIntersection(self,cars):
        pass
        

I1 = Intersection(252,326,192,192)
I2 = Intersection(662,325,192,192)

Intersections = [I1, I2]