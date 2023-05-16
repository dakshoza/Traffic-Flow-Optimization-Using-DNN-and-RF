import random
import pygame
class Car:
    def __init__(self, spawnLocation):
        sprite = pygame.image.load("./Assets/CarSprites/CarSprite1.png")
        self.spawnLocation = spawnLocation
        self.sprite = sprite
        self.hitbox = []
        self.speed = 1.5
        
        #Generating Car Path
        self.carPath = []
        self.carPath.append(random.randint(0,2))
        self.carPath.append(random.randint(0,1))
        self.carPath.append(random.randint(0,2))
                        
        
        #Car Spawn
        if self.spawnLocation == 1:
                self.x = -20
                self.y = 248
                self.orientation = "rtl" #right to left
        elif self.spawnLocation ==2:
                self.x = 228
                self.y = -20
                self.orientation = "ttb" #top to bottom
        elif self.spawnLocation ==3:
                self.x = 760
                self.y = -20
                self.orientation = "ttb" #top to bottom
        elif self.spawnLocation ==4:
                self.x = 228
                self.y = -20
                self.orientation = "ltr" #Left to right
        elif self.spawnLocation ==5:
                self.x = 715
                self.y = 560
                self.orientation = "btt" #bottom to top
        elif self.spawnLocation ==6:
                self.x = 440
                self.y = 560
                self.orientation = "btt" #bottom to top
                del self.carPath[0]
        elif self.spawnLocation ==7:
                self.x = 170
                self.y = 560
                self.orientation = "btt" #bottom to top
        self.hitbox = [self.x,self.y, 20, 33] #top left x, top left y, width, height

    def drawCar(self, window):
        window.blit(self.sprite, (self.x, self.y))

    def changeOri(self, newOri):
           if newOri == "btt":
                  self.hitbox = [self.x, self.y, 20, 33]
           elif newOri == "ttb":
                  self.hitbox = [self.x, self.y, 20, -33]                  
           elif newOri == "ltr":
                  self.hitbox = [self.x, self.y, 33, 20]                  
           elif newOri == "rtl":
                  self.hitbox = [self.x, self.y, -33, 20]                  
                  
        
    def moveCar(self):
           if self.orientation == "btt":
                  self.y -= self.speed
           elif self.orientation == "ttb":
                  self.y += self.speed
           elif self.orientation == "ltr":
                  self.x += self.speed
           elif self.orientation == "rtl":
                  self.x -= self.speed
           self.hitbox = [self.x,self.y, 20, 33] #top left x, top left y, width, height

    def drawHitbox(self, window):
           pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)
           print(self.hitbox)
# car1 = Car()
# print(f"SpawnLocation = {car1.spawnLocation}\nX = {car1.x}\nY = {car1.y}")