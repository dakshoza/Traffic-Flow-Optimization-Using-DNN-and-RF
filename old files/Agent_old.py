import random
import numpy as np  
import tensorflow as tf
from collections import deque
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizer_v2.adam import Adam

# Define your DQN agent class
class agent:
    def __init__(self, stateSize, actionSize):
        self.stateSize = stateSize
        self.actionSize = actionSize
        # self.memory = deque(maxlen=1000)  
        self.memory  = []
        self.gamma = 0.95  
        self.epsilon = 1.0  
        self.epsilonDecay = 0.85  
        self.epsilonMin = 0.01  
        self.learningRate = 0.1 
        self.loss= 0
        self.model = self.buildModel()

    def buildModel(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.stateSize, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.actionSize, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learningRate))
        return model

    def remember(self, state, action, reward, nextState, done):
        self.memory.append((state, action, reward, nextState, done))
        # if len(self.memory) > self.memory.maxlen:
        if len(self.memory) > 1000:
            self.memory.pop(0)

    def act(self, state):
        #epsilon-greedy policy
        if np.random.rand() <= self.epsilon:
            # Random action selection
            numActions = random.randint(1, 2)  # Select random number of actions
            actionIndices = random.sample(range(self.actionSize), numActions)  # Select random indices
        else:
            # Exploitation: Select actions with highest Q-values
            qValues = self.model.predict(state)
            sortedIndices = np.argsort(qValues[0])[::-1]  # Sort indices in descending order of Q-values
            numActions = random.randint(1,2)  # Select random number of actions
            actionIndices = sortedIndices[:numActions]  # Select top indices

        binaryAction = self.getBinaryAction(actionIndices) # Get binary action based on selected indices of highest Q-values
        return binaryAction

    def getBinaryAction(self, actionIndices):
        binaryAction = [0] * self.actionSize
        for index in actionIndices:
            binaryAction[index] = 1
        return binaryAction


    def trainMemory(self, batchSize):
        # Train the agent by training Memory experiences from the trainMemory memory
        minibatch = random.sample(self.memory, batchSize)
        
        for state, action, reward, nextState, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(nextState)[0]))
            
            targetFinal = self.model.predict(state)
            targetFinal[0][action] = target # Updates current(predicted) Q-values with target Q-values

            self.model.fit(state, targetFinal, epochs=1, verbose=1) # Train the model according to target Q-values

        if self.epsilon > self.epsilonMin:
            self.epsilon *= self.epsilonDecay # Decaying epsilon value to reduce exploration and promote exploitation

        del minibatch  # Clear memory

    def save_weights(self, filename):
        # Save the weights of the agent to a file
        self.model.save_weights(filename)

    def load_weights(self, filename):
        # Load the weights of the agent from a file
        self.model.load_weights(filename)

