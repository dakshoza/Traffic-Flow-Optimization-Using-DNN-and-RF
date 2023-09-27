import csv, pygame
from Cars import *
from Env import Environment

window = pygame.display.set_mode((1050,844))

env = Environment()

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

background = pygame.image.load("Assets/background.png")

running = True

genCars(10)

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
                    env.getState()
                    
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

        pygame.display.flip()
        