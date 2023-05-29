import pygame
import random
from TrafficSignals import *
class Road:
    def __init__(self, x, y, width, height):
        self.boundaries = pygame.Rect(x, y, width, height)
        if width < height: 
            self.laneWidth = int(round((width-4)/2))
        else: 
            self.laneWidth = int(round((height - 4)/2))
        self.freeSpace = int((self.laneWidth-30)/2)
        self.carList = []
        self.state = 0 
        self.waitingTime = 0
        
    def drawHitBox(self, window):
        pygame.draw.rect(window,(0,0,255),self.boundaries,2)

    def blitCoordinate(self,spawnLocation, carPath):
        if spawnLocation == 1 or spawnLocation == 2:
            if carPath[0] == 0:
                # if carPath[1] == 2:
                #         x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                # else:
                x = int(self.boundaries[0] + self.freeSpace)
            # elif carPath[0] == 2:
            #     x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
            else:
                x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
        elif spawnLocation == 3:
            if carPath[0] == 0:
                x = int(self.boundaries[1] + self.freeSpace)
            elif carPath[0] == 1:
                if carPath[1] == 0:
                    x = int(self.boundaries[1] + self.freeSpace)    
                else:
                    x = int(self.boundaries[1] + self.laneWidth + 4 + self.freeSpace)
            else:
                x = int(self.boundaries[1] +self.laneWidth + 4 + self.freeSpace)
        
        else:
            if self.boundaries[2] < self.boundaries[3] :
                if carPath[0] == 0:
                    x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                elif carPath[0] == 1:
                    x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                else:
                    x = int(self.boundaries[0] + self.freeSpace)
                        
            elif self.boundaries[2] >= self.boundaries[3]: 
                if carPath[0] == 0:
                    # if carPath[1] == 2:
                    #x = int(self.boundaries[1] + self.freeSpace)
                    # else:
                    x = int(self.boundaries[1] + self.laneWidth + 4 + self.freeSpace)
                elif carPath[0] == 1:
                    if carPath[1] == 0:
                        x = int(self.boundaries[1] + self.laneWidth + 4 + self.freeSpace)
                    else:
                        x = int(self.boundaries[1] + self.freeSpace)    
                else:
                    x = int(self.boundaries[1] + self.freeSpace)
        return x
        
    def update(self):
        if self.signal.state == 0:
            self.signal.state = 1
        else: 
            self.signal.state = 0
            
    def stopPosition(self, car):
        if car in self.lane1List:
            carPos = self.lane1List.index(car)
        elif car in self.lane2List:
            carPos = self.lane2List.index(car)
        if self.direction == "left":
            self.carList.sort(key=lambda rect: rect.hitbox.x)
            x = self.boundaries.x
            return (10 + x + (60*carPos))
        elif self.direction == "right":
            self.carList.sort(key=lambda rect: rect.hitbox.x, reverse=True)
            x = self.boundaries.x + self.boundaries.width
            return (x - 10 - 52 - (60*carPos))
        elif self.direction == "up":
            self.carList.sort(key=lambda rect: rect.hitbox.y, reverse=True)
            y = self.boundaries.y
            return (y + 10 + (60*carPos))  
        elif self.direction == "down":
            self.carList.sort(key=lambda rect: rect.hitbox.y)
            y = self.boundaries.y + self.boundaries.height
            return (y - 52 - 10 - (60*carPos))
        
            
        
        
road1 = Road(767,517,87,327)
road2 = Road(662,517,87,327)
road3 = Road(355,517,87,327)
road4 = Road(251,517,87,327)
road5 = Road(0,431,251,87)
road6 = Road(0, 325, 251, 87)
road7 = Road(251, 0, 87,325)
road8 = Road(356,0,87,325)
road9 = Road(443,325,219,87)
road10 = Road(443,431,219,87)
road11 = Road(854,325,196,87)
road12 = Road(854,431,196,87)

road4.signal = A0
road6.signal = A1
road8.signal = A2
road10.signal = A3
road2.signal = B0
road9.signal = B1
road12.signal = B2

road4.direction = "up"
road6.direction = "right"
road8.direction = "down"
road10.direction = "left"
road2.direction = "up"
road9.direction = "right"
road12.direction = "left"

monitoredRoads = [road4,road6,road8,road10,road2,road9,road12,]

allRoads = [road1, 
            road2,road3,
            road4,road5,
            road6,road7,
            road8,road9,
            road10,road11,
            road12]

signalRoads = [road.boundaries for road in monitoredRoads]
