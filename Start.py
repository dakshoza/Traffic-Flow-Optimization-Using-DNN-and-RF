import pygame
from Car import Car as Vehicle
pygame.init()
window = pygame.display.set_mode((1050,844))        

running = True 
background = pygame.image.load('Assets\Road Work Ahead1050.png')
cars = []
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
        # if currentCar.hitbox.collidelist(carHitboxes) > 0:
        #     print("collision")
        # carHitboxes[i] = currentCar.hitbox
            
        currentCar.moveCar()
        currentCar.drawCar(window)
        currentCar.drawHitbox(window)
    
    for currentCar in cars:    
        if not all([currentCar.hitbox.x < 1110 , currentCar.hitbox.x > -60 , currentCar.hitbox.y > -60 , currentCar.hitbox.y < 904]):
            cars.remove(currentCar)
            genCar(2)
            
    print(len(cars))

    pygame.display.update()