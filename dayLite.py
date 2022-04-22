import pygame
import time
import random
import sys
import os
from pygame.locals import *
# COLOR SCHEME
GREEN = (20, 255, 140)
DARKGREY = (80, 82, 78)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (38,79,110)
BLACK = (0, 0, 0)
count = 0
flags = SCALED | FULLSCREEN | DOUBLEBUF
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(resolution, flags, 16)


def load_image(name):
	image = pygame.image.load(name)
	return image

class daylite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(load_image('assets/dayCycle/dayCycle1.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle2.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle3.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle4.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle5.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle6.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle7.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle8.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle9.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle10.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle11.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle12.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle13.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle14.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle15.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle16.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle17.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle18.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle19.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle20.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle21.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle22.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle23.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle24.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle25.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle26.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle27.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle28.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle29.png').convert_alpha())
		self.images.append(load_image('assets/dayCycle/dayCycle30.png').convert_alpha())


		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,1,1)

		
	def update(self):
		global count
		self.image = self.images[self.index]
		count += 1
		if count >= 200:
			self.index = self.index + 1
			count = 0
		if self.index > 29:
			self.index = 0

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = daylite()
	my_group = pygame.sprite.Group(my_sprite)

	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		# Calling the 'my_group.update' function calls the 'update' function of all
		# its member sprites. Calling the 'my_group.draw' function uses the 'image'
		# and 'rect' attributes of its member sprites to draw the sprite.
		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()

	if __name__ == '__main__':
		main()
