import random
class Car:
    def __init__(self, spawnLocation):
        self.spawnLocation = spawnLocation
        #Generating Car Path
        self.carPath = []
        self.carPath.append(random.randint(0,2))
        self.carPath.append(random.randint(0,1))
        self.carPath.append(random.randint(0,2))
                        
        
        #Car Spawn
        if self.spawnLocation == 1:
                self.x = -20
                self.y = 248
        elif self.spawnLocation ==2:
                self.x = 228
                self.y = -20
        elif self.spawnLocation ==3:
                self.x = 760
                self.y = -20
        elif self.spawnLocation ==4:
                self.x = 228
                self.y = -20
        elif self.spawnLocation ==5:
                self.x = 715
                self.y = 560
        elif self.spawnLocation ==6:
                self.x = 440
                self.y = 560
                del self.carPath[0]
        elif self.spawnLocation ==7:
                self.x = 183
                self.y = 560
        
    def moveCar(self):
           IntersectionCoordinates = []

# car1 = Car()
# print(f"SpawnLocation = {car1.spawnLocation}\nX = {car1.x}\nY = {car1.y}")