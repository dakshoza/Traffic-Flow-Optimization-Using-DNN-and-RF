import pygame, random
from Cars import *

window = pygame.display.set_mode((1050,844))

def genCars(num):
    # global currentCars
    if len(currentCars) <= 100:
        for i in range(num):
            collision = False
            while True:
                newCar = Car()
                for car in currentCars:
                    if newCar.hitbox.colliderect(car.hitbox):
                        collision = True

                if not collision:
                    currentCars.append(Car())
                    break


background = pygame.image.load("Assets/background.png")

running = True

genCars(5)

while running:
    window.blit(background,(0,0))
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for road in SignalRoads.values():
        if len(road.queue) != 0:
            road.checkTurn()

    for car in currentCars:
        car.drive()
        car.render(window)

        # Deleting the cars
        if (car.hitbox.x < -50 or car.hitbox.x > 1100) or (car.hitbox.y < -50 or car.hitbox.y > 890):
            currentCars.remove(car)
            # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
            genCars(1)
        

    pygame.display.flip()
    