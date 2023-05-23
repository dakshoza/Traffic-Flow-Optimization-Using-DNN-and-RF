import random
import pygame
from Roads import *
from Intersections import *
class Car:
	def __init__(self):
		self.speed = 3
		self.distanceIntoIntersection = 0
		self.turnI1 = False
		self.turnI2 = False
		self.turn1Executed = False
		self.turn2Executed = False
		# Car sprite and Car Length
		sprite = random.randint(1,6)
		if sprite == 1:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite1.png")
			self.sprite = sprite
		elif sprite == 2:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite2.png")
			self.sprite = sprite
		elif sprite == 3:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite3.png")
			self.sprite = sprite
		elif sprite == 4:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite4.png")
			self.sprite = sprite
		elif sprite == 5:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite5.png")
			self.sprite = sprite
		elif sprite == 6:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite6.png")
			self.sprite = sprite

		self.hitbox = sprite.get_rect()

		#Generating Car Path
		# 0 - first exit, 1 - second exit, 2 - third exit
		self.carPath = []
		self.carPath.append(random.randint(0,2))
		self.carPath.append(random.randint(0,2))

		self.spawnLocation = random.randint(1,5)
		self.setSpawn(self.spawnLocation)


	def setSpawn(self, spawnLocation):
		if spawnLocation == 1:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road2.boundaries[1] + road2.boundaries[3]
			self.hitbox.x = road2.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[0] == 1:
				self.carPath[0] = random.choice([0,2])
   
		elif spawnLocation == 2:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road4.boundaries[1] + road4.boundaries[3]
			self.hitbox.x = road4.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[1] == 0:
				self.carPath[1] = random.choice([1,2])
   
   
		elif spawnLocation == 3:
			self.orientation = "right"
			self.sprite = pygame.transform.rotate(self.sprite,270)
			self.updateHitbox()
			self.hitbox.x = road6.boundaries[0] - 52
			self.hitbox.y = road6.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[1] == 0:
				self.carPath[1] = random.choice([1,2])
   

		elif spawnLocation == 4:
			self.orientation = "down"
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.updateHitbox()
			self.hitbox.y = road8.boundaries[1] - 52
			self.hitbox.x = road8.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[1] == 0:
				self.carPath[1] = random.choice([1,2])
   
		else:
			self.orientation = "left"
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.updateHitbox()
			self.hitbox.x = road12.boundaries[0] +  road9.boundaries[2] + 52
			self.hitbox.y = road12.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[0] == 2:
				self.carPath[0] = random.choice([0,1])
   
		print("done")


	def drawCar(self, window):
		window.blit(self.sprite, (self.hitbox.x,self.hitbox.y))

	def changeOri(self, newOri):
		self.orientation = newOri
		self.updateHitbox()

	def moveCar(self):
		self.checkIntersectionI1()
		self.checkIntersectionI2()
		# self.turn()
		if self.orientation == "up":
			self.hitbox.y -= self.speed
		elif self.orientation == "down":
			self.hitbox.y += self.speed
		elif self.orientation == "right":
			self.hitbox.x += self.speed
		elif self.orientation == "left":
			self.hitbox.x -= self.speed

	def updateHitbox(self):
		self.hitbox = self.sprite.get_rect()
    
	def checkCurrentTurn(self):
		# if (self.turnI1 == True) and (self.turnI2 == True):
		# 	pass
		if (self.turnI1 == True) or (self.turnI2 == True):
			return self.carPath[1] 
		else:
			return self.carPath[0]
	
	def checkIntersectionI1(self):
		if (self.hitbox.colliderect(I1.hitbox)):
			if self.checkCurrentTurn() == 1:
				pass
			else:
				if self.turn1Executed:
					pass
				else:
					self.distanceIntoIntersection += self.speed
					selectedLane = self.selectLane()
					if self.distanceIntoIntersection >= selectedLane:
						self.turnCar()
						self.turn1Executed = True
						self.turnI1 = True
						print(f"Car Path: {self.carPath} Current Turn: {self.currentTurn} Selected Lane: {selectedLane}")
		# else:
		# 	print("NOT COLIDE")

	def checkIntersectionI2(self):
		if (self.hitbox.colliderect(I2.hitbox)):
			if self.checkCurrentTurn() == 1:
				pass
			else:
				if self.turn2Executed:
					pass
				else:
					self.distanceIntoIntersection += self.speed
					selectedLane = self.selectLane()
					if self.distanceIntoIntersection >= selectedLane:
						self.turnCar()
						self.turn2Executed = True
						self.turnI2 = True
						print(f"Car Path: {self.carPath} Current Turn: {self.currentTurn} Selected Lane: {selectedLane}")
		#else:
			#print("NOT COLIDE")	

	def selectLane(self):
		leftLane1 = road1.freeSpace
		leftLane2 =  road1.laneWidth +  road1.freeSpace + 4
		rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace
		rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace

		self.currentTurn = self.checkCurrentTurn()
		self.secondTurn = self.carPath[1]

		if self.currentTurn == 0:
			if self.secondTurn == 0:
				return leftLane1
			else:
				return leftLane2
			
		elif self.currentTurn == 2:
			if self.secondTurn == 2:
				return rightLane1
			else:
				return rightLane2

	def turnCar(self):
		pass

		# if(self.carPath[1]==0):
		# 	return leftLane1
		# elif(self.carPath[1]==2):
		# 	return leftLane2
		# elif(self.carPath[1]==0):
		# 	return leftLane1
		# 	else(self.carPath[1]==2):
		# 		 leftLane2
		
			
		
		
	'''def checkIntersection(self):
		collisionFound = False
		for road in allRoads:
			if road.boundaries.collidepoint(self.hitbox.x, self.hitbox.y):
				road.carList.append(self)
				collisionFound = True
	
		# at this point, the car is on a road or not, if not then it can be in an intersection, if its in an intersection then,

		#if self.onRoad == 'intersection':
	# so now the possibilities are its either not hit a road yet or its on a road, if its on a road we don't have to do anything, if it isn't on a road we don't have to do anything. so now to write the turning code					

		# if self.distanceIntoIntersection != 0:
		# 	if self.carPath[0] == 1:
				'''

	# def drawHitbox(self, window):
	# 	pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

	''' def carCollisionWithIntersection(self, cars):
        carHitboxes = [car.hitbox for car in cars]
        carsInIntersection = self.hitbox.collidelistall(carHitboxes)
        if carsInIntersection != []:
           # print(self.hitbox.collidelistall(carHitboxes))
           for x in carsInIntersection:
                print(x)
           # self.distancetravelled += 1
            
            #self.turnInIntersection(cars)
        else:
            print("Not colliding")
        
    def turnInIntersection(self,cars):
        pass
        '''


