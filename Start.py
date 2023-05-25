import pygame, time, Roads, random
from Car import Car as Vehicle
from Intersections import I1,I2 

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
        
genCar(3)

prevTime = time.time()

while running:
    dt = time.time() - prevTime # Calculating Delta Time
    prevTime = time.time()
    window.blit(background,(0,0))

    pygame.draw.rect(window, (255, 0, 0), I1.hitbox, 2)
    pygame.draw.rect(window, (255, 0, 0), I2.hitbox, 2)
    #event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # for road in Roads.allRoads:
    #     pygame.draw.rect(window,(0,0,255), road.boundaries, 2)
    carHitboxes = [car.hitbox for car in cars]

    # Car Movement and collision check
    for i,currentCar in enumerate(cars):
        carHitboxes[i] = pygame.Rect(0,0,0,0)
        if currentCar.hitbox.collidelist(carHitboxes) > 0:
            print("Car Crash")
            #FOR SCOTT: uncomment this line if you want the sim to stop when cars crash
            # running = False
        carHitboxes[i] = currentCar.hitbox
        currentCar.moveCar(dt)
        currentCar.drawCar(window)
        currentCar.drawHitbox(window)
    
    for currentCar in cars:    
        if not all([currentCar.hitbox.x < 1150 , currentCar.hitbox.x > -60 , currentCar.hitbox.y > -100 , currentCar.hitbox.y < 950]):
            cars.remove(currentCar)
            score += 1
            genCar(random.choice([0,1,1,1,1,2]))


    pygame.display.update()

print(f"Score: {score}")