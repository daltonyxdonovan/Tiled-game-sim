import pygame

WHITE = (255, 255, 255)

class mainGuy(pygame.sprite.Sprite):
	def __init__ (self, color, width, height, speed):
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
		
	def moveLeft(self, pixels):
		self.rect.x -= pixels
		
	def moveRight(self, pixels):
		self.rect.x += pixels
		
	def moveUp(self, pixels):
		self.rect.y -= pixels
		
	def moveDown(self, pixels):
		self.rect.y += pixels
