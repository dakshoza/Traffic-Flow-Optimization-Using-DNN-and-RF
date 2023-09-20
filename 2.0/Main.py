import pygame, random
from Cars import *

window = pygame.display.set_mode((1050,844))

def genCars(num):
    # global currentCars
    if len(currentCars) < 100:
        for i in range(num):
            spawnpoint = random.choice([0,1,1,1,2,2,3,4,4,4,5])
            if len(SignalRoads[spawnpoint].spawnQ) > 0:
                currentCars.append(SignalRoads[spawnpoint].spawnQ[0])
            else:
                newCar = Car(spawnpoint)
                #check if any collision was found on spawn
                if not newCar.hitbox.collidelistall([car.hitbox for car in SignalRoads[spawnpoint].queue]):
                    currentCars.append(newCar)
                else:
                    SignalRoads[spawnpoint].spawnQ.append(newCar)



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
        if len(road.spawnQ) >0:
            if not road.spawnQ[0].hitbox.collidelistall([car.hitbox for car in road.queue]):
                currentCars.append(road.spawnQ[0])


    for car in currentCars:
        car.drive()
        car.render(window)

        # Deleting the cars
        if (car.hitbox.x < -50 or car.hitbox.x > 1100) or (car.hitbox.y < -50 or car.hitbox.y > 890):
            currentCars.remove(car)
            # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
            genCars(1)
        

    pygame.display.flip()
    