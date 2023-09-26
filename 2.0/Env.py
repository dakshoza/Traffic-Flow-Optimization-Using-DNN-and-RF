import numpy as np
from Roads import *

class Environment:
    def __init__(self):
        pass

    def getState(self):
        trafficStates = np.array([Road.signalState for Road in SignalRoads.values()])
        queueLengths = np.array([len(Road.queue) for Road in SignalRoads.values()])
        distancesToClosestCars = np.array([Road.distanceToClosestCar for Road in SignalRoads.values()])

        trafficDensities = queueLengths / np.sum(queueLengths)

        training_example = np.concatenate((trafficStates, trafficDensities, distancesToClosestCars))

        return training_example

    def takeAction(self, action):
        for index, Road in enumerate(SignalRoads.values()):
            Road.signalState = action[index]

