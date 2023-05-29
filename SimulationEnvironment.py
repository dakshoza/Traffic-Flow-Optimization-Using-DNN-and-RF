import numpy as np
from Roads import monitoredRoads
from TrafficSignals import *

class SimulationEnvironment:
    def __init__(self):
        self.stateSize = 14  # Number of inputs
        self.actionSize = 7  # Number of outputs

    def reset(self):
        # Reset the environment to its initial state and return the initial state
        state = [0]*14
        for road in monitoredRoads:
            road.waitingTime = 0
        for signal in allSignals:
            signal.state = 0
        return state
  
    def takeAction(self, action):
        # Take an action in the environment
        for i,signal in enumerate(allSignals):
            signal.state = action[i]
        
    def getParameters(self, time, collision, waitingTime, score):
        nextState = self.getState()
        reward = self.getReward(collision, waitingTime, score)

        # Terminating episode condition
        if time >= 8040 or collision:
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
