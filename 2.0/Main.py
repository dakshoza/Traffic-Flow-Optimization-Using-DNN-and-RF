import pygame, random, csv
import numpy as np
from Cars import *

window = pygame.display.set_mode((1050,844))
currentCars = pygame.sprite.Group()

def genCars(num):
    # global currentCars
    if len(currentCars) < 100:
        for i in range(num):
            spawnpoint = random.choice([0,1,1,1,2,2,3,4,4,4,5])
            # spawnpoint = random.choice([2,3])
            spawnRoad = SignalRoads[spawnpoint]
            if len(spawnRoad.spawnQ) > 0:
                currentCars.add(spawnRoad.spawnQ[0])
            else:
                newCar = Car(spawnpoint)
                #check if any collision was found on spawn
                if len(pygame.sprite.spritecollide(newCar,currentCars,False,pygame.sprite.collide_rect_ratio(1.3)))>=0:
                    currentCars.add(newCar)
                    spawnRoad.queue.append(newCar)
                else:
                    spawnRoad.spawnQ.append(newCar)

pauseSimulator = False

def append_to_csv(file_name, data):
    try:
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print("Data appended to", file_name)
    except Exception as e:
        print("Error appending data to", file_name)
        print(e)


def addToTrainingData():
    # waitingTimes = []
    trafficDensities = np.zeros(6)
    queueLengths = np.zeros(6)
    distancesToClosestCars = np.zeros(6)

    for index in range(6):
        queueLengths[index] = len(SignalRoads[index].queue)
        distancesToClosestCars[index] = SignalRoads[index].distanceToClosestCar

    trafficDensities = queueLengths/np.sum(queueLengths)

    training_example = np.concatenate((trafficDensities, queueLengths, distancesToClosestCars))
    
    print(training_example)

    append_to_csv('2.0\TrainingDataset.csv', training_example)

background = pygame.image.load("Assets/background.png")

running = True

genCars(5)

while running:
    window.blit(background,(0,0))
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Toggle pause on "P" key press
                pauseSimulator = not pauseSimulator
                if pauseSimulator == True:
                    addToTrainingData()

    if not pauseSimulator:

        for road in SignalRoads.values():
            if len(road.queue) != 0:
                road.checkTurn()
                if len(road.spawnQ) >0:
                    road.spawnQ[0].drive(4)
                    if not road.spawnQ[0].rect.collidelistall([car.rect for car in road.queue]):
                        road.spawnQ[0].drive(-4)
                        currentCars.append(road.spawnQ.pop(0))
                    else:
                        road.spawnQ[0].drive(-4)


        for car in currentCars:
            car.drive()
            car.render(window)

            # Deleting the cars
            if (car.rect.x < -50 or car.rect.x > 1100) or (car.rect.y < -50 or car.rect.y > 890):
                currentCars.remove(car)
                # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
                genCars(1)

        pygame.display.flip()
        