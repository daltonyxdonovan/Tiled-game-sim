import pygame
from tileSettings import *
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont("Arial", 20)
cowchance = 150
cowcount = 0
wheelposition = 0

#write a method to check how many times something is in inventorybuffer
def check_inventory(item):
	count = 0
	for i in inventorybuffer:
		if i == item:
			count += 1
	return count
def craft_check():
	if check_inventory("stick") >= 3:
		if "shovel" not in craftinglist:
			craftinglist.append("shovel")
	if check_inventory("stick") >= 4:
		if "sword" not in craftinglist:
			craftinglist.append("sword")
	if check_inventory("stick") >= 5:
		if "hoe" not in craftinglist:
			craftinglist.append("hoe")
def craft_display(index):
	
	try:
		
		if craftinglist[index] == "shovel":
			playerscreen.blit(shovel, [player.rect.x-18, player.rect.y-72])
		if craftinglist[index] == "sword":
			playerscreen.blit(swords, [player.rect.x-18, player.rect.y-72])
		if craftinglist[index] == "hoe":
			playerscreen.blit(hoeimg, [player.rect.x-18, player.rect.y-72])
	except:
		pass

def Convert(string):
    li = list(string.split(" "))
    return li
def render_text(text, x, y):
	textsurface = font.render(text, True, (255,255,255))
	playerscreen.blit(textsurface, (x, y))
def load_image(name):
	image = pygame.image.load(name)
	return image
def cellNumber(row, column):
	if row >= 0 and row < int(MAP_HEIGHT/CELL) and column >= 0 and column < int(MAP_WIDTH/CELL):
		return grid[row][column]
	else:
		return 0
def run_rules():
	tempchance = random.randint(1,10)
	global grid
	temp = []
	for row in range(int(MAP_HEIGHT/CELL)):
		temp.append([])
		for column in range(int(MAP_WIDTH/CELL)):
			tilechance = random.randint(0,10)
			cell_sum = sum([cellNumber(row -1, column),
							cellNumber(row -1, column -1),
							cellNumber(row, column -1),
							cellNumber(row +1, column -1),
							cellNumber(row +1, column),
							cellNumber(row +1, column +1),
							cellNumber(row, column +1),
							cellNumber(row -1, column +1)])
			if grid[row][column] == 1 or grid[row][column] == 2 or grid[row][column] == 3 or grid[row][column] == 4 or grid[row][column] == 5 or grid[row][column] == 6 and cell_sum < 6:
				if tilechance < 4:
					temp[row].append(1)
				elif tilechance >3 and tilechance < 5:
					temp[row].append(2)
				elif tilechance >4 and tilechance < 6:
					temp[row].append(3)
				elif tilechance == 6:
					temp[row].append(4)
				elif tilechance == 7:
					temp[row].append(5)
				else:
					temp[row].append(6)
			elif grid[row][column] != 0 and cell_sum > 35:
				if tempchance < 4:
					temp[row].append(-50)
				if tempchance > 3 and tempchance < 7:
					temp[row].append(-51)
				else:
					temp[row].append(-52)
			elif grid[row][column] == 0 and cell_sum >=3:
				temp[row].append(1)
			else:
				currentValue = cellNumber(row,column)
				temp[row].append(currentValue)
	grid = temp
def smooth_rules():
		
	global grid
	temp = []
	for row in range(int(MAP_HEIGHT/CELL)):
		temp.append([])
		for column in range(int(MAP_WIDTH/CELL)):
			if grid[row][column] == 1 or grid[row][column] == 2 or grid[row][column] == 3 or grid[row][column] == 4 or grid[row][column] == 5 or grid[row][column] == 6:
				if cellNumber(row -1, column) == -50:
					temp[row].append(-52)
				elif cellNumber(row -1, column -1) == -51:
					temp[row].append(-52)
				elif cellNumber(row, column -1) == -50:
					temp[row].append(-51)
				elif cellNumber(row, column -1) == -50 and cellNumber(row -1, column) == -52:
					temp[row].append(-52)
				elif cellNumber(row, column -1) == -52 and cellNumber(row -1, column) == -51:
					temp[row].append(-52)
				elif cellNumber(row, column -1) == -52 and cellNumber(row -1, column) == -52:
					temp[row].append(-52)
				elif cellNumber(row +1, column -1) == -51:
					temp[row].append(-52)
				elif cellNumber(row +1, column) == -50:
					temp[row].append(-52)
				elif cellNumber(row +1, column +1) == -50:
					temp[row].append(-51)
				elif cellNumber(row, column +1) == 0:
					temp[row].append(0)
				elif cellNumber(row -1, column +1) == 0:
					temp[row].append(0)
				else:
					currentValue = cellNumber(row,column)
					temp[row].append(currentValue)
			else:
				currentValue = cellNumber(row,column)
				temp[row].append(currentValue)
	grid = temp
