import pygame, random
from Cars import *

window = pygame.display.set_mode((1050,844))

currentCars = []
def genCars(num):
    global currentCars
    if len(currentCars) <= 100:
        for i in range(num):
            currentCars.append(Car())

background = pygame.image.load("Assets/background.png")

running = True

genCars(6)

while running:
    window.blit(background,(0,0))
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for road in SignalRoads:
        road.checkTurn()

    for car in currentCars:
        car.drive()
        car.render(window)

        # Deleting the cars
        if (car.hitbox.x < -30 or car.hitbox.x > 1100) or (car.hitbox.y < -40 or car.hitbox.y > 890):
            currentCars.remove(car)
            genCars(random.choice([0,1,1,1,2,2,2,3,3]))

        #Checking waypoints wrt roads
        # try:
        #     pygame.draw.circle(window, (0,255,0), car.waypoint[0], 2)
        # except:
        #     continue
        

    pygame.display.flip()
    