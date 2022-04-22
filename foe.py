import pygame

#colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)

class Enemy(pygame.sprite.Sprite):
	def __init__ (self, color, speed, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		self.width = width
		self.height = height
		self.color = color
		self.speed = speed
		pygame.draw.rect(self.image, color, [0,0,width,height])
		self.rect = self.image.get_rect()
		
	def moveForward(self, pixels):
		self.rect.y -= pixels
	
	def moveBackward(self, pixels):
		self.rect.y += pixels
