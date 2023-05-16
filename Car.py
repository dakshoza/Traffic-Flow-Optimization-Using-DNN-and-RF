import random
import pygame
from Roads import *
class Car:
	def __init__(self):
		self.hitbox = []
		self.speed = 1.5

		sprite = random.randint(1,7)
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
		self.setSpawn(random.randint(1,7),self.carPath[0])


	def setSpawn(self, spawnLocation, firstTurn):
		if spawnLocation == 1:
			self.orientation = "ltr" # left to right
			self.x = road1.boundaries[0] - self.carLength
			if firstTurn == 0:
				self.y = road1.boundaries[1] - 3
			elif firstTurn == 2:
				self.y = road1.boundaries[1] - 51
				self.hitbox = [self.x,self.y, 20, 33] #top left x, top left y, width, height




	def drawCar(self, window):
		if self.orientation == "btt":
			window.blit(self.sprite, (self.x, self.y))
		elif self.orientation == "ttb":
			window.blit(pygame.transform.rotate(self.sprite, 180), (self.x, self.y))
		elif self.orientation == "ltr":
			window.blit(pygame.transform.rotate(self.sprite, 90), (self.x, self.y))
		elif self.orientation == "rtl":
			window.blit(pygame.transform.rotate(self.sprite, 270), (self.x, self.y))

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