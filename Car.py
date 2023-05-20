import random
import pygame
from Roads import *
from Intersections import Intersection
class Car:
	def __init__(self):
		self.speed = 2

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

		self.hitbox = sprite.get_rect()
		#Generating Car Path
		# 0 - first exit, 1 - second exit, 2 - third exit
		self.carPath = []
		self.carPath.append(random.randint(0,2))
		self.carPath.append(random.randint(0,2))

		#Car Spawn
		self.setSpawn(random.randint(1,5))
		# self.hitbox = (self.x, self.y, 30, self.carLength)


	def setSpawn(self, spawnLocation):
		#Spawn Location, orientation, x, y, car.rotate, hitbox, 
		print(f"{spawnLocation} - SpawnLocation")
		if spawnLocation == 1:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road2.boundaries[0] + road2.boundaries[3]
			self.hitbox.x = road2.blitCoordinate(spawnLocation, self.carPath)
			if self.carPath[0] == 1:
				self.carPath = random.choice([0,2])
   
		elif spawnLocation == 2:
			self.orientation = "up"
			self.updateHitbox()
			self.hitbox.y = road4.boundaries[1] + road4.boundaries[3]
			self.hitbox.x = road4.blitCoordinate(spawnLocation, self.carPath)
   
		elif spawnLocation == 3:
			self.orientation = "right"
			self.sprite = pygame.transform.rotate(self.sprite,270)
			self.updateHitbox()
			self.hitbox.x = road6.boundaries[0] - self.carLength
			self.hitbox.y = road6.blitCoordinate(spawnLocation, self.carPath)

		elif spawnLocation == 4:
			self.orientation = "down"
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.updateHitbox()
			self.hitbox.y = road8.boundaries[1] - self.carLength
			self.hitbox.x = road8.blitCoordinate(spawnLocation, self.carPath)
   
		else:
			self.orientation = "left"
			self.sprite = pygame.transform.rotate(self.sprite,90)
			self.updateHitbox()
			self.hitbox.x = road12.boundaries[0] +  road9.boundaries[2] + self.carLength
			self.hitbox.y = road12.blitCoordinate(spawnLocation, self.carPath)


	def drawCar(self, window):
		window.blit(self.sprite, (self.hitbox.x,self.hitbox.y))

	def changeOri(self, newOri):
		self.orientation = newOri
		self.updateHitbox()


	def moveCar(self):
		if self.orientation == "up":
			self.hitbox.y -= self.speed
		elif self.orientation == "down":
			self.hitbox.y += self.speed
		elif self.orientation == "right":
			self.hitbox.x += self.speed
		elif self.orientation == "left":
			self.hitbox.x -= self.speed

	def drawHitbox(self, window):
		pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

	def updateHitbox(self):
		self.hitbox = self.sprite.get_rect()
    
	def turn(self):
		print("placeholder")