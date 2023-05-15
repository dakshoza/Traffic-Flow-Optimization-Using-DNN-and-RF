import pygame
pygame.init()
window = pygame.display.set_mode((960,540))

# class car:
#     def __init__(self,spawnLocation):

running = True
background = pygame.image.load('BG1.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((81,81,81))
    window.blit(background,(0,0))


    pygame.display.update()