import pygame, random, time
from Cars import *
from Env import Environment
from tensorflow.python.keras.models import load_model
import tensorflow as tf
import numpy as np

window = pygame.display.set_mode((1050,844))

env = Environment()

score = 0

interpreter = tf.lite.Interpreter(model_path="deepnn.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

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
    if len(currentCars) < 100:
        for i in range(num):
            spawnpoint = random.choice([0,1,1,1,2,2,3,4,4,4,5])
            # spawnpoint = random.choice([2,3,0,5])
            spawnRoad = SignalRoads[spawnpoint]
        
            newCar = Car(spawnpoint)
            #check if any collision was found on spawn
            if len(newCar.rect.collidelistall([car.rect for car in spawnRoad.queue]))>0:
                if len(spawnRoad.spawnQ) <10:
                    spawnRoad.spawnQ.append(newCar)
            else:
                currentCars.append(newCar)
                spawnRoad.queue.append(newCar)

background = pygame.image.load(r"./Assets/background.png")

running = True

startTime = time.time()

timeframe = 0

genCars(21)

while running:
    window.blit(background,(0,0))
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for road_id, road in SignalRoads.items():
            if road.signalState == False:
                pygame.draw.rect(window, (255, 0, 0, 200), roadHitboxes[road_id])
            else:
                pygame.draw.rect(window, (0, 255, 0, 200), roadHitboxes[road_id])
    
    if timeframe % 30 == 0: 
        data1 = env.getData1()
        data2 = env.getData2()

        data1 = np.array(data1, dtype=np.float32)
        data2 = np.array(data2, dtype=np.float32)

        # Ensure the input data has the correct shape
        data1 = data1.reshape((1, -1))  # Reshape to (1, num_features)
        data2 = data2.reshape((1, -1))  # Reshape to (1, num_features)

        # action1 = model1.predict(data1)
        # action2 = model1.predict(data2)

        interpreter.set_tensor(input_details[0]['index'], data1)
        interpreter.invoke()
        action1 = interpreter.get_tensor(output_details[0]['index'])

        interpreter.set_tensor(input_details[0]['index'], data2)
        interpreter.invoke()
        action2 = interpreter.get_tensor(output_details[0]['index'])

        action1 = list((action1[0] >= 0.5).astype(int))
        action2 = list((action2[0] >= 0.5).astype(int))

        # if action1 == [0,0,0,0]:
        #     traf_dens = data1[0][4:9]
        #     if traf_dens[4] < 0:
        #         signalIndex = traf_dens.argmax()
        #         action1[signalIndex] = 1    
        # if action2 == [0,0,0,0]:
        #     traf_dens = data2[0][4:9]
        #     if traf_dens[4] < 0:
        #         signalIndex = traf_dens.argmax()
        #         action2[signalIndex] = 1

        env.takeAction1(action1)
        env.takeAction2(action2)

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
                score += 1
            except:
                pass
            # genCars(random.choice([0,1,1,1,2,2,2,3,3]))
            genCars(1)

    elapsedTime = time.time() - startTime

    for road in SignalRoads.values():
        pygame.draw.rect(window, (0,0,0,200), road.signal)
    if not road.signalState:
        pygame.draw.circle(window,(255,0,0), road.signal.center, 5)
    else:
        pygame.draw.circle(window,(0,255,0), road.signal.center, 5)

    if elapsedTime >= 60:
        print(f"Score : {score}")
        running = False

    timeframe += 1 

    pygame.display.flip()
        