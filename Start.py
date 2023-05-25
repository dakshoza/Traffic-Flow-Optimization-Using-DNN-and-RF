import pygame
import random
from Car import Car as Vehicle
from Intersections import I1,I2 
import Roads
pygame.init()
window = pygame.display.set_mode((1050,844))        

running = True 
score = 0
background = pygame.image.load('Assets\Road Work Ahead1050.png')
cars = []
carHitboxes = []
def genCar(num):    
    global cars
    for i in range(0,num):
        tempCar = Vehicle()
        cars.append(tempCar)
        
genCar(3)

while running:
    window.blit(background,(0,0))

    pygame.draw.rect(window, (255, 0, 0), I1.hitbox, 2)
    pygame.draw.rect(window, (255, 0, 0), I2.hitbox, 2)
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # window color
    for road in Roads.allRoads:
        pygame.draw.rect(window,(0,0,255), road.boundaries, 2)
    carHitboxes = [car.hitbox for car in cars]

    # Car Movement and collision check
    for i,currentCar in enumerate(cars):
        carHitboxes = [car.hitbox for car in cars]
        carHitboxes.remove(currentCar.hitbox)
        if currentCar.hitbox.collidelist(carHitboxes) >= 0:
            if currentCar.distanceTravelled <= 20:
                print(f"Collision at spawnpoint: {currentCar.spawnLocation}")
                cars.remove(currentCar)
                print("respawning car")
                currentCar = Vehicle()
                print(f"new spawn: {currentCar.spawnLocation}")
                cars.append(currentCar)
            else:
                print("Collision")
        carHitboxes.append(currentCar.hitbox)
        carHitboxes[i] = currentCar.hitbox
        currentCar.moveCar()
        currentCar.drawCar(window)
        currentCar.drawHitbox(window)
    
    for currentCar in cars:    
        if not all([currentCar.hitbox.x < 1150 , currentCar.hitbox.x > -60 , currentCar.hitbox.y > -100 , currentCar.hitbox.y < 950]):
            cars.remove(currentCar)
            score += 1
            genCar(2)


    pygame.display.update()

print(f"Score: {score}")