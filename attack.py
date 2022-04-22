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

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))

class ballAttack(pygame.sprite.Sprite):
	def __init__ (self, color, speed, radius, pos ):
		super().__init__()
		self.color = color
		self.speed = speed
		self.width = width
		self.height = height
		self.radius = radius
		self.pos = pos
		pygame.draw.circle(screen, PURPLE, (400,400), 40)
		self.rect = self.image.get_rect()
