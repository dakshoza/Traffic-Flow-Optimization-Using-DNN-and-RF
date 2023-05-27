import pygame, time, random
from Car import Car as Vehicle
from Intersections import I1,I2 
from Car import TURN
from Roads import *

pygame.init()
window = pygame.display.set_mode((1050,844))        

running = True 
score = 0
background = pygame.image.load('Assets\Road Work Ahead1050.png')
cars = []
carHitboxes = []
def genCar(num):    
    global cars, carHitboxes
    for i in range(num):
        carGenerated = False
        while not carGenerated:
            tempCar = Vehicle()
            print(f"spawn: {tempCar.spawnLocation}")
            if tempCar.hitbox.collidelist(carHitboxes) == -1:
                carGenerated = True
                cars.append(tempCar)
                carHitboxes.append(tempCar.hitbox)
        
genCar(2)

prevTime = time.time()

invincibleCars = []

while running:
    #delta time estimation for debugging
    dt = 0.012044906616210938
    
    # dt = time.time() - prevTime # Calculating Delta Time
    # prevTime = time.time()
    
    
    window.blit(background,(0,0))
    pygame.draw.rect(window, (255, 0, 0), I1.hitbox, 2)
    pygame.draw.rect(window, (255, 0, 0), I2.hitbox, 2)
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TURN:
            turnedCar = event.ID
            invincibleCars.append(turnedCar)
            turnedCar.iTimer = 10
            carHitboxes.remove(pygame.Rect(turnedCar.hitbox.x, turnedCar.hitbox.y, turnedCar.hitbox.height, turnedCar.hitbox.width))
    
    for car in invincibleCars:
        if turnedCar.iTimer == 0:
            carHitboxes.append(car.hitbox)
            invincibleCars.remove(car)
        else:
            car.iTimer -= 1
        
    print(invincibleCars)
            
            
    # for road in Roads.allRoads:
    #     pygame.draw.rect(window,(0,0,255), road.boundaries, 2)

    # Car Movement and collision check
    for i,currentCar in enumerate(cars):
        removed = False
        if currentCar.hitbox in carHitboxes:
            carHitboxes.remove(currentCar.hitbox)
            removed= True
        collision = currentCar.hitbox.collidelist(carHitboxes)
        if collision >= 0:
            if not((currentCar in invincibleCars) or (carHitboxes[collision] in invincibleCars)):
                print("Car Crash")
                running = False
        if removed:
            carHitboxes.append(currentCar.hitbox)
        
        # Linking Car and Roads
        roadIndex = currentCar.hitbox.collidelist(signalRoads)
        if roadIndex >=0:
            monitoredRoads[roadIndex].carList.append(currentCar)
            currentCar.onRoad = monitoredRoads[roadIndex]
        
        currentCar.moveCar(dt)
        currentCar.drawCar(window)
        currentCar.drawHitbox(window)
    
    for currentCar in cars:    
        if not all([currentCar.hitbox.x < 1150 , currentCar.hitbox.x > -60 , currentCar.hitbox.y > -100 , currentCar.hitbox.y < 950]):
            cars.remove(currentCar)
            carHitboxes.remove(currentCar.hitbox)
            score += 1
            genCar(random.choice([2]))


    pygame.display.update()

print(f"Score: {score}")