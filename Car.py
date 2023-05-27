import random, pygame
from Roads import *
from Intersections import *

TURN = pygame.USEREVENT + 0
class Car:
	def __init__(self):
		self.speed = 120
		self.distanceIntoIntersection = 0
		self.turnI1 = False
		self.turnI2 = False
		self.turn1Executed = False
		self.turn2Executed = False
		self.iTimer = 0 #invincibility timer
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
		#self.spawnLocation = random.choice([3])
		self.setSpawn(self.spawnLocation)
		# self.setSpawn(3)

	def setSpawn(self, spawnLocation):
		if spawnLocation == 1:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road2.boundaries[1] + road2.boundaries[3]
			if self.carPath[0] == 1:
				self.carPath[0] = random.choice([0,2])
			self.hitbox.x = road2.blitCoordinate(spawnLocation, self.carPath)
			
   
		elif spawnLocation == 2:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road4.boundaries[1] + road4.boundaries[3]
			if self.carPath[0] == 2:
				if self.carPath[1] == 0:
					self.carPath[1] = random.choice([1,2])
			self.hitbox.x = road4.blitCoordinate(spawnLocation, self.carPath)
   
		elif spawnLocation == 3:
			self.orientation = "right"
			self.sprite = pygame.transform.rotate(self.sprite,270)
			self.updateHitbox()
			self.hitbox.x = road6.boundaries[0] - 52
			if self.carPath[0] == 1:
				if self.carPath[1] == 0:
					self.carPath[1] = random.choice([1,2])
			self.hitbox.y = road6.blitCoordinate(spawnLocation, self.carPath)

		elif spawnLocation == 4:
			self.orientation = "down"
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.updateHitbox()
			self.hitbox.y = road8.boundaries[1] - 52
			if self.carPath[0] == 0:
				if self.carPath[1] == 0:
					self.carPath[1] = random.choice([1,2])
			self.hitbox.x = road8.blitCoordinate(spawnLocation, self.carPath)
   
		else:
			self.orientation = "left"
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.updateHitbox()
			self.hitbox.x = road12.boundaries[0] +  road9.boundaries[2] + 52
			if self.carPath[0] == 2:
				self.carPath[0] = random.choice([0,1])
			self.hitbox.y = road12.blitCoordinate(spawnLocation, self.carPath)

		self.pos = pygame.math.Vector2(self.hitbox.topleft)
			
   
	def drawCar(self, window):
		window.blit(self.sprite, (self.hitbox.x,self.hitbox.y))

	def changeOri(self, newOri):
		self.orientation = newOri
		self.turnHitboxUpdate()

	def turnHitboxUpdate(self):
		self.hitbox = pygame.Rect(self.hitbox.x,self.hitbox.y,self.hitbox.height,self.hitbox.width)
  
	def checkSignal(self,dt):
		try:
			if self.onRoad.state == 0:
				stopCoord = self.onRoad.stopPosition(self)
				if self.orientation == "up":
					if self.hitbox.y - round(self.speed*dt) <= stopCoord:
						return False
					else:
						return True
				elif self.orientation == "down":
					if self.hitbox.y + round(self.speed*dt) >= stopCoord:
						return False
					else:
						return True
				elif self.orientation == "right":
					if self.hitbox.x + round(self.speed*dt) >= stopCoord:
						return False
					else:
						return True
				elif self.orientation == "left":
					if self.hitbox.x - round(self.speed*dt) <= stopCoord:
						return False
					else:
						return True
		except:
			return True

	def moveCar(self, dt):
		if self.checkSignal(dt):
			if self.orientation == "up":
				self.pos.y -= self.speed * dt
				self.hitbox.y = round(self.pos.y)
			elif self.orientation == "down":
				self.pos.y += self.speed * dt
				self.hitbox.y = round(self.pos.y)
			elif self.orientation == "right":
				self.pos.x += self.speed * dt
				self.hitbox.x = round(self.pos.x)
			elif self.orientation == "left":
				self.pos.x -= self.speed * dt
				self.hitbox.x = round(self.pos.x)
			self.checkIntersectionI1(dt)
			self.checkIntersectionI2(dt)


	def updateHitbox(self):
		self.hitbox = self.sprite.get_rect()
    
	def checkCurrentTurn(self):
		# if (self.turnI1 == True) and (self.turnI2 == True):
		# 	pass
		if (self.turnI1 == True) or (self.turnI2 == True):
			return self.carPath[1] 
		else:
			return self.carPath[0]
	
	def checkIntersectionI1(self,dt):
		invincibility = pygame.event.Event(TURN, ID = self)
		if (self.hitbox.colliderect(I1.hitbox)):
			if self.turn1Executed:
				pass
			else:
				if self.checkCurrentTurn() == 1:
					self.turn1Executed = True
					self.turnI1 = True
					selectedLane = self.selectLane()
				else:
					self.distanceIntoIntersection += self.speed * dt
					selectedLane = self.selectLane()
					if self.distanceIntoIntersection >= selectedLane:
						self.turnCar()
						self.turn1Executed = True
						pygame.event.post(invincibility)
						self.turnI1 = True
						self.distanceIntoIntersection = 0

	def checkIntersectionI2(self, dt):
		invincibility = pygame.event.Event(TURN, ID = self)
		if (self.hitbox.colliderect(I2.hitbox)):
			if not self.turn2Executed:
				if self.checkCurrentTurn() == 1:
					self.turn2Executed = True
					self.turnI2 = True
					selectedLane = self.selectLane()
				else:
					self.distanceIntoIntersection += self.speed * dt
					selectedLane = self.selectLane()
					if self.distanceIntoIntersection >= selectedLane:
						self.turnCar()
						self.turn2Executed = True
						pygame.event.post(invincibility)
						self.turnI2 = True
						self.distanceIntoIntersection = 0

	def selectLane(self):
		self.currentTurn = self.checkCurrentTurn()
		self.secondTurn = self.carPath[1]
		
		if self.spawnLocation == 1 or self.spawnLocation == 5:
			leftLane1 = road1.freeSpace + 36
			leftLane2 =  road1.laneWidth +  road1.freeSpace + 4 + 35
			rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace + 34
			rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace + 34
		
		elif self.spawnLocation == 3 or self.spawnLocation == 4:
			leftLane1 = road1.freeSpace + 50
			leftLane2 =  road1.laneWidth +  road1.freeSpace + 4 + 49
			rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace + 47
			rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace + 47

		else:
			leftLane1 = road1.freeSpace + 30
			leftLane2 =  road1.laneWidth +  road1.freeSpace + 4 + 30
			rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace + 32
			rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace + 32
			if self.turnI1 == True and self.secondTurn == 2:
				rightLane1 += 15

		if self.currentTurn == 0:
			if self.secondTurn == 0:
				return leftLane1
			else:
				if self.spawnLocation == 4 and self.secondTurn != 2:
					return leftLane1
				else:
					return leftLane2
			
		elif self.currentTurn == 2:
			if self.secondTurn == 2:
				return rightLane1
			else:
				return rightLane2
		elif self.currentTurn == 1:
			return None

	def turnCar(self):
		if self.orientation == "up":
			if self.currentTurn == 0:
				self.sprite = pygame.transform.rotate(self.sprite,90)
				self.changeOri("left")
			else:
				self.sprite = pygame.transform.rotate(self.sprite,-90)
				self.changeOri("right")

		elif self.orientation == "right":
			if self.currentTurn == 0:
				self.sprite = pygame.transform.rotate(self.sprite,90)
				self.changeOri("up")
			else:
				self.sprite = pygame.transform.rotate(self.sprite,-90)
				self.changeOri("down")

		elif self.orientation == "left":
			if self.currentTurn == 0:
				self.sprite = pygame.transform.rotate(self.sprite,90)
				self.changeOri("down")
			else:
				self.sprite = pygame.transform.rotate(self.sprite,-90)
				self.changeOri("up")

		elif self.orientation == "down":
			if self.currentTurn == 0:
				self.sprite = pygame.transform.rotate(self.sprite,90)
				self.changeOri("right")
			else:
				self.sprite = pygame.transform.rotate(self.sprite,-90)
				self.changeOri("left")

	def drawHitbox(self, window):
	 	pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