def boulder_rules():
	global grid
	temp = []
	grid[random.randint(0,int(MAP_HEIGHT/CELL)-5)][random.randint(0,int(MAP_WIDTH/CELL)-5)] = 1000
	for row in range(int(MAP_HEIGHT/CELL)):
		temp.append([])
		for column in range(int(MAP_WIDTH/CELL)):
			cell_sum = sum([cellNumber(row -1, column),
							cellNumber(row -1, column -1),
							cellNumber(row, column -1),
							cellNumber(row +1, column -1),
							cellNumber(row +1, column),
							cellNumber(row +1, column +1),
							cellNumber(row, column +1),
							cellNumber(row -1, column +1)])
			if grid[row][column] == 6 and cell_sum < -200:
				temp[row].append(-100)
			if grid[row][column] == 7 and cell_sum > 10:
				temp[row].append(1000)
			if grid[row][column] != 0 and grid[row][column] != -1 and cell_sum > 700:
				temp[row].append(1000)
			else:
				currentValue = cellNumber(row,column)
				temp[row].append(currentValue)
	grid = temp
def draw_invtile():
	global invtile
	playerscreen.blit(invtile, (int(SCREEN_WIDTH/2 - invtile.get_width()/2), int(SCREEN_HEIGHT - invtile.get_height())))
def river_rules():
	pass
def inventoryPresent(index):

	invposition = [(240,530),(315,530),(390,530),(465,530),(540,530),(615,530),(690,530),(765,530)]

	if inventory[index] == 'stick':
		texts = str(inventorybuffer.count('stick'))
		textsurface = font.render(texts, True, (255,255,255))
		playerscreen.blit(stick, (invposition[index]))
		playerscreen.blit(textsurface, invposition[index])

	elif inventory[index] == 'shovel':
		playerscreen.blit(shovel, (invposition[index]))

	elif inventory[index] == 'grassitem':
		if int(inventorybuffer.count('grassitem')) > 0:
			texts = str(inventorybuffer.count('grassitem'))
			playerscreen.blit(grassitem, (invposition[index]))
			textsurface = font.render(texts, True, (255,255,255))
			playerscreen.blit(textsurface, invposition[index])

	elif inventory[index] == 'sword':
		playerscreen.blit(swords, (invposition[index]))

	elif inventory[index] == 'hoes':
		playerscreen.blit(hoeimg, (invposition[index]))

	elif inventory[index] != 'axe' and inventory[index] != 'grassitem' and inventory[index] != 'shovel' and inventory[index] != 'hoes' and inventory[index] != 'sword' and inventory[index] != 'stick':
		playerscreen.blit(blank, (invposition[index]))

	else:
		playerscreen.blit(blank, (invposition[index]))
def invselector(wheel):
	invposition = [(240,530),(315,530),(390,530),(465,530),(540,530),(615,530),(690,530),(765,530)]
	if wheel == 0:
		playerscreen.blit(selection, invposition[0])
	elif wheel == 1:
		playerscreen.blit(selection, invposition[1])
	elif wheel == 2:
		playerscreen.blit(selection, invposition[2])
	elif wheel == 3:
		playerscreen.blit(selection, invposition[3])
	elif wheel == 4:
		playerscreen.blit(selection, invposition[4])
	elif wheel == 5:
		playerscreen.blit(selection, invposition[5])
	elif wheel == 6:
		playerscreen.blit(selection, invposition[6])
	elif wheel == 7:
		playerscreen.blit(selection, invposition[7])
