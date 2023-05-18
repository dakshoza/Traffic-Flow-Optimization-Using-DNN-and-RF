import pygame
class Road:
    def __init__(self, x, y, width, height):
        self.boundaries = (x, y, width, height)
        if width < height: 
            self.laneWidth = round((width-4)/2)
        else: 
            self.laneWidth = round((height - 4)/2)
        self.freeSpace = int((self.laneWidth-30)/2)
        
    def drawHitBox(self, window):
        pygame.draw.rect(window,(0,0,255),self.boundaries,2)

road1 = Road(0, 325, 251, 87)
road2 = Road(251, 0, 86,325)
road3 = Road(356,0,87,325)
road4 = Road(1058,0,86,325)
road5 = Road(1163, 0, 87, 325)
road6 = Road(1250,325,250,87)
road7 = Road(1250,431,250,85)
road8 = Road(1163,517,87,327)
road9 = Road(1058,517,85,327)
road10 = Road(767,517,87,327)
road11 = Road(662,517,86,327)
road12 = Road(355,517,88,327)
road13 = Road(251,517,86,327)
road14 = Road(0,431,251,86)
road15 = Road(443,325,219,87)
road16 = Road(443,431,219,87)
road17 = Road(854,325,204,87)
road18 = Road(854,431,204,86)

allRoads = [road1, 
            road2,road3,
            road4,road5,
            road6,road7,
            road8,road9,
            road10,road11,
            road12,road13,
            road14,
            road15,road16,
            road17,road18]