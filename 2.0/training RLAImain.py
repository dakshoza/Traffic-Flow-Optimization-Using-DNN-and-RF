import pygame, random
import Roads, Cars
from Cars import *
from Env import Environment
from DRLAgent import DRLAgent

window = pygame.display.set_mode((1050,844))

env = Environment()
agent = DRLAgent()

agent.loadWeights('2.0\model_weights.h5')

episodes = 1
batchSize = 2

roadHitboxes = {
    0 : pygame.Rect(252, 523, 86, 321),
    1 : pygame.Rect(1, 325, 245, 96),
    2 : pygame.Rect(357, 0, 87, 319),
    "I1" : pygame.Rect(450, 432, 207, 84),
    3 : pygame.Rect(768, 0, 87, 319),
    4 : pygame.Rect(861, 431, 190, 86),
    5 : pygame.Rect(662, 522, 86, 322),
    "I2" : pygame.Rect(450, 324, 207, 88)
}

def genCars(num):
    if len(currentCars) < 20:
        for i in range(num):
            # spawnpoint = random.choice([0,1,1,1,2,2,3,4,4,4,5])
            spawnpoint = random.choice([0,1,2,3,4])
            spawnRoad = SignalRoads[spawnpoint]
        
            newCar = Car(spawnpoint)
            #check if any collision was found on spawn
            if len(newCar.rect.collidelistall([car.rect for car in spawnRoad.queue]))>0:
                if len(spawnRoad.spawnQ) <10:
                    spawnRoad.spawnQ.append(newCar)
            else:
                currentCars.append(newCar)
                spawnRoad.queue.append(newCar)

background = pygame.image.load("Assets/background.png")

running = True

for roads in list(SignalRoads.values())[4:]:
            roads.signalState = True

while running:

    for episode in range(episodes):
        if episode != 0:
            TurningCars = []
            currentCars = []
            T1Turners = []
            T2Turners = []
            ExitingCars = []
            for road in SignalRoads.values():
                road.queue = []
                road.spawnQ = []
        for roads in list(SignalRoads.values())[:4]:
            roads.signalState = False
        genCars(random.randint(8, 16))

        for time in range(4020000):

            window.blit(background,(0,0))
            # Event Check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(f"Score: {Cars.scoret1}")
                    running = False

            for road_id, road in list(SignalRoads.items())[:4]:
                    if road.signalState == False:
                        pygame.draw.rect(window, (255, 0, 0, 200), roadHitboxes[road_id])
                    else:
                        pygame.draw.rect(window, (0, 255, 0, 200), roadHitboxes[road_id])
            
            if time % 30 == 0:
                # every 10 steps a decision is made
                state1 = env.getData1()

                action1 = [0] * 4

                for road in list(SignalRoads.values())[:4]:
                    if road.distanceToClosestCar <= 130:
                        action1 = agent.chooseAction(state1)
                        break

                env.takeAction1(action1)

            for car in currentCars:
                car.render(window)

            for road in SignalRoads.values():
                if len(road.queue) != 0:
                    road.checkTurn()
                    if len(road.spawnQ) >0:
                        road.spawnQ[0].drive(4)
                        if len(road.spawnQ[0].rect.collidelistall([car.rect for car in road.queue]))==0:
                            road.spawnQ[0].drive(-4)
                            road.queue.append(road.spawnQ[0])
                            currentCars.append(road.spawnQ.pop(0))
                        else:
                            road.spawnQ[0].drive(-4)

            for car in TurningCars:
                car.turn()
                # if len(car.rect.collidelistall(TurningCars)) >0:
                #     pass # Collision Detected

            for car in ExitingCars:
                car.drive()

                # Deleting the cars
                if (car.rect.x < -150 or car.rect.x > 1200) or (car.rect.y < -150 or car.rect.y > 990):
                    try:
                        currentCars.remove(car)
                    except:
                        pass
                    try:
                        TurningCars.remove(car)
                    except:
                        pass
                    try:
                        T1Turners.remove(car)
                    except:
                        pass
                    try:
                        T2Turners.remove(car)
                    except:
                        pass
                    try:
                        ExitingCars.remove(car)
                    except:
                        pass
                    # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
                    genCars(1)

            for road in SignalRoads.values():
                pygame.draw.rect(window, (0,0,0,200), road.signal)
            if not road.signalState:
                pygame.draw.circle(window,(255,0,0), road.signal.center, 5)
            else:
                pygame.draw.circle(window,(0,255,0), road.signal.center, 5)
                    
            if time % 30 == 0:

                nextState1 = env.getData1()

                signalstate = env.getSignalState1()

                reward = env.getReward(action1, signalstate, Cars.scoret1)

                if time >= 4020:
                    done = True
                    print("Episode: {}/{}, Score: {}".format(episode, episodes, Cars.scoret1))
                else:
                    done = False

                agent.remember(state1, action1, reward, nextState1, done)

                if len(agent.memory) > batchSize:
                    for road in list(SignalRoads.values())[:4]:
                        if road.distanceToClosestCar <= 130:
                            agent.train(batchSize)
                            break

                if Cars.scoret1 >= 1000:
                    print("Achieved Score: {}".format(Cars.scoret1))
                    agent.saveWeights('RLmodel_weights.h5')
                    agent.loadWeights('RLmodel_weights.h5')
                    Cars.scoret1 = 0

            pygame.display.flip()
        
        print(f"Final Score: {Cars.scoret1}")


        # if episode % 5 == 0:       
        #     agent.saveWeights('RLmodel_weights.h5')
        
        # if episode == 49:
        #     running = False

agent.saveWeights('final_RLmodel_weights.h5')

