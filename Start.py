import pygame
from Car import Car as Vehicle
from Intersections import *
pygame.init()
window = pygame.display.set_mode((1920,1080))        

running = True
background = pygame.image.load('./Assets/Background.png')
car1 = Vehicle(7)

while running:
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            wait = True
            while wait:
                if event.type == pygame.KEYUP:
                    wait = False
    # window color
    window.fill((81,81,81))
    window.blit(background,(0,0))

    #Car movement and hitboxes
    car1.moveCar()
    car1.drawCar(window)
    car1.drawHitbox(window)
    for i in Intersections:
        pygame.draw.rect(window, (255, 255, 0), i.hitbox, 3)

    #collision detection
    # for i in Intersections:
    #     # checking x coordinates
    #     if i.hitbox[0] + i.hitbox[2] 
    if car1.y <= 282:
        car1.changeOri("ltr")

    print(car1.orientation)
    pygame.display.update()