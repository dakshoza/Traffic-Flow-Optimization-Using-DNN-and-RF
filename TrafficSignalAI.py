import pygame
import numpy as np
import random
from Roads import monitoredRoads
from Agent import agent
from TrafficSignals import *
# Define your custom environment class
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
        
    def step(self):
        # Take an action in the environment


        nextState = self.getState()
        reward = self.getReward()

        # Check if terminal state or not through done which checks for either crash, either time limit or either goal score?
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

    def getReward(self):
        return reward


# Initialize Pygame and create the game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Create your custom environment
env = SimulationEnvironment()

# Create your DQN agent 
agent = agent(env.stateSize, env.actionSize)

# Training parameters
EPISODES = 1000  # Number of episodes
batchSize = 10  # Batch size for training

# Training loop
for episode in range(EPISODES):
    state = env.reset()
    # Delete all cars
    # Reset score
    # Wipe all lists 
    # Call genCar function

    state = np.reshape(state, [1, env.stateSize])
    for time in range(500):
        # Render the game window if needed
        # pygame.display.update()

        # Get action from the agent
        action = agent.act(state)

        # Take action in the environment
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, env.stateSize])

        # Store the transition in the agent's trainMemory memory
        agent.remember(state, action, reward, next_state, done)

        # Update the state
        state = next_state

        if done:
            print("Episode: {}/{}, Score: {}, Epsilon: {:.2}".format(episode, EPISODES, time, agent.epsilon))
            break

        # Train the agent by replaying experiences from the trainMemory memory
        if len(agent.memory) > batchSize:
            agent.trainMemory(batchSize)

    # Save the agent's weights every 100 episodes
    if episode % 100 == 0:
        agent.save_weights("agent_weights.h5")

# Save the final trained agent's weights
agent.save_weights("final_agent_weights.h5")

# Close the Pygame window
pygame.quit()
