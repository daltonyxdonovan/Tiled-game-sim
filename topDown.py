import pygame, time
from player import mainGuy
from attack import ballAttack
from foe import Enemy
pygame.init()
global counter
global countertimeout
global score

#inits
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("topD0WN")
myfont = pygame.font.SysFont("thick pixel", 20, bold=True)
myfont2 = pygame.font.SysFont("thick pixel", 10, bold=True)
clock = pygame.time.Clock()

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

#variables
playervelocity = 5
running = True
justStarted = True
counter = 100
countertimeout = 0
score = 0
enemy1x = 30
enemy1y = 30
radius = 70

#add to groups
playerDude = pygame.sprite.Group()
attacks = pygame.sprite.Group()
Enemies = pygame.sprite.Group()

#set attributes for objects
playerGuy = mainGuy(RED, 50, 50, playervelocity)
playerGuy.rect.x = 375
playerGuy.rect.y = 375
location = (playerGuy.rect.x, playerGuy.rect.y)

Balls = ballAttack(GREEN, playervelocity, radius, location)

enemy1 = Enemy(GREEN, playervelocity, 50, 50)
enemy1.rect.x = 200
enemy1.rect.y = 200

#add objects to groups
playerDude.add(playerGuy)
attacks.add(Balls)
Enemies.add(enemy1)

#main loop
while running:
	#fill screen, draw walls
	keys = pygame.key.get_pressed()
	radius -= 1
	screen.fill(CYAN)
	if radius < 50:
		radius = 50
	if justStarted:
		startthing = myfont.render("get rekt scrub", 60, (0,0,0))
		startthing_rect = startthing.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		screen.blit(startthing, startthing.get_rect(center = screen.get_rect().center))
		justStarted = False
		
		pygame.display.update()
		pygame.time.wait(500)
	pygame.draw.rect(screen, YELLOW, [0, 780, 800, 20], 0)
	pygame.draw.rect(screen, YELLOW, [0, 0, 800, 20], 0)
	pygame.draw.rect(screen, YELLOW, [0, 0, 20, 800], 0)
	pygame.draw.rect(screen, YELLOW, [780, 0, 20, 800], 0)
	power = myfont2.render("attack power left - " + str(counter), 60, (0,0,0))
	power_rect = power.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(power, power.get_rect(bottomright = screen.get_rect().bottomright))
	scoretext = myfont.render(str(score), False, (0,0,0))
	scoretext_rect = scoretext.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(scoretext, scoretext.get_rect(topright = screen.get_rect().topright))
	
	attacks.draw(screen)
	playerDude.draw(screen)
	Enemies.draw(screen)
	
		#attack logic/ drawing?
	if keys[pygame.K_SPACE]:
		radius += 2
		if radius > 80:
			radius = 80
		print(radius)
	
	#player movement
	if keys[pygame.K_UP]:
		playerGuy.moveUp(playervelocity)
	if keys[pygame.K_w]:
		playerGuy.moveUp(playervelocity)
	if keys[pygame.K_DOWN]:
		playerGuy.moveDown(playervelocity)
	if keys[pygame.K_s]:
		playerGuy.moveDown(playervelocity)
	if keys[pygame.K_LEFT]:
		playerGuy.moveLeft(playervelocity)
	if keys[pygame.K_a]:
		playerGuy.moveLeft(playervelocity)
	if keys[pygame.K_RIGHT]:
		playerGuy.moveRight(playervelocity)
	if keys[pygame.K_d]:
		playerGuy.moveRight(playervelocity)
		
	#wall logic
	if playerGuy.rect.x < 20:
		playerGuy.rect.x = 20
	if playerGuy.rect.x > 730:
		playerGuy.rect.x = 730
	if playerGuy.rect.y < 20:
		playerGuy.rect.y = 20
	if playerGuy.rect.y > 730:
		playerGuy.rect.y = 730
		
	sprite_collision_list = pygame.sprite.spritecollide(playerGuy, Enemies, True)
	if sprite_collision_list:
		running = False
	sprite_collision_list2 = pygame.sprite.groupcollide(Enemies, attacks, True, True)
	if sprite_collision_list2:
		score += 100
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	if keys[pygame.K_ESCAPE]:
			exit()
	
	pygame.display.update()
	clock.tick(30)
	
