import pygame
from Car import Car as Vehicle
# from Roads import *
pygame.init()
window = pygame.display.set_mode((1050,844))        

running = True 
background = pygame.image.load('Assets\Road Work Ahead1050.png')
cars = []
# car1 = Vehicle()
# cars.append(car1)
# def generateCar(numberOfCars):
#     global cars
#     totalCars = len(cars)+ numberOfCars
#     while len(cars) != (totalCars):
#         tempCar = Vehicle()
#         for car in cars:
#             if tempCar.x != car.x and tempCar.y != car.y:
#                 cars.append(tempCar)
# generateCar(5)
 
 

# -----DAKSH---------
# uncomment the next 3 lines if you want multiple cars spawning (there's still no turning)
# the cars also overlap when they spawn sometimes but I have an idea of how to fix that im doing that rn
def genCar(num):    
    global cars
    for i in range(0,num):
        tempCar = Vehicle()
        cars.append(tempCar)

genCar(4)

while running:
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # window color
    window.fill((81,81,81))
    window.blit(background,(0,0))

    carHitboxes = [car.hitbox for car in cars]

    # Car Movement and collision check
    for i,currentCar in enumerate(cars):
        carHitboxes[i] = pygame.Rect(0,0,0,0)
        if currentCar.hitbox.collidelist(carHitboxes) > 0:
            print("collision")
        carHitboxes[i] = currentCar.hitbox
        
        currentCar.moveCar()
        currentCar.drawCar(window)
        currentCar.drawHitbox(window)
            # generateCar(1)
    
    for currentCar in cars:    
        if not all([currentCar.hitbox.x < 1250 , currentCar.hitbox.x > -200 , currentCar.hitbox.y > -200 , currentCar.hitbox.y < 1040]):
            cars.remove(currentCar)
            genCar(2)
            
    # for road in allRoads:
    #     road.drawHitBox(window)

    pygame.display.update()