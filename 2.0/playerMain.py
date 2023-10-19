import pygame, time
from Cars import *
from Env import Environment

window = pygame.display.set_mode((1050,844))

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

startTime = time.time()

score = 0

background = pygame.image.load("Assets/background.png")

roadHitboxes = {
    0 : pygame.Rect(252, 523, 86, 321),
    1 : pygame.Rect(1, 325, 245, 96),
    2 : pygame.Rect(357, 0, 87, 319),
    3 : pygame.Rect(768, 0, 87, 319),
    4 : pygame.Rect(861, 431, 190, 86),
    5 : pygame.Rect(662, 522, 86, 322),
    "I1" : pygame.Rect(450, 432, 207, 84),
    "I2" : pygame.Rect(450, 324, 207, 88)
}

running = True
tick = 100
genCars(10)

while running:
    window.blit(background,(0,0))
    # Event Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_t:  # Toggle Signals
                for road in SignalRoads.values():
                    road.signalState = not road.signalState
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for road_id, rect in roadHitboxes.items():
                    if rect.collidepoint(mouse_pos):
                        SignalRoads[road_id].signalState = not SignalRoads[road_id].signalState
    
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
    tick -= 1
    if tick ==0:
        tick = 100
        genCars(random.choice([0,1,1,1,2,2,2,3,3]))

    for car in TurningCars:
        car.turn()

    for car in ExitingCars:
        car.drive()

    for car in currentCars:
        car.render(window)

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
                ExitingCars.remove(car)
                score += 1
            except:
                pass
            genCars(random.choice([0,1,1,1,2,2,2,3,3]))
            # genCars(1)

    elapsedTime = time.time() - startTime
    
    if elapsedTime >= 60:
        print(f"Score : {score}")
        running = False

    for road in SignalRoads.values():
        pygame.draw.rect(window, (0,0,0,200), road.signal)
        if not road.signalState:
            pygame.draw.circle(window,(255,0,0), road.signal.center, 5)
        else:
            pygame.draw.circle(window,(0,255,0), road.signal.center, 5)


    pygame.display.flip()
    