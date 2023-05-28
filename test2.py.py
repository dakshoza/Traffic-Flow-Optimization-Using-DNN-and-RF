import random
import numpy as np
epsilon = 1
actionSize = 7
state_size = 14
# if np.random.rand() <= epsilon:
#     print(random.randrange(action_size))
# state = [random.uniform(0, 1) for _ in range(action_size)]
# print(state)
# action = [0,1,1,0,0,0,0]  
# action_indices = [1,6]
# print(action_indices)
# binary_action = [0] * action_size
# # for index in action_indices:
# #     binary_action[index] = 1
# binary_action = [0] * action_size
# for index in action_indices:
#     binary_action[index] = 1
# print(binary_action)

sorted_indices = [0,0,0]
num_actions = random.randint(1,2)  # Select random number of actions
action_indices = sorted_indices[:num_actions]  # Select top indices
# print(sorted_indices)

# Get the state of the environment (e.g., activation states of traffic lights)
# state = [random.randint(0, 1) for _ in range(state_size)]  # Randomly generate state
# print(state)

# # numActions = random.randint(1,actionSize)  # Select random number of actions
# actionIndices = random.sample(range(actionSize), numActions)

q_values = np.array([4,2,7,1,5,3,6])
sorted_indices = np.argsort(q_values)[::-1]  # Sort indices in descending order of Q-values
print(sorted_indices)
numActions = random.randint(1,2)  # Select random number of actions
print(numActions)
actionIndices = sorted_indices[:numActions]  # Select top indices
print(actionIndices)
binary_action = [0] * actionSize
for index in actionIndices:
    binary_action[index] = 1
print(binary_action)
        