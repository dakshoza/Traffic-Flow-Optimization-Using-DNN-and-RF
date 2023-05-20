import random
import pygame
from Roads import *
from Intersections import Intersection
class Car:
	def __init__(self):
		self.speed = 2
		self.hitbox = []

		# Car sprite and Car Length
		sprite = random.randint(1,6)
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

		self.rect = sprite.get_rect()
		#Generating Car Path
		# 0 - first exit, 1 - second exit, 2 - third exit
		self.carPath = []
		self.carPath.append(random.randint(0,2))
		self.carPath.append(random.randint(0,1))
		self.carPath.append(random.randint(0,2))

		#Car Spawn
		self.setSpawn(random.randint(1,7),self.carPath[0])
		# self.hitbox = (self.x, self.y, 30, self.carLength)


	def setSpawn(self, spawnLocation, firstTurn):
		#Spawn Location, orientation, x, y, car.rotate, hitbox, 
		print(f"{spawnLocation} - SpawnLocation")
		if spawnLocation == 1:
			self.orientation = "right" # left to right
			self.x = road1.boundaries[0] - self.carLength
			self.sprite = pygame.transform.rotate(self.sprite,270)
			self.y = road1.blitCoordinate(spawnLocation, self.carPath)
   
		if spawnLocation == 2:
			self.orientation = "down" # top to bottom
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.y = road3.boundaries[1] - self.carLength
			self.x = road3.blitCoordinate(spawnLocation, self.carPath)

		if spawnLocation == 3:
			self.orientation = "down" #top to bottom
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.y = road5.boundaries[1] - self.carLength
			self.x = road5.blitCoordinate(spawnLocation, self.carPath)

		if spawnLocation == 4:
			self.orientation = "left" # left to right
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.x = road7.boundaries[0] + road7.boundaries[2]
			self.y = road7.blitCoordinate(spawnLocation, self.carPath)
   
		if spawnLocation == 5:
			self.orientation = "up" #top to bottom
			self.sprite = pygame.transform.rotate(self.sprite,0)
			self.y = road9.boundaries[1] +  road9.boundaries[3]
			self.x = road9.blitCoordinate(spawnLocation, self.carPath)
			#Problem is here, x is not setting

		if spawnLocation == 6:
			if firstTurn ==1:
				self.setSpawn(6, random.choice([0,2]))
			del self.carPath[0]
			self.orientation = "up" #top to bottom
			self.sprite = pygame.transform.rotate(self.sprite,0)
			self.y = road11.boundaries[1] + road11.boundaries[3]
			if firstTurn == 0:
				self.x = road11.boundaries[0] + road11.freeSpace
			elif firstTurn == 2:
				self.x = road11.boundaries[0] + road11.laneWidth + 4 + road11.freeSpace


		if spawnLocation == 7:
			self.orientation = "up" #top to bottom
			self.sprite = pygame.transform.rotate(self.sprite,0)
			self.y = road13.boundaries[1] +  road13.boundaries[3] + self.carLength
			self.x = road13.blitCoordinate(spawnLocation, self.carPath)		
		print(f"{self.x, self.y} - coords")
		self.updateHitbox()
		# Spawn location 6 should also drop the first value in CarPath




	def drawCar(self, window):
		window.blit(self.sprite, (self.x,self.y))

	def changeOri(self, newOri):
		self.orientation = newOri
		self.updateHitbox()


	def moveCar(self):
		if self.orientation == "up":
			self.y -= self.speed
		elif self.orientation == "down":
			self.y += self.speed
		elif self.orientation == "right":
			self.x += self.speed
		elif self.orientation == "left":
			self.x -= self.speed
		self.updateHitbox()

	def drawHitbox(self, window):
		pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

	def updateHitbox(self):
		if (self.orientation == "up") or (self.orientation == "down"):
			self.hitbox = [self.x, self.y, 30, self.carLength] #top left x, top left y, width, height
		elif self.orientation == "left" or self.orientation == "right":
			self.hitbox = [self.x, self.y, self.carLength, 30] #top left x, top left y, width, height\
    
	def turn(self):
		print("placeholder")