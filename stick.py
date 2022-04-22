import pygame
import random
import sys
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
CELL = 32


def load_image(name):
	image = pygame.image.load(name)
	return image

class Stick(pygame.sprite.Sprite):
	def __init__(self, dead):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(load_image('assets/tiles/stick_item.png').convert_alpha())
		self.index = 0
		self.dead = dead
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,32,32)

	def update(self):
		global count
		self.image = self.images[self.index]

	def redraw(self):
		global stickx
		global sticky
		stickx = random.randint(0, int(SCREEN_WIDTH-32))
		sticky = random.randint(0, int(SCREEN_HEIGHT-32))
		self.dead = False
		

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = Stick()
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
