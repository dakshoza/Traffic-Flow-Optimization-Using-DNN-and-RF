import pygame
from Car import Car

car1 = Car()
car1.hitbox = pygame.Rect(377,800,30,54)
car2 = Car()
car1.hitbox = pygame.Rect(388,700,30,54)

x = [car1, car2]
x.sort(key=lambda rect: rect.hitbox.y)

print(x)