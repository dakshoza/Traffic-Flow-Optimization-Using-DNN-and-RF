import random, pygame
from Graphing import getPath
from math import sqrt
from Roads import SignalRoads, speed

currentCars = []

class Car:
    def __init__(self, spawnpoint):

    #Sprite Loading
        self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{random.randint(1, 6)}.png")

        # spawnpoint = 5
        self.hitbox = self.sprite.get_rect()    
        SignalRoads[spawnpoint].addCar(self)
        '''
            This biases the spawning so that there is a :
            - 1 in 11 chance for it to spawn at 1
            - 6 in 11 chance for it to spawn on the main road.
            - 2 in 11 chance for it to spawn on road 3 to simulate a busier side road
            - 2 in 11 chance for it to spawn on the right side
        '''
    #Path Generation
        #Basic Path
        destinations = [i for i in range(6)]
        destinations.remove(spawnpoint)
        endpoint = random.choice(destinations)
        path = getPath(spawnpoint, endpoint)[2:]        

        #Waypoints
        if len(path) == 1:
            self.waypoint = [random.choice(SignalRoads[path.pop(0)].Waypoint)]
        else:
            self.waypoint = [random.choice(SignalRoads[path.pop(1)].Waypoint)]
            lanes = SignalRoads[path.pop(0)].Waypoint
            x1, y1 = lanes[0]
            x2, y2 = lanes[1]
            x3, y3 = self.waypoint[0]
            if (sqrt((x3-x1)**2 + (y3-y1)**2) < sqrt((x3-x2)**2 + sqrt((y3-y2)**2))):
                self.waypoint.insert(0, lanes[0])
            else:
                self.waypoint.insert(0, lanes[1])

    #Spawning
        #Picking Closer lane
        x1, y1 = SignalRoads[spawnpoint].Spawnpoint[0]
        x2, y2 = SignalRoads[spawnpoint].Spawnpoint[1]
        x3,y3 = self.waypoint[0]
        if (sqrt((x3-x1)**2 + (y3-y1)**2) < sqrt((x3-x2)**2 + (y3-y2)**2)):
            tempx, tempy = SignalRoads[spawnpoint].Spawnpoint[0]
        else:
            tempx, tempy = SignalRoads[spawnpoint].Spawnpoint[1]
        
        self.CDR(SignalRoads[spawnpoint], (tempx, tempy))

        # Check Queue:
        for car in SignalRoads[spawnpoint].spawnQ:
            if self.hitbox.colliderect(car.hitbox):
                SignalRoads[spawnpoint].spawnQ.append(self)
    
    def CDR(self, road, currentCoord): # Centering, Direction and Rotation
        tempx,tempy = currentCoord
        if road.orientation == 3:
            self.dx = speed
            self.dy = 0
            self.sprite = pygame.transform.rotate(self.sprite,270)
            self.hitbox = self.sprite.get_rect()
            self.hitbox.centery = tempy
            self.hitbox.right = tempx

        elif road.orientation == 2:
            self.dx = -speed
            self.dy = 0
            self.sprite = pygame.transform.rotate(self.sprite,90)
            self.hitbox = self.sprite.get_rect()
            self.hitbox.left = tempx
            self.hitbox.centery = tempy

        elif road.orientation == 0:
            self.dx = 0
            self.dy = -speed
            self.hitbox = self.sprite.get_rect()
            self.hitbox.centerx = tempx
            self.hitbox.top = tempy
        else:
            self.dx = 0
            self.dy = speed
            self.sprite = pygame.transform.rotate(self.sprite,180)
            self.hitbox = self.sprite.get_rect()
            self.hitbox.bottom = tempy
            self.hitbox.centerx = tempx

    def drive(self):
        self.hitbox.x += self.dx
        self.hitbox.y += self.dy

    def render(self, screen):
        screen.blit(self.sprite, (self.hitbox.x,self.hitbox.y))