def cowAI(restfactor):
	global cowx
	global cowy
	global cowcount
	global cowchance
	
	cowcount += 1
	if cowcount > 100:
		
		cowchance = random.randint(0,restfactor)
		cowcount = 0
	if cowchance < 100:
		cowx -= 1
		cow.moveLeft()
	if cowchance > 99 and cowchance < 200:
		cowx += 1
		cow.moveRight()
	if cowchance > 199 and cowchance < 300:
		cowy -= 1
		cow.moveUp()
	if cowchance > 299 and cowchance < 400:
		cowy += 1
		cow.moveDown()
	if cowchance > 399:
		cow.standingLeft()
def tilePickup():
	global inventory
	global grid
	global grasscount
	position = (player.rect.x+15, player.rect.y+40)
	playercolumn = position[0] // CELL
	playerrow = position[1] // CELL
	if cellNumber(mousextile,mouseytile) == 1 or cellNumber(mousextile,mouseytile) == 2 or cellNumber(mousextile,mouseytile) == 3 or cellNumber(mousextile,mouseytile) == 4 or cellNumber(mousextile,mouseytile) == 5 or cellNumber(mousextile,mouseytile) == 6 or cellNumber(mousextile,mouseytile) == -50 or cellNumber(mousextile,mouseytile) == -51 and grid[mousextile][mouseytile] != grid[playerrow][playercolumn]:
		grid[mousextile][mouseytile] = 0
		if grassitem not in inventory:
			inventorybuffer.append('grassitem')
			[inventory.append(x) for x in inventorybuffer if x not in inventory]
			grasscount = grasscount + 1
		if grassitem in inventory:
			grasscount = grasscount + 1
	if cellNumber(mousextile,mouseytile) == -52 or cellNumber(mousextile,mouseytile) == -51 and grid[mousextile][mouseytile] != grid[playerrow][playercolumn]:
		grid[mousextile][mouseytile] = 0
		if grassitem not in inventory:
			inventorybuffer.append('grassitem')
			[inventory.append(x) for x in inventorybuffer if x not in inventory]
			grasscount = grasscount + 1
		if grassitem in inventory:
			grasscount = grasscount + 1
	if cellNumber(mousextile,mouseytile) == -51:
		grid[mousextile][mouseytile] = 0
		if grassitem not in inventory:
			inventorybuffer.append('grassitem')
			[inventory.append(x) for x in inventorybuffer if x not in inventory]
			grasscount = grasscount + 1
		if grassitem in inventory:
			grasscount = grasscount + 1
def tilePutdown(index):
	global inventory
	global grid
	global grasscount
	position = (player.rect.x+15, player.rect.y+40)
	playercolumn = position[0] // CELL
	playerrow = position[1] // CELL
	try:
		if inventory[index] == 'grassitem' and cellNumber(mousextile,mouseytile) == 0:
			if cellNumber(mousextile,mouseytile) == 0 or cellNumber(mousextile,mouseytile) == -1 and grassitem in inventory:
				grid[mousextile][mouseytile] = 6
				inventorybuffer.remove('grassitem')
				grasscount = grasscount - 1
	except:
		pass

#             GRID CREATE

for row in range(int(MAP_HEIGHT/CELL)):
	grid.append([])
	for column in range(int(MAP_WIDTH/CELL)):
		chance = random.randint(0,10)
		if chance == 0:
			grid[row].append(0)
		elif chance == 1:
			grid[row].append(1)
		elif chance == 2:
			grid[row].append(2)
		elif chance == 3:
			grid[row].append(3)
		elif chance == 4:
			grid[row].append(4)
		elif chance == 5:
			grid[row].append(5)
		else:
			grid[row].append(6)
pygame.mixer.music.play(-1)
while running:
	
	
	if wheelposition > 7:
		wheelposition = 0
	if wheelposition < 0:
		wheelposition = 7
	mousepos = (pygame.mouse.get_pos())
	mousex = mousepos[1]+mapy
	mousextile = mousex // CELL
	mousey = mousepos[0]+mapx
	mouseytile = mousey // CELL
