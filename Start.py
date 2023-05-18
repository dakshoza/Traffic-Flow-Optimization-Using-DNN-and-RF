import pygame
from Car import Car as Vehicle
from Roads import *
pygame.init()
window = pygame.display.set_mode((1500,844))        

running = True 
background = pygame.image.load('./Assets/Background1500.png')
car1 = Vehicle()
while running:
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # window color
    window.fill((81,81,81))
    window.blit(background,(0,0))

    # Hitboxes
    car1.moveCar()
    car1.drawCar(window)
    car1.drawHitbox(window)
    for road in allRoads:
        road.drawHitBox(window)

    pygame.display.update()