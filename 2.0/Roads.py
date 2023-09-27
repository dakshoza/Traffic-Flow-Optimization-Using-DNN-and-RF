import pygame
from pygame import Vector2 as v2

speed = 4
TurningCars = []
currentCars = []
class Road:
# Have to define all road bounds

    def __init__(self, orientation, IBoundary, Waypoint, Spawnpoint=[]):
        self.orientation = orientation # 0 for up, 1: down, 2: left, 3: right
        self.IBoundary = IBoundary # Intersection Boundary
        self.Spawnpoint = Spawnpoint
        self.Waypoint= Waypoint
        self.queue = []
        self.popWait = 0
        self.spawnQ = []
        self.signalState = False
        self.distanceToClosestCar = 1000 # For the AI model, distance to the first car in queue

    # queue length can straight up be pulled from the models

    # def calcTrafficDensity(self):
        # We make a dictionary with all the roads and their respective queueAmount, then do self.queueAmount/sum(dict.values()) to get a ratio 
        # self.trafficDensity = len(self.queue)/len(currentCars)

    
    def popCar(self, Car):
        # Removing car from queue
        TurningCars.append(Car)
        Car.rotate()
        self.queue.remove(Car)
        # Resorting queue
        if (self.orientation == 0) or (self.orientation == 1):
            self.queue = sorted(self.queue, key=lambda car: abs(self.IBoundary - car.rect.y))
        else:
            self.queue = sorted(self.queue, key=lambda car: abs(self.IBoundary - car.rect.x))

    def checkTurn(self): #REAL ONE
        #If Signal Is on
        if self.signalState:
            for car in self.queue:
                car.drive()
                # If it crossed the boundary:
                if self.orientation in [2,3]:
                    if len(car.rect.clipline((self.IBoundary,0),(self.IBoundary,844))) != 0:
                        if self.popWait == 0:
                            self.popCar(car)
                            self.popWait == 15
                        else: 
                            self.popWait -=1
                else:
                    if len(car.rect.clipline((0,self.IBoundary),(1050,self.IBoundary))) != 0:
                        if self.popWait == 0:
                            self.popCar(car)
                            self.popWait == 15
                        else: 
                            self.popWait -=1
        #If Signal off
        else:
            for car in self.queue:
                #If next won't move will exit/collide:
                car.drive(2)
                if self.orientation in [2,3]:
                    if (len(car.rect.clipline((self.IBoundary,0),(self.IBoundary,844))) == 0) and (len(car.rect.collidelistall([a.rect for a in self.queue])) <=1):
                        car.drive()
                else:
                    if (len(car.rect.clipline((0,self.IBoundary),(1050,self.IBoundary))) == 0) and (len(car.rect.collidelistall([a.rect for a in self.queue])) <=1):
                        car.drive()
                car.drive(-2)

        self.calculateDistanceToClosestCar()

    def calculateDistanceToClosestCar(self):
        if len(self.queue)==0:
            self.distanceToClosestCar == 1000
        else:
            try:
                if (self.orientation == 0):
                    #for a car, its distance from the intersection is calculated to feed to the ai model
                    self.distanceToClosestCar = self.queue[0].rect.top - self.IBoundary
                    
                elif (self.orientation == 1):
                    #for a car, its distance from the intersection is calculated to feed to the ai model
                    self.distanceToClosestCar = self.IBoundary - self.queue[0].rect.bottom 
                    
                elif self.orientation == 2:
                    #for a car, its distance from the intersection is calculated to feed to the ai model
                    self.distanceToClosestCar = self.queue[0].rect.left - self.IBoundary

                else:
                    #for a car, its distance from the intersection is calculated to feed to the ai model
                    self.distanceToClosestCar = self.IBoundary - self.queue[0].rect.right
            except:
                pass



SignalRoads = {
    0 : Road(0,520, Spawnpoint= [(272,844), (317, 844)], Waypoint =[(422,519), (377,520)]),
    1 : Road(3,247, Spawnpoint= [(0,346), (0, 391)], Waypoint =[(247,497), (247,455)]),
    2 : Road(1,321, Spawnpoint= [(422, 0), (379, 0)], Waypoint =[(273,321), (316,321)]),
    3 : Road(1,322, Spawnpoint= [(831, 0), (790, 0)], Waypoint =[(682,322), (726,322)]),
    4 : Road(2,857, Spawnpoint= [(1050, 494), (1050, 452)], Waypoint =[(857,348), (857,390)]),
    5 : Road(0,520, Spawnpoint= [(684, 844), (727, 844)],Waypoint =[(833,520), (788,520)]),
    "I1" : Road(3,445, Waypoint =[(659,494), (659, 451)]),
    "I2" : Road(2,659, Waypoint =[(445,348 ), (445,388)])
}


Crossroads = {
    0 : [SignalRoads[0], SignalRoads[1], SignalRoads[2], SignalRoads['I1']],
    1 : [SignalRoads[3], SignalRoads[4], SignalRoads[5], SignalRoads["I2"]]
}