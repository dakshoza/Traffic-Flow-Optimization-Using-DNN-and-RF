import csv
import numpy as np
from Roads import *

class Environment:
    def __init__(self):
        pass

    def getOldState(self):
        return np.array([Road.signalState for Road in list(SignalRoads.values())[:4]])

    def getData(self, oldState):
        trafficStates = np.array([Road.signalState for Road in list(SignalRoads.values())[:4]])
        queueLengths = np.array([len(Road.queue) for Road in list(SignalRoads.values())[:4]])
        queueLengths = np.append(queueLengths, len(T1Turners))
        distancesToClosestCars = np.array([Road.distanceToClosestCar for Road in list(SignalRoads.values())[:4]])
        # waitTimes = np.array([Road.roadWaitTime for Road in list(SignalRoads.values())[:4]])

        trafficDensities = queueLengths / np.sum(queueLengths)

        training_example = np.concatenate((oldState, trafficDensities, distancesToClosestCars, trafficStates))

        self.append_to_csv('2.0\TrainingDataset.csv', training_example)

    def append_to_csv(self, file_name, data):
        try:
            with open(file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Data appended to", file_name)
        except Exception as e:
            print("Error appending data to", file_name)
            print(e)

    def takeAction(self, action):
        for index, Road in enumerate(SignalRoads.values()):
            Road.signalState = action[index]
