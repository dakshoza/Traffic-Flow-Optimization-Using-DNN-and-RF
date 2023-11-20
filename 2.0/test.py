import numpy as np
import random
from Roads import SignalRoads

reward = 0

action = [0, 0, 0, 0]

for idx in range(len(action)):
    if action[idx] == 1:
        values_list = list(SignalRoads.values())[:4]
        if len(values_list[idx].queue) <= 0:
            print("HELP")

                
