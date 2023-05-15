import pygame
import random
pygame.init()
window = pygame.display.set_mode((960,540))

class car:
    def __init__(self,spawnLocation):
        
        #Generating Car Path
        self.carPath = []
        self.carPath.append(random.randint(0,2))
        self.carPath.append(random.randint(0,1))
        self.carPath.append(random.randint(0,2))
                        
        
        #Car Spawn
        if spawnLocation == 1:
                self.x = -20
                self.y = 248
        elif spawnLocation ==2:
                self.x = 228
                self.y = -20
        elif spawnLocation ==3:
                self.x = 760
                self.y = -20
        elif spawnLocation ==4:
                self.x = 228
                self.y = -20
        elif spawnLocation ==5:
                # self.x = 228
                self.y = 560
        elif spawnLocation ==6:
                self.x = 228
                self.y = 560
                del self.carPath[0]
        elif spawnLocation ==7:
                self.x = 182
                self.y = 560
        

running = True
background = pygame.image.load('BG1.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((81,81,81))
    window.blit(background,(0,0))


    pygame.display.update()