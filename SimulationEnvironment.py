import numpy as np
from Roads import monitoredRoads
from TrafficSignals import *

class SimulationEnvironment:
    def __init__(self):
        self.stateSize = 14  # Number of inputs
        self.actionSize = 7  # Number of outputs
        self.iterationCount = [0] * self.actionSize


    def reset(self):
        # Reset the environment to its initial state and return the initial state
        state = [0]*14
        for road in monitoredRoads:
            road.waitingTime = 0
            road.carList = []
            road.lane1List = []
            road.lane2List = []
        for signal in allSignals:
            signal.state = 0
        return state
  
    def takeAction(self, action):
        # Take an action in the environment
        tempReward = 0
        for i, road in enumerate(monitoredRoads):
            if action[i] != road.signal.state: 
                if self.iterationCount[i] <= 10: 
                    tempReward -= 10
                else:
                    tempReward += road.update(action[i])
                    self.iterationCount[i] = 0
            self.iterationCount[i] += 1
        return tempReward
        
    def getParameters(self, time, collisionCheck, waitingTime, score):
        nextState = self.getState()
        reward = self.getReward(collisionCheck, waitingTime, score)

        # Terminating episode condition
        if time >= 8040 or collisionCheck:
            done = True
        else:
            done = False

        return nextState, reward, done
    
    def getState(self):
        # Get the state of the environment (e.g., activation states of traffic lights)
        state = []
        # Get road waiting times
        for road in monitoredRoads:
            state.append(road.waitingTime)
        # Get signal states    
        for signal in allSignals:
            state.append(signal.state)
        
        return np.array(state, dtype=int)

    def getReward(self, collision, waitingTime, score):
        reward = 0
        if collision:
            reward -= 1000
        reward -= waitingTime
        reward += score

        return reward
