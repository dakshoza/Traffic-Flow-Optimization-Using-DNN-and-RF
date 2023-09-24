import pygame, random
import time as tm
import numpy as np
from Roads_old import *
from Car_old import TURN
from Car_old import Car as Vehicle
from Agent_old import agent
from TrafficSignals_old import *
from Intersections_old import I1,I2 
from SimulationEnvironment_old import SimulationEnvironment

pygame.init()
window = pygame.display.set_mode((1050,844))        

env = SimulationEnvironment()
agent = agent(env.stateSize, env.actionSize)

EPISODES = 50
batchSize = 20 

running = True 
background = pygame.image.load('Assets\Road Work Ahead1050.png')

def genCar(num):    
    global cars, carHitboxes
    for i in range(num):
        carGenerated = False
        while not carGenerated:
            tempCar = Vehicle()
            # print(f"spawn: {tempCar.spawnLocation}")
            if tempCar.hitbox.collidelist(carHitboxes) == -1:
                carGenerated = True
                cars.append(tempCar)
                carHitboxes.append(tempCar.hitbox)
        
prevTime = tm.time()

# agent.load_weights("agent_weights_old.h5")

while running:
    #delta time estimation for debugging
    
    pygame.draw.rect(window, (255, 0, 0), I1.hitbox, 2)
    pygame.draw.rect(window, (255, 0, 0), I2.hitbox, 2)
    #event checking

    for episode in range(EPISODES):
        state = env.reset()
        cars = []
        carHitboxes = []
        invincibleCars = []
        score = 0
        waitingTime = 0
        genCar(8)

        state = np.reshape(state, [1, env.stateSize])
    
        for time in range(4020):
            collisionCheck = False
            action = agent.act(state)
            tempReward = env.takeAction(action)

            dt = 0.012044906616210938
            # dt = tm.time() - prevTime # Calculating Delta Time
            # prevTime = tm.time()
            window.blit(background,(0,0))   

            # Game implements action
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # if event.button == 1:  # Left mouse button
                    #     mouse_pos = pygame.mouse.get_pos()
                    #     for road in monitoredRoads:
                    #         if road.boundaries.collidepoint(mouse_pos):
                    #             road.update() 
                    #             break
                    # else:
                    #     genCar(1)
                if event.type == TURN:
                    turnedCar = event.ID
                    tempReward += 10
                    if turnedCar.hitbox in carHitboxes:
                        carHitboxes.remove(turnedCar.hitbox)
                    turnedCar.turnHitboxUpdate()
                    invincibleCars.append(turnedCar)
                    turnedCar.iTimer = 10
            
            for car in invincibleCars:
                if turnedCar.iTimer == 0:
                    carHitboxes.append(car.hitbox)
                    invincibleCars.remove(car)
                else:
                    car.iTimer -= 1
            # print(invincibleCars)

            for road in monitoredRoads:
                road.waitingTime = 0
                if road.signal.state == 0:
                    pygame.draw.rect(window,(255,0,0, 200), road.boundaries)
                elif road.signal.state == 1:
                    pygame.draw.rect(window,(0,255,0, 200), road.boundaries)
                
                road.carList = road.lane1List + road.lane2List
                # Wait time calculation
                for car in road.carList:
                    road.waitingTime += car.waitTime

            # Car Movement and collision check
            chbeforecol = len(carHitboxes)
            for i,currentCar in enumerate(cars):
                removed = False
                if currentCar.hitbox in carHitboxes:
                    try:
                        carHitboxes.remove(currentCar.hitbox)
                    except Exception as e:
                        pass
                    removed= True
                collision = currentCar.hitbox.collidelist(carHitboxes)
                if collision >= 0:
                    if not((currentCar in invincibleCars) or (carHitboxes[collision] in invincibleCars)):
                        # print("Car Crash")
                        collisionCheck = True
                if removed:
                    carHitboxes.append(currentCar.hitbox)
                
                # Linking Car and Roads
                roadIndex = currentCar.hitbox.collidelist(signalRoads)
                if roadIndex >=0:
                    collidedRoad = monitoredRoads[roadIndex]
                    
                    if collidedRoad.direction == "up":
                        if currentCar.hitbox.x < collidedRoad.boundaries.x + (collidedRoad.boundaries.width/2):
                            collidedRoad.lane1List.append(currentCar)
                            currentCar.lane=1
                        else:
                            collidedRoad.lane2List.append(currentCar)
                            currentCar.lane=2
                            
                    elif collidedRoad.direction == "down":
                        if currentCar.hitbox.x >= collidedRoad.boundaries.x + (collidedRoad.boundaries.width/2):
                            collidedRoad.lane1List.append(currentCar)
                            currentCar.lane=1
                        else:
                            collidedRoad.lane2List.append(currentCar)
                            currentCar.lane=2
                            
                    elif collidedRoad.direction == "left":
                        if currentCar.hitbox.y < collidedRoad.boundaries.y + (collidedRoad.boundaries.height/2):
                            collidedRoad.lane2List.append(currentCar)
                            currentCar.lane=2
                        else:
                            collidedRoad.lane1List.append(currentCar)
                            currentCar.lane=1
                            
                    elif collidedRoad.direction == "right":
                        if currentCar.hitbox.y < collidedRoad.boundaries.y + (collidedRoad.boundaries.height/2):
                            collidedRoad.lane1List.append(currentCar)
                            currentCar.lane=1
                        else:
                            collidedRoad.lane2List.append(currentCar)
                            currentCar.lane=2
                    currentCar.onRoad = collidedRoad
                
                currentCar.moveCar(dt)
                currentCar.drawCar(window)
                # currentCar.drawHitbox(window)
            chaftercol = len(carHitboxes)
            if chbeforecol != chaftercol:
                pass
            
            for currentCar in cars:    
                if not all([currentCar.hitbox.x < 1150 , currentCar.hitbox.x > -60 , currentCar.hitbox.y > -100 , currentCar.hitbox.y < 950]):
                    cars.remove(currentCar)
                    carHitboxes.remove(currentCar.hitbox)
                    score += 1
                    genCar(random.choice([0,1,1,1,1,1,1,1,1,1,1,2,2]))

            done = False
            next_state, reward, done = env.getParameters(time, collisionCheck, waitingTime, score*50)
            reward += tempReward
            next_state = np.reshape(next_state, [1, env.stateSize])

            # Store the transition in the agent's trainMemory memory
            agent.remember(state, action, reward, next_state, done)

            # Update the state
            state = next_state

            if done:
                print("Episode: {}/{}, Score: {}".format(episode, EPISODES, score))
                break

            # # Train the agent by replaying experiences from the trainMemory memory
            if len(agent.memory) > batchSize:
                agent.trainMemory(batchSize)

            # print("Training loss: ",agent.loss)
            
            pygame.display.update()
            for road in monitoredRoads:
                road.carList = []
                road.lane1List = []
                road.lane2List = []
        # Save the agent's weights every 10 episodes
        # if episode % 10 == 0:
        agent.save_weights("agent_weights.h5")

        if episode == 49:
            running = False
    
    # Save the final trained agent's weights
    # agent.save_weights("final_agent_weights.h5")

print(f"Score: {score}")