import csv, pygame
import numpy as np
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

genCars(4)

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
            if event.key == pygame.K_t:  # Toggle Signals
                for road in SignalRoads.values():
                    road.signalState = not road.signalState

    if not pauseSimulator:
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
            for wp in road.Waypoint:
                pygame.draw.circle(window,(255,0,0),wp, 5)

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
                except:
                    pass
                # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
                genCars(1)


        # for car in TurningCars:
        #     car.drive()

        pygame.display.flip()
        