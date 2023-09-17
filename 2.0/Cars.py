import random, pygame
from Graphing import *
from math import sqrt

Spawnpoints = {
    1: [(272,844), (317, 844)],
    2: [(0,346), (0, 391)],
    3: [(422, 0), (379, 0)],
    4: [(831, 0), (790, 0)],
    5: [(1050, 494), (1050, 452)],
    6: [(684, 844), (727, 844)]
}

class Car:
    def __init__(self):
    #Spawn Point & direction
        spawnpoint = random.choice([1,2,2,2,3,3,4,5,5,5,6])
        self.dx = 0
        if spawnpoint == 2:
            self.dx = 8
            self.dy = 0
        elif spawnpoint == 5:
            self.dx = -8
            self.dy = 0
        elif spawnpoint == 1 | spawnpoint == 6:
            self.dy = -8
        else:
            self.dy = 8
        
        '''
            This biases the spawning so that there is a :
            - 1 in 11 chance for it to spawn at 1
            - 6 in 11 chance for it to spawn on the main road.
            - 2 in 11 chance for it to spawn on road 3 to simulate a busier side road
            - 2 in 11 chance for it to spawn on the right side
        '''
    #Path Generation
        #Basic Path
        destinations = [i for i in range(1,7)]
        destinations.remove(spawnpoint)

        endpoint = random.choice(destinations)
        path = getPath(spawnpoint, endpoint)[2:]        

        #Waypoints
        if len(path) == 1:
            self.waypoint = [random.choice(Waypoints[path.pop(0)])]
        elif len(path) == 2:
            self.waypoint = [random.choice(Waypoints[path.pop(1)])]
            lanes = Waypoints[path.pop(0)]
            x1, y1 = lanes[0]
            x2, y2 = lanes[1]
            x3, y3 = self.waypoint[0]
            if (sqrt(float(x3-x1)**2 + float(y3-y1)**2) < sqrt(float(x3-x2)**2 + sqrt(float(y3-y2)**2))):
                self.waypoint.insert(0, lanes[0])
            else:
                self.waypoint.insert(0, lanes[1])

    #Sprite Loading
        self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{random.randint(1, 6)}.png")
        self.hitbox = self.sprite.get_rect()

    #Spawning
        self.hitbox.x, self.hitbox.y = random.choice(Spawnpoints[spawnpoint])
        #Finding first turn
    
    
    # def findWaypoints(path):

    # def turns():

    def drive(self):
        self.hitbox.x += self.dx
        self.hitbox.y += self.dy

    def render(self, screen):
        screen.blit(self.sprite, (self.hitbox.x,self.hitbox.y))

#testing
for i in range(12):
    x = Car()

