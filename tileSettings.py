import pygame 
from pygame.locals import *
import random
from playerPic import playerPNG
from pygame.constants import DOUBLEBUF, FULLSCREEN, HWSURFACE, RESIZABLE, VIDEORESIZE
from water import waterPNG
from dayLite import daylite
from cowPic import cowPNG
from collections import Counter
from stick import Stick
from bunny import Bunny


def load_image(name):
	image = pygame.image.load(name)
	return image

pygame.init()
pygame.mixer.init()
flags = SCALED | DOUBLEBUF | HWSURFACE# | FULLSCREEN
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1070
MAP_WIDTH = 2000
MAP_HEIGHT = 2000
CELL = 32
playerscreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
bufferscreen = pygame.Surface((125,75))
pygame.display.set_caption("topDown")
clock = pygame.time.Clock()
mapx = 500
mapy = 500
grid = []
riverstart = True
justspawned = True
font = pygame.font.SysFont("Arial", 20)
evens = [x for x in range(100) if x%2 == 0]
tilechance = random.randint(0,10)
watergroup = pygame.sprite.Group()
watercount = 0
grasscount = 0
dayClock = 0
inventorybuffer = ['stick', 'stick', 'stick', 'stick', 'stick']
inventory = ['stick']
sword = False
hoe = False
shovel = True
swordspawned = False
hoeSpawned = False
shovelSpawned = False


selectnumber = 0
craftingnumber = 0
craftingticker = 0
grasscount = 0
left = False
right = False
up = False
down = True
craftinglist = []
crafting = False
#VIEWPORT SCREEN MOVEMENT MOTHERFUCKERS



#tile settings
grass = load_image("assets/tiles/grassFloor.png")
grass2 = load_image("assets/tiles/grassFloor2.png")
grass22 = load_image("assets/tiles/grassFloor22.png")
grass3 = load_image("assets/tiles/grassFloor3.png")
grass4 = load_image("assets/tiles/grassFloor4.png")
grass5 = load_image("assets/tiles/grassFloor5.png")
grass6 = load_image("assets/tiles/grassFloor6.png")
rock = load_image("assets/tiles/rockFloor.png")
rock2 = load_image("assets/tiles/rockFloor2.png")
rock22 = load_image("assets/tiles/rockFloor22.png")
rock222 = load_image("assets/tiles/rockFloor222.png")
rock3 = load_image("assets/tiles/rockFloor3.png")
water = load_image("assets/tiles/waterFloor1.png")
water2 = load_image("assets/tiles/waterFloor2.png")
water3 = load_image("assets/tiles/waterFloor3.png")
marker = load_image("assets/tiles/marker.png")
floor3 = load_image("assets/tiles/floor3.png")
swirl1 = load_image("assets/loading/swirl1.png")
swirl2 = load_image("assets/loading/swirl2.png")
swirl3 = load_image("assets/loading/swirl3.png")
swirl4 = load_image("assets/loading/swirl4.png")
banner = load_image("assets/loading/BANNER.png")
invtile = load_image("assets/inventory/invtile.png")
chest = load_image("assets/tiles/chest_closed.png")
boulder = load_image("assets/tiles/boulder.png")
stick = load_image("assets/inventory/stick.png")
shovel = load_image("assets/inventory/shovel.png")
grassitem = load_image("assets/inventory/grass.png")
bush1 = load_image("assets/tiles/bush1.png")
bush2 = load_image("assets/tiles/bush2.png")
bush3 = load_image("assets/tiles/bush3.png")
bush4 = load_image("assets/tiles/bush4.png")
stake = load_image("assets/tiles/stake1.png")
selection = load_image("assets/inventory/selection.png")
shovelbase = load_image("assets/tiles/base_shovel.png")
hoebase = load_image("assets/tiles/base_hoe.png")
swordbase = load_image("assets/tiles/base_sword.png")
base = load_image("assets/tiles/base.png")
swords = load_image("assets/inventory/sword.png")
hoeimg = load_image("assets/inventory/hoe.png")
blank = load_image("assets/inventory/blank.png")
craftselection = load_image("assets/crafting/selection.png")



#music COURTESY OF MONDO LOOPS :> WOOOOO
ambient = pygame.mixer.music.load("assets/music/ajourneyinthedark.ogg")


bunnyx = 500
bunnyy = 500
cowx = 200
cowy = 200
stickx = 600
sticky = 600

# COLOR SCHEME
GREEN = (20, 255, 140)
DARKGREY = (80,82,78)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (24,0,255)
BLACK = (0, 0, 0)

startthing = font.render("Day Timer is: " + str(dayClock), 10, (BLACK))
running = True

#sprites
player = playerPNG(33)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT/2
playergroup = pygame.sprite.Group()
playergroup.add(player)
playerspeed = 3
playerbuffer = [129, 594, 483, 276]

cow = cowPNG()
cow.rect.x = cowx + mapx
cow.rect.y = cowy + mapy
cowgroup = pygame.sprite.Group()
cowgroup.add(cow)

bunnys = Bunny()
bunnys.rect.x = bunnyx + mapx
bunnys.rect.y = bunnyy + mapy
bunnygroup = pygame.sprite.Group()
bunnygroup.add(bunnys)

day = daylite()
day.rect.x = 0
day.rect.y = 0
daygroup = pygame.sprite.Group()
daygroup.add(day)

stick_item = Stick(False)
stick_item.rect.x = stickx + mapx
stick_item.rect.y = sticky + mapy
stick_group = pygame.sprite.Group()
stick_group.add(stick_item)

#flags

#FOR RANDOM GENERATION BOOT- UNCOMMENT TO USE
generating = True
loading = False


#FOR TESTING LOAD FROM SAVE ONLY- UNCOMMENT TO USE
#generating = False
#loading = True

generationcount = 0
riverchance = random.randint(4,28)
chestspawned = False


