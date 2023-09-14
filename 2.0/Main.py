import pygame
from Cars import *

window = pygame.display.set_mode((1050,844))

currentCars = []
def genCars(num):
    global currentCars
    for i in range(num+1):
        currentCars.append(Car())

background = pygame.image.load("Assets/background.png")

running = True

while running:
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(background,(0,0))
    pygame.display.update()
    