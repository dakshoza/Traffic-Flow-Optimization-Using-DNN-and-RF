import random
import numpy as np
import tensorflow as tf
from collections import deque
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizer_v2.adam import Adam

class DRLAgent:
    
    def __init__(self) -> None:
        self.actionSize = 4
        self.memory = deque(maxlen=1000)  
        self.gamma = 0.99 
        self.epsilon = 1.0  
        self.epsilonDecay = 0.85  
        self.epsilonMin = 0.01  
        self.learningRate = 0.1 
        self.loss= 0
        self.model = self.buildModel()
    
# Build architecture of the model and compile
    def buildModel(self):
        model1 = Sequential([
            Dense(20, activation = 'relu', input_shape = (13,)),
            Dense(13, activation = 'relu'),
            Dense(13, activation = 'relu'),
            Dense(self.actionSize, activation = 'sigmoid')
        ])
        model1.compile(loss = 'binary_crossentropy', optimizer=Adam(lr = self.learningRate), metrics=['accuracy'])
        return model1


    def remember(self, state, action, reward, nextState, done):
        self.memory.append((state, action, reward, nextState, done))
        if len(self.memory) > self.memory.maxlen:
            self.memory.popleft()

# Choosing an appropriate action based on the policy
    def chooseAction(self, inpdata):
        if np.random.rand() <= self.epsilon:
            # Random action selection
            actionIndice = np.random.randint(0, self.n_actions)
        else:
            # Exploitation: Select actions with highest Q-values
            qValues = self.model.predict(inpdata)
            sortedIndice = np.argsort(qValues[0])[::-1]  # Sort indices in descending order of Q-values
            actionIndice = sortedIndice[0]  # Select top indice

        action = [0] * self.actionSize
        action[actionIndice] = 1
        return action

    def train(self, batchSize):
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

# To save the weights of the agent
    def saveWeights(self, filename):
        self.model.save_weights(filename)

# To load the weights of the agent
    def loadWeights(self, filename):
        self.model.load_weights(filename)