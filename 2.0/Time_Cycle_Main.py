import pygame
import time
from Cars import *

window = pygame.display.set_mode((1050,844))

def genCars(num):
    if len(currentCars) < 100:
        for i in range(num):
            spawnpoint = random.choice([0,1,1,1,2,2,3,4,4,4,5])
            # spawnpoint = random.choice([2,3,0,5])
            spawnRoad = SignalRoads[spawnpoint]
        
            newCar = Car(spawnpoint)
            #check if any collision was found on spawn
            if len(newCar.rect.collidelistall([car.rect for car in spawnRoad.queue]))>0:
                if len(spawnRoad.spawnQ) <10:
                    spawnRoad.spawnQ.append(newCar)
            else:
                currentCars.append(newCar)
                spawnRoad.queue.append(newCar)

background = pygame.image.load("Assets/background.png")

crossroad1 = Crossroads[0]
crossroad2 = Crossroads[1]

currentSignalIndex = 0
signalTimer = 0

crossroad1[currentSignalIndex].signalState = True
crossroad2[currentSignalIndex].signalState = True

clock = pygame.time.Clock()

startTime = time.time()

score = 0

running = True

timeframe = 0

genCars(21)

# for Road in SignalRoads.values():
#     Road.signalState = True

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
                road.spawnQ[0].drive(4)
                if len(road.spawnQ[0].rect.collidelistall([car.rect for car in road.queue]))==0:
                    road.spawnQ[0].drive(-4)
                    road.queue.append(road.spawnQ[0])
                    currentCars.append(road.spawnQ.pop(0))
                else:
                    road.spawnQ[0].drive(-4)

            # print(road.distanceToClosestCar)

    signalTimer += clock.tick(60) / 1000

    if signalTimer >= 3.5:
        currentSignalIndex = (currentSignalIndex + 1) % 4
        for index in range(4):
            crossroad1[index].signalState = False
            crossroad2[index].signalState = False
        crossroad1[currentSignalIndex].signalState = True
        crossroad2[currentSignalIndex].signalState = True
        signalTimer = 0

    for car in TurningCars:
        car.turn()

    for car in ExitingCars:
        car.drive()

    for car in currentCars:
        car.render(window)

        # Deleting the cars
        if (car.rect.x < -150 or car.rect.x > 1200) or (car.rect.y < -150 or car.rect.y > 990):
            try:
                currentCars.remove(car)
            except:
                pass
            try:
                TurningCars.remove(car)
            except:
                pass
            try:
                ExitingCars.remove(car)
                score += 1
            except:
                pass
            # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
            genCars(1)

    elapsedTime = time.time() - startTime
    
    if elapsedTime >= 60:
        print(f"Score : {score}")
        print(timeframe)
        running = False

    for road in SignalRoads.values():
        pygame.draw.rect(window, (0,0,0,200), road.signal)
        if not road.signalState:
            pygame.draw.circle(window,(255,0,0), road.signal.center, 5)
        else:
            pygame.draw.circle(window,(0,255,0), road.signal.center, 5)

    timeframe += 1


    pygame.display.flip()
        