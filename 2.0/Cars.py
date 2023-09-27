import random, pygame, math
from Graphing import getPath
from math import sqrt
from Roads import *
from pygame import Vector2


ExitingCars = []
class Car():
    def __init__(self, spawnpoint):
    #Sprite Loading
        self.spriteNumber = random.randint(1, 6)
        self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")

        # spawnpoint = 5
        self.rect = self.sprite.get_rect
        '''
            This biases the spawning so that there is a :
            - 1 in 11 chance for it to spawn at 1
            - 6 in 11 chance for it to spawn on the main road.
            - 2 in 11 chance for it to spawn on road 3 to simulate a busier side road
            - 2 in 11 chance for it to spawn on the right side
        '''
    #Path Generation
        #Basic Path
        if spawnpoint in [0,1,2]:
            destinations = [0,0,1,1,2,2,3,4,5]
            destinations.remove(spawnpoint)
            destinations.remove(spawnpoint)
        else:
            destinations = [0,1,2,3,3,4,4,5,5]
            destinations.remove(spawnpoint)
            destinations.remove(spawnpoint)
        endpoint = random.choice(destinations)
        path = getPath(spawnpoint, endpoint)[2:]  
        self.roads = getPath(spawnpoint, endpoint)[2:]     
        # print(path)
        # print(self.roads)
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

        # self.waitTime = 0


    
    def CDR(self, road, currentCoord): # Centering, Direction and Rotation
        tempx,tempy = currentCoord
        if road.orientation == 3:
            self.dx = speed
            self.dy = 0
            self.sprite = pygame.transform.rotate(self.sprite,270)
            self.rect = self.sprite.get_rect()
            self.rect.centery = tempy
            self.rect.right = tempx

        elif road.orientation == 2:
            self.dx = -speed
            self.dy = 0
            self.sprite = pygame.transform.rotate(self.sprite,90)
            self.rect = self.sprite.get_rect()
            self.rect.left = tempx
            self.rect.centery = tempy

        elif road.orientation == 0:
            self.dx = 0
            self.dy = -speed
            self.rect = self.sprite.get_rect()
            self.rect.centerx = tempx
            self.rect.top = tempy
        else:
            self.dx = 0
            self.dy = speed
            self.sprite = pygame.transform.rotate(self.sprite,180)
            self.rect = self.sprite.get_rect()
            self.rect.bottom = tempy
            self.rect.centerx = tempx

    def drive(self, times=1):
        self.rect.x += times*self.dx
        self.rect.y += times*self.dy

    def turn(self):
        pos = Vector2(self.rect.centerx, self.rect.centery)
        waypoint = Vector2(self.waypoint[0])
        direction = waypoint - pos
        distance = direction.length()

        #If it's gonna overshoot
        if distance < speed:
            newRoad = SignalRoads[self.roads.pop(0)]
            #Add to Intersection roads
            if newRoad == SignalRoads["I1"] or newRoad == SignalRoads["I2"]:
                newRoad.queue.append(self)
            else:
                ExitingCars.append(self)

            
            #Change movement Vector
            if newRoad.orientation ==0:
                if self.dx !=0 and self.dy != speed:
                    self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")
                    self.dx = 0            
                    self.dy = speed
                    self.sprite = pygame.transform.rotate(self.sprite, 180) 
                    self.rect = self.sprite.get_rect()
                #Clip to waypoint 
                    self.rect.center = (self.waypoint[0][0], self.rect.y)
                    self.rect.bottom = self.waypoint[0][1]
            elif newRoad.orientation == 1:
                if self.dx !=0 and self.dy != -speed:
                    self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")
                    self.dx = 0            
                    self.dy = -speed
                    self.rect = self.sprite.get_rect()
                    self.rect.center = (self.waypoint[0][0], self.rect.y)
                    self.rect.top = self.waypoint[0][1]
            elif newRoad.orientation == 2:  
                if self.dx !=speed and self.dy != 0:
                    self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")
                    self.dx = speed         
                    self.dy = 0
                    self.sprite = pygame.transform.rotate(self.sprite, 270)
                    self.rect = self.sprite.get_rect()
                    self.rect.center = (self.rect.x, self.waypoint[0][1])
                    self.rect.right = self.waypoint[0][0]
            else:  
                if self.dx != -speed and self.dy != 0:
                    self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")
                    self.dx = -speed          
                    self.dy = 0
                    self.sprite = pygame.transform.rotate(self.sprite, 90)
                    self.rect = self.sprite.get_rect()
                    self.rect.center = (self.rect.x, self.waypoint[0][1])
                    self.rect.left = self.waypoint[0][0]
            self.waypoint.pop(0)
            TurningCars.remove(self)
        # Still turning
        else: 
            direction = direction.normalize()
            self.rect.x += direction.x * speed
            self.rect.y += direction.y * speed

    def rotate(self):
        pos = Vector2(self.rect.center)
        oldpos = (self.rect.x, self.rect.y)
        destination = Vector2(self.waypoint[0])
        distanceVector = destination-pos
        angle = math.degrees(math.atan2(-distanceVector[1], distanceVector[0]))
        self.sprite = pygame.image.load(f"./Assets/CarSprites/CarSprite{self.spriteNumber}.png")
        self.sprite = pygame.transform.rotate(self.sprite, angle+270)
        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = oldpos

    def render(self, screen):
        screen.blit(self.sprite, (self.rect.x,self.rect.y))

    # def collisionPredict(self, road):