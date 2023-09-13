import pygame
import numpy as np
from Agent import agent
from TrafficSignals import *
from SimulationEnvironment import SimulationEnvironment

# Initialize Pygame and create the game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Create your custom environment
env = SimulationEnvironment()

# Create your DQN agent 
agent = agent(env.stateSize, env.actionSize)

# Training parameters
EPISODES = 1000  # Number of episodes
batchSize = 67  # Batch size for training

# Training loop
for episode in range(EPISODES):
    state = env.reset()
    # Delete all cars
    score = 0
    # Wipe all lists 
    # Call genCar function

    state = np.reshape(state, [1, env.stateSize])
    for time in range(8040):
        # Render the game window if needed
        # pygame.display.update()

        # Get action from the agent
        action = agent.act(state)
        # Take action in the environment
        env.takeAction(action)

        # Game implements action

        next_state, reward, done = env.getParameters(time, collision, waitingTime, score)
        next_state = np.reshape(next_state, [1, env.stateSize])

        # Store the transition in the agent's trainMemory memory
        agent.remember(state, action, reward, next_state, done)

        # Update the state
        state = next_state

        if done:
            print("Episode: {}/{}, Score: {}".format(episode, EPISODES, time))
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
