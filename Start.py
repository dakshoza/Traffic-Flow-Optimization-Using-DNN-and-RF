import pygame
from Car import Car as Vehicle
# from Roads import *
pygame.init()
window = pygame.display.set_mode((1500,844))        

running = True 
background = pygame.image.load('./Assets/Background1500.png')
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
    
for i in range(0,7):
    tempCar = Vehicle()
    cars.append(tempCar)    
    
while running:
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # window color
    window.fill((81,81,81))
    window.blit(background,(0,0))

    # Hitboxes
    for i in cars:
        if i.x < 1600 and i.x > -100 and i.y > -100 and i.y < 940:
            i.moveCar()
            i.drawCar(window)
            i.drawHitbox(window)
        else:
            cars.remove(i)
            # generateCar(1)
        
    # for road in allRoads:
    #     road.drawHitBox(window)

    pygame.display.update()