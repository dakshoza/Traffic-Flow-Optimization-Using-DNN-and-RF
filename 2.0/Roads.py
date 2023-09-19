from collections import deque

speed = 2
class Road:
# Have to define all road bounds

    def __init__(self, orientation, IBoundary, Waypoint, Spawnpoint=[]):
        self.orientation = orientation # 0 for up, 1: down, 2: left, 3: right
        self.IBoundary = IBoundary # Intersection Boundary
        self.Spawnpoint = Spawnpoint
        self.Waypoint= Waypoint
        self.queue = deque()
        self.trafficDensity = 0 # The traffic density for this road

    def calcTrafficDensity(self):
    # We make a dictionary with all the roads and their respective queueAmount, then do self.queueAmount/sum(dict.values()) to get a ratio 
        pass
    
    def addCar(self, Car):
        self.queue.append(Car)
    
    def popCar(self, Car):
        # Removing car from queue
        self.queue.popleft()
        print(f"{Car} removed from queue, headed {self.orientation}")
        # Resorting queue to make sure no overtaking has been done
        if (self.orientation == 0) or (self.orientation == 1):
            self.queue = sorted(self.queue, key=lambda car: abs(self.IBoundary - car.hitbox.y))
        else:
            self.queue = sorted(self.queue, key=lambda car: abs(self.IBoundary - car.hitbox.x))
        

    def checkTurn(self):
        try:
            if (self.orientation == 0):
                if (self.queue[0].hitbox.top - speed) <= self.IBoundary:
                    self.popCar(self.queue[0])
                    pass # Tell car to turn function
            elif (self.orientation == 1):
                if (self.queue[0].hitbox.bottom + speed) >= self.IBoundary:
                    self.popCar(self.queue[0])
                    pass # Tell car to turn function
            elif self.orientation == 2:
                if (self.queue[0].hitbox.left - speed) <= self.IBoundary:
                    self.popCar(self.queue[0])
                    pass # Tell car to turn function
            else:
                if (self.queue[0].hitbox.right + speed) >= self.IBoundary:
                    self.popCar(self.queue[0])
                    pass # Tell car to turn function
        except:
            pass


SignalRoads = {
    0 : Road(0,520, Spawnpoint= [(272,844), (317, 844)], Waypoint =[(422,519), (377,520)]),
    1 : Road(3,247, Spawnpoint= [(0,346), (0, 391)], Waypoint =[(247,497), (247,455)]),
    2 : Road(1,321, Spawnpoint= [(422, 0), (379, 0)], Waypoint =[(273,321), (316,321)]),
    3 : Road(1,322, Spawnpoint= [(831, 0), (790, 0)], Waypoint =[(682,322), (726,322)]),
    4 : Road(2,857, Spawnpoint= [(1050, 494), (1050, 452)], Waypoint =[(857,348), (857,390)]),
    5 : Road(0,520, Spawnpoint= [(684, 844), (727, 844)],Waypoint =[(833,520), (788,520)]),
    "I1" : Road(3,445, Waypoint =[(445,348 ), (445,388)]),
    "I2" : Road(2,659, Waypoint =[(659,494), (659, 451)])
}