#            generation
	if generating:
		playerscreen.fill((BLACK))
		playerscreen.blit(banner,(40,484))
		print("Generating")
		generationcount += 1
		if generationcount ==1:
			run_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount ==2:
			run_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount ==3:
			run_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount ==4:
			run_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount ==5:
			run_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount ==6:
			run_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount ==7:
			run_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount ==8:
			run_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 9:
			smooth_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 10:
			smooth_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 11:
			smooth_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 12:
			smooth_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 13:
			river_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 14:
			river_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 15:
			river_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 16:
			river_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 17:
			smooth_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 18:
			smooth_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 19:
			smooth_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 20:
			smooth_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 21:
			river_rules()
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 22:	
			river_rules()
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 23:
			river_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 24:
			river_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 25:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 26:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 27:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 28:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 29:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 30:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 31:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 32:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 33:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 34:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 35:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 36:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 37:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 38:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 39:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 40:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 41:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 42:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 43:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 44:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 45:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 46:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 47:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 48:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 49:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 50:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 51:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 52:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 53:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 54:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 55:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 56:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 57:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 58:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 59:
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 60:
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 61:
			playerscreen.blit(swirl1,(250,10))
		if generationcount == 62:
			playerscreen.blit(swirl2,(250,10))
		if generationcount == 63:
			boulder_rules()
			playerscreen.blit(swirl3,(250,10))
		if generationcount == 64:
			boulder_rules()
			playerscreen.blit(swirl4,(250,10))
		if generationcount == 65:
			generationcount = 0
			generating = False
			print("done generating")
		else:
			pass
	if not generating and loading == True:
		savefile = open("worldsave.txt","r").readlines()
		for row in range (int(MAP_HEIGHT/CELL)):
			grid.append([])
			for column in range (int(MAP_WIDTH/CELL)):
				grid[row].append(savefile[column])
		
		loading = False
#           game loop start
	if not generating and loading == False:
		craft_check()
		cow.rect.x = cowx - mapx
		cow.rect.y = cowy - mapy
		if chestspawned == False:
			random1 = random.randint(1,round(MAP_WIDTH/CELL-5))
			random2 = random.randint(1,round(MAP_HEIGHT/CELL-5))
			if grid[random1][random2] != 0 and grid[random1][random2] != -1:
				grid[random1][random2] = 7
				chestspawned = True
#            counts
		watercount += 1
		grasscount += 1
		if watercount == 30:
			watercount = 0
		if grasscount == 80:
			grasscount = 0
#            spawn protection 
		if player.rect.x == 485 and player.rect.y == 275:
			position = (player.rect.x+15, player.rect.y+40)
			playercolumn = position[0] // CELL
			playerrow = position[1] // CELL
		if player.rect.x != 485 or player.rect.y != 275:
			position = (mapx+player.rect.x+15, mapy+player.rect.y+40)
			playercolumn = position[0] // CELL
			playerrow = position[1] // CELL
		if cellNumber(playerrow,playercolumn) != 1 and cellNumber(playerrow,playercolumn) != 2 and cellNumber(playerrow,playercolumn) != 3 and cellNumber(playerrow,playercolumn) != 4 and cellNumber(playerrow,playercolumn) != 5 and cellNumber(playerrow,playercolumn) != 6 and cellNumber(playerrow,playercolumn) != -50 and cellNumber(playerrow,playercolumn) != -51 and cellNumber(playerrow,playercolumn) != -52:
			mapx = playerbuffer[0]
			mapy = playerbuffer[1]
			player.rect.x = playerbuffer[2]
			player.rect.y = playerbuffer[3]
		if cellNumber(playerrow,playercolumn) == -100 and justspawned == True:
			mapx -= playerspeed
		cowlist = pygame.sprite.spritecollide(player,cowgroup,False)
		for cow in cowlist:
			mapx = playerbuffer[0]
			mapy = playerbuffer[1]
			player.rect.x = playerbuffer[2]
			player.rect.y = playerbuffer[3]
		if cellNumber(playerrow,playercolumn) != 1 and cellNumber(playerrow,playercolumn) != 2 and cellNumber(playerrow,playercolumn) != 3 and cellNumber(playerrow,playercolumn) != 4 and cellNumber(playerrow,playercolumn) != 5 and cellNumber(playerrow,playercolumn) != 6 and cellNumber(playerrow,playercolumn) != -50 and cellNumber(playerrow,playercolumn) != -51 and cellNumber(playerrow,playercolumn) != -52 and justspawned == True:
			mapx -= 5
		if cellNumber(playerrow,playercolumn) == 1 or cellNumber(playerrow,playercolumn) == 2 or cellNumber(playerrow,playercolumn) == 3 or cellNumber(playerrow,playercolumn) == 4 or cellNumber(playerrow,playercolumn) == 5 or cellNumber(playerrow,playercolumn) == 6 or cellNumber(playerrow,playercolumn) == -50 or cellNumber(playerrow,playercolumn) == -51 or cellNumber(playerrow,playercolumn) == -52:
			justspawned = False
		playerscreen.fill(BLACK)
