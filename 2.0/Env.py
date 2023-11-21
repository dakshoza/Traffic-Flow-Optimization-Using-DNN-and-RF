import csv
import numpy as np
from Roads import *
from Cars import *

class Environment:
    def __init__(self):
        pass

    def getData1(self):
        trafficStates = [Road.signalState for Road in list(SignalRoads.values())[:4]]
        queueLengths = [len(Road.queue) for Road in list(SignalRoads.values())[:4]]
        queueLengths.append(len(T1Turners))
        distancesToClosestCars = [Road.distanceToClosestCar for Road in list(SignalRoads.values())[:4]]
        # waitTimes = np.array([Road.roadWaitTime for Road in list(SignalRoads.values())[:4]])

        try:
            trafficDensities = [queueLengths[index] / sum(queueLengths) for index in range(len(queueLengths))]
        except ZeroDivisionError:
            trafficDensities = [0] * len(queueLengths)

        training_example = trafficStates + trafficDensities + distancesToClosestCars

        training_example = np.array([training_example])
        training_example = training_example.reshape(-1, 13)

        return training_example
    
    def getData2(self):
        trafficStates = [Road.signalState for Road in list(SignalRoads.values())[4:]]
        queueLengths = [len(Road.queue) for Road in list(SignalRoads.values())[4:]]
        queueLengths.append(len(T2Turners))
        distancesToClosestCars = [Road.distanceToClosestCar for Road in list(SignalRoads.values())[4:]]
        # waitTimes = np.array([Road.roadWaitTime for Road in list(SignalRoads.values())[:4]])

        try:
            trafficDensities = [queueLengths[index] / sum(queueLengths) for index in range(len(queueLengths))]
        except ZeroDivisionError:
            trafficDensities = [0] * len(queueLengths)

        training_example = trafficStates + trafficDensities + distancesToClosestCars

        training_example = np.array([training_example])
        training_example = training_example.reshape(-1, 13)

        return training_example
    
    def getSignalState(self):
        return np.array([Road.signalState for Road in list(SignalRoads.values())[:4]]).reshape(4,1)
    
    def getSignalState1(self):
        return np.array([Road.signalState for Road in list(SignalRoads.values())[:4]])

    def getSignalState2(self):
        return np.array([Road.signalState for Road in list(SignalRoads.values())[4:]])
    
    def append_to_csv(self, file_name, data):
        try:
            with open(file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Data appended to", file_name)
        except Exception as e:
            print("Error appending data to", file_name)
            print(e)

    def takeAction1(self, action):
        for index, Road in enumerate(list(SignalRoads.values())[:4]):
            Road.signalState = action[index]

    def takeAction2(self, action):
        for index, Road in enumerate(list(SignalRoads.values())[4:]):
            Road.signalState = action[index]

    def getReward(self, action, signalstate, score):
        reward = 0
        values_list = list(SignalRoads.values())[:4]

        for idx in range(len(action)):
            if action[idx] == 1:
                # toggling green on empty road
                if len(values_list[idx].queue) <= 0:
                    reward -= 100
                if values_list[idx].roadWaitTime >= 8:
                    reward -= 40
            else:
                if signalstate[idx] == 1:
                    # toggling green signal red even when cars are moving
                    if len(values_list[idx].queue) >= 1:
                        reward -= 500
            reward += score

        return reward

        
