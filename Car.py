import random
import pygame
from Roads import *
class Car:
	def __init__(self):
		self.speed = 2
  
		# Car sprite and Car Length
		sprite = random.randint(1,6)
		print(sprite)
		if sprite == 1:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite1.png")
			self.carLength = 49
			self.sprite = sprite
		elif sprite == 2:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite2.png")
			self.carLength = 51
			self.sprite = sprite
		elif sprite == 3:
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite3.png")
			self.carLength = 48
			self.sprite = sprite
		elif sprite == 4:
			self.carLength = 54
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite4.png")
			self.sprite = sprite
		elif sprite == 5:
			self.carLength = 52
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite5.png")
			self.sprite = sprite
		elif sprite == 6:
			self.carLength = 52
			sprite = pygame.image.load("./Assets/CarSprites/CarSprite6.png")
			self.sprite = sprite

		#Generating Car Path
		# 0 - first exit, 1 - second exit, 2 - third exit
		self.carPath = []
		self.carPath.append(random.randint(0,2))
		self.carPath.append(random.randint(0,1))
		self.carPath.append(random.randint(0,2))

		#Car Spawn
		self.setSpawn(random.randint(1,4),self.carPath[0])
		# self.hitbox = (self.x, self.y, 30, self.carLength)


	def setSpawn(self, spawnLocation, firstTurn):
		if spawnLocation == 1:
			self.orientation = "ltr" # left to right
			self.x = road1.boundaries[0] - self.carLength
			# self.sprite = pygame.transform.rotate(self.sprite,270)
			if firstTurn == 0:
				road1.boundaries[1] + road1.freeSpace
			elif firstTurn == 2:
				road1.boundaries[1] + road1.laneWidth + 4 + road1.freeSpace
			else:
				self.setSpawn(1, random.choice([0,2]))
				
			self.hitbox = (self.x,self.y, self.carLength,30) #top left x, top left y, width, height
		if spawnLocation == 2:
			self.orientation = "ttb" # top to bottom
			# self.sprite = pygame.transform.rotate(self.sprite,180)
			self.y = road3.boundaries[1] - self.carLength
			if firstTurn == 0:
				self.x = road3.boundaries[0] + road3.laneWidth + 4 + road3.freeSpace
			elif firstTurn == 2:
				self.x = road3.boundaries[0] + road3.laneWidth - road3.freeSpace
			else:
				self.setSpawn(2, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
		if spawnLocation == 3:
			self.orientation = "ttb" 
			# self.sprite = pygame.transform.rotate(self.sprite,180)
			self.y = road5.boundaries[1] - self.carLength
			if firstTurn == 0:
				self.x = road4.boundaries[0] + road4.laneWidth + 4 + road4.freeSpace
			elif firstTurn == 2:
				self.x = road4.boundaries[0] + road4.laneWidth - road4.freeSpace
			else:
				self.setSpawn(3, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
		
		if spawnLocation == 4:
			self.orientation = "rtl" # bottom to top
			# self.sprite = pygame.transform.rotate(self.sprite,90)
			self.x = road7.boundaries[0] + road7.boundaries[2] + self.carLength
			if firstTurn == 0:
				self.y = road7.boundaries[1] +road7.laneWidth + 4 + road7.freeSpace
			elif firstTurn == 2:
				self.y = road7.boundaries[1] + road7.freeSpace
			else:
				self.setSpawn(4, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
		if spawnLocation == 5:
			self.orientation = "rtl" # bottom to top
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.x = road7.boundaries[0] + road7.boundaries[2] + self.carLength
			if firstTurn == 0:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 48
			elif firstTurn == 2:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 3
			else:
				self.setSpawn(3, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
		if spawnLocation == 6:
			self.orientation = "rtl" # bottom to top
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.x = road7.boundaries[0] + road7.boundaries[2] + self.carLength
			if firstTurn == 0:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 48
			elif firstTurn == 2:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 3
			else:
				self.setSpawn(3, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
		if spawnLocation == 7:
			self.orientation = "rtl" # bottom to top
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.x = road7.boundaries[0] + road7.boundaries[2] + self.carLength
			if firstTurn == 0:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 48
			elif firstTurn == 2:
				self.y = road7.boundaries[1] + road7.boundaries[3] - 3
			else:
				self.setSpawn(3, random.choice([0,2]))
			self.hitbox = [self.x,self.y, 30, self.carLength] #top left x, top left y, width, height
    
		# Spawn location 6 should also drop the first value in CarPath




	def drawCar(self, window):
		window.blit(self.sprite, (self.x,self.y))

	def changeOri(self, newOri):
		if newOri == "btt":
			self.orientation = "btt"
			self.hitbox = [self.x, self.y, 20, 33]
		elif newOri == "ttb":
			self.orientation = "ttb"
			self.hitbox = [self.x, self.y, 20, -33]                  
		elif newOri == "ltr":
			self.orientation = "ltr"
			self.hitbox = [self.x, self.y, 33, 20]                  
		elif newOri == "rtl":
			self.orientation = "rtl"
			self.hitbox = [self.x, self.y, -33, 20]                  


	def moveCar(self):
		if self.orientation == "btt":
			self.y -= self.speed
		elif self.orientation == "ttb":
			self.y += self.speed
		elif self.orientation == "ltr":
			self.x += self.speed
		elif self.orientation == "rtl":
			self.x -= self.speed
			self.hitbox = [self.x,self.y, 20, 33] #top left x, top left y, width, height

	def drawHitbox(self, window):
		pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)
		print(self.hitbox)