#            viewport rects

		if mapy < 0:
			mapy = 0
		if mapx < 0:
			mapx = 0
		if mapy > MAP_HEIGHT - SCREEN_HEIGHT-15:
			mapy = MAP_HEIGHT - SCREEN_HEIGHT-15
		if mapx > MAP_WIDTH - SCREEN_WIDTH-15:
			mapx = MAP_WIDTH - SCREEN_WIDTH-15
#            display tiles
		
		for row in range(int(MAP_HEIGHT/CELL)):	
			for column in range(int(MAP_WIDTH/CELL)):
				if grid[row][column] == 0 or grid[row][column] == -1:
					if watercount < 10:
						playerscreen.blit(water,(column*CELL-mapx,row*CELL-mapy))
					if watercount > 9 and watercount < 20:
						playerscreen.blit(water2,(column*CELL-mapx,row*CELL-mapy))
					if watercount > 19 and watercount < 31:
						playerscreen.blit(water3,(column*CELL-mapx,row*CELL-mapy))
				if grid[row][column] == 1 and grasscount < 40:
					playerscreen.blit(grass, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 1 and grasscount >39:
					playerscreen.blit(grass22, (column*CELL-mapx, row*CELL-mapy))	
				if grid[row][column] == 2:
					playerscreen.blit(grass6, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 3:
					playerscreen.blit(grass3, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 4:
					playerscreen.blit(grass4, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 5:
					playerscreen.blit(grass5, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 6:
					playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 7:
					playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
					playerscreen.blit(chest, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 8:
					playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
					playerscreen.blit(stake, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == 9:
					playerscreen.blit(marker, (column*CELL-mapx, row*CELL-mapy))
					
				if grid[row][column] == 1000:
					playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
					if grasscount > -1 and grasscount < 21:
						playerscreen.blit(bush1, (column*CELL-mapx, row*CELL-mapy))
					if grasscount > 20 and grasscount < 41:
						playerscreen.blit(bush2, (column*CELL-mapx, row*CELL-mapy))
					if grasscount > 40 and grasscount < 60:
						playerscreen.blit(bush3, (column*CELL-mapx, row*CELL-mapy))
					if grasscount > 59 and grasscount < 81:
						playerscreen.blit(bush4, (column*CELL-mapx, row*CELL-mapy))
					
				if grid[row][column] == -50:
					if grasscount < 10 or grasscount > 70:
						playerscreen.blit(rock, (column*CELL-mapx, row*CELL-mapy))
					else:
						playerscreen.blit(rock222, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -51:
					if grasscount < 20 or grasscount > 60:
						playerscreen.blit(rock2, (column*CELL-mapx, row*CELL-mapy))
					else:
						playerscreen.blit(rock22, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -52:
					playerscreen.blit(rock3, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -100:
					playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
					playerscreen.blit(boulder, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -101:
					if shovel == True:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(base, (column*CELL-mapx, row*CELL-mapy))
					else:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(shovelbase, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -102:
					if sword == True:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(base, (column*CELL-mapx, row*CELL-mapy))
					else:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(swordbase, (column*CELL-mapx, row*CELL-mapy))
				if grid[row][column] == -103:
					if hoe == True:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(base, (column*CELL-mapx, row*CELL-mapy))
					else:
						playerscreen.blit(grass2, (column*CELL-mapx, row*CELL-mapy))
						playerscreen.blit(hoebase, (column*CELL-mapx, row*CELL-mapy))
#               SINGLE POINT ACTION/ TAP INPUT
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				if event.key == pygame.K_RETURN:
					savefile = open("worldsave.txt", "w")
					savefile.write(str(grid))
					print('saving...')
				if event.key == pygame.K_SPACE:
					print(len(craftinglist))
				if event.key == pygame.K_e:
					pass
				if event.key == pygame.K_TAB:
					crafting = True
				if event.key == pygame.K_F11:
					pygame.display.toggle_fullscreen()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					print(cellNumber(mousextile, mouseytile))
					tilePickup()
				if event.button == 3:
					tilePutdown(wheelposition)
				if event.button == 4:
					if not crafting:
						wheelposition = wheelposition - 1
					else:
						if craftingticker < len(craftinglist)-1 and craftingticker > -1:
							craftingticker = craftingticker - 1
						else:
							craftingticker =  craftingticker + 1
						

				if event.button == 5:
					if not crafting:
						wheelposition = wheelposition + 1
					else:
						if craftingticker < len(craftinglist)-1 and craftingticker > -1:
							craftingticker = craftingticker + 1
						else:
							craftingticker =  craftingticker - 1
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					player.standingUp()
				if event.key == pygame.K_s:
					player.standingDown()
				if event.key == pygame.K_a:
					player.standingLeft()
				if event.key == pygame.K_d:
					player.standingRight()
			
#           KEYPRESS EVENTS/ GET_PRESSED INPUT
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			left = False
			right = False
			up = True
			down = False
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
					
			playerbuffer.append(mapx)
			playerbuffer.append(mapy)
			playerbuffer.append(player.rect.x)
			playerbuffer.append(player.rect.y)
			if mapy == 0 or player.rect.y > 274:
				player.rect.y -= playerspeed
				player.moveUp()
			else:
				mapy -= playerspeed
				player.moveUp()
		elif keys[pygame.K_s]:
			left = False
			right = False
			up = False
			down = True
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
					
			playerbuffer.append(mapx)
			playerbuffer.append(mapy)
			playerbuffer.append(player.rect.x)
			playerbuffer.append(player.rect.y)
			if mapy == MAP_HEIGHT - SCREEN_HEIGHT-15 or player.rect.y < 276:
				player.rect.y += playerspeed
				player.moveDown()
			else:
				mapy += playerspeed
				player.moveDown()
		elif keys[pygame.K_a]:
			left = True
			right = False
			up = False
			down = False
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
					
			playerbuffer.append(mapx)
			playerbuffer.append(mapy)
			playerbuffer.append(player.rect.x)
			playerbuffer.append(player.rect.y)
			print(bunnygroup)
			if mapx == 0 or player.rect.x > 484:
				player.rect.x -= playerspeed
				player.moveLeft()
			else:
				mapx -= playerspeed
				player.moveLeft()
		elif keys[pygame.K_d]:
			left = False
			right = True
			up = False
			down = False
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
			playerbuffer.pop(0)
					
			playerbuffer.append(mapx)
			playerbuffer.append(mapy)
			playerbuffer.append(player.rect.x)
			playerbuffer.append(player.rect.y)
			if mapx == MAP_WIDTH - SCREEN_WIDTH-15 or player.rect.x < 486:
				player.rect.x += playerspeed
				player.moveRight()
			else:
				mapx += playerspeed
				player.moveRight()
		if keys[pygame.K_LSHIFT]:
			playerspeed = 6
		else:
			playerspeed = 3		
#         drawing and updating sprites
		
		cowgroup.draw(playerscreen)
		
		cowgroup.update()
		playergroup.draw(playerscreen)
		playergroup.update()	
		stick_group.draw(playerscreen)
		stick_item.rect.x = stickx - mapx
		stick_item.rect.y = stickx - mapy
		stick_group.update()
		daygroup.draw(playerscreen)
		draw_invtile()
		bunnygroup.draw(playerscreen)
		bunnygroup.update()
		bunnys.rect.x = bunnyx - mapx
		bunnys.rect.y = bunnyy - mapy
		for index in range(len(inventory)):
			inventoryPresent(index)
		stick_collision_list = pygame.sprite.spritecollide(player, stick_group, False)

		for i in stick_collision_list:
			stick_item.redraw()
			inventorybuffer.append("stick")
			stickx = random.randint(0, MAP_WIDTH - CELL)
			sticky = random.randint(0, MAP_HEIGHT - CELL)
		texts = str(Counter(inventorybuffer))
		render_text(texts, SCREEN_WIDTH/3, 0)
		daygroup.update()
		cowAI(600)
		invselector(wheelposition)
		if crafting:
			playerscreen.blit(craftselection, [player.rect.x - 22, player.rect.y - 78])
			craft_display(craftingticker)
		pygame.display.update()