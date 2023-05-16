import pygame
from Car import Car as Vehicle
pygame.init()
window = pygame.display.set_mode((960,540))
CarSprite = pygame.image.load("./Assets/CarSprites/CarSprite1.png")        

running = True
background = pygame.image.load('./Assets/BG1.png')
car1 = Vehicle(7)
car1.x -= 15
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            wait = True
            while wait:
                if event.type == pygame.KEYUP:
                    wait = False
    window.fill((81,81,81))
    window.blit(background,(0,0))
    
    car1.y -= 1.5
    # print(f"({car1.x}, {car1.y})")
    # window.blit(CarSprite, (car1.x, car1.y))

    pygame.display.update()