import random
from Graphing import *
class Car:
    def __init__(self):
        self.executedT1 = False
    #Spawn Point
        spawnpoint = random.choice([1,2,2,2,3,3,4,5,5,5,6])
        '''
            This biases the spawning so that there is a :
            - 1 in 11 chance for it to spawn at 1
            - 6 in 11 chance for it to spawn on the main road.
            - 2 in 11 chance for it to spawn on road 3 to simulate a busier side road
            - 2 in 11 chance for it to spawn on the right side
        '''
    #Path Generation
        #Basic Path
        destinations = [1,2,3,4,5,6]
        destinations.remove(spawnpoint)

        endpoint = random.choice(destinations)
        self.path = getPath(spawnpoint, endpoint)

        #Waypoints

    #Spawning
    
    # def findWaypoints(path):

    # def turns():

            


for i in range(12):
    x = Car()