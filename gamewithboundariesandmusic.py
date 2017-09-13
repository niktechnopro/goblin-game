# 1. Include pygame
# Include pygame which we got from pip
import pygame
import time
import random
# from the math module (built into python), get the fabs method
from math import fabs

# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()
pygame.mixer.init()
#start for music function
file = ('sounds/music.wav')

def music(f, n):
	pygame.mixer.music.load(f)
	pygame.mixer.music.play(n)

music (file, -1)
#end for music function

# 3. Create a screen with a particular size
# the screen size MUST be a tuple
screen = {"scr_height": 512, "scr_width": 480}
screen_size = (screen["scr_height"], screen["scr_width"])
# Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
# Set a pointless caption
pygame.display.set_caption("Goblin Chase")
# set up a var with our image
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')

# 8. Set up the hero location
hero = {
	"x": random.randint(100, 400),
	"y": random.randint(50, 480),
	"speed": 15,
	"wins": 0,
	"loses": 0
}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 1
}

monster = {
	"x": random.randint(150, 400),
	"y": random.randint(150, 480),
	"speed": 1
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

# 4. Create a game loop (while)
# Create a boolean for whether the game should be going or not
game_on = True
while game_on:
	
	# we are inside the main game loop.
	# it will keep running, as long as our bool is true
	# 5. Add a quit event (Python needs an escape)
	# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			# the user clicked the red x in the top left
			game_on = False
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			if event.key == keys['up']:
				# user pressed up!!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys['down']:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys['left']:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			elif event.key == keys['right']:
				# hero['x'] += hero['speed']
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# the user let go of a key. See if it's one that matters
			if event.key == keys['up']:
				# user let go of the upkey. Flip the bool
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False


	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']


	#screen boundaries for hero
	if hero["x"] < 0:
		hero["x"] += 10
	elif hero["x"] > screen["scr_width"] - 10:
		hero["x"] = screen["scr_width"] - 10
	elif hero["y"] < 0:
		hero["y"] = 10
	elif hero["y"] > screen["scr_height"] - 70:
		hero["y"] = screen["scr_height"] - 70


	#collision event
	def collision(sound, wilo):
		print "collision!"
		hero[wilo] += 1
		pygame.mixer.music.pause()
		music(sound, 0)
		time.sleep(2.0)
		music(file, -1)



	# COLLISION DETECTION!!!
	distance_between_goblin = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	distance_between_monster = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if distance_between_monster < 32:
		# the hero and goblin are touching!
		collision('sounds/lose.wav', 'loses')
	elif distance_between_goblin < 32:
		collision('sounds/win.wav', 'wins')
	else:
		print "not touching"



	#goblin movement
	
	if (hero['x'] > goblin['x']):
		goblin['x'] -= goblin['speed']
	else:
		goblin['x'] += goblin['speed']
	if (hero['y'] < goblin['y']):
		goblin['y'] += goblin['speed']
	else:
		goblin['y'] -= goblin['speed']

	#monster movement
	if (hero['x'] > monster['x']):
		monster['x'] += monster['speed']
	else:
		monster['x'] -= monster['speed']
	if (hero['y'] < monster['y']):
		monster['y'] -= monster['speed']
	else:
		monster['y'] += monster['speed']
	

	# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you watn you to draw it
	pygame_screen.blit(background_image, [0,0])

	# Make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	#text for wins
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])
	#text for loses
	wins_text = font.render("Loses: %d" % (hero['loses']), True, (0,0,0))
	pygame_screen.blit(wins_text,[400,400])

	
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	pygame_screen.blit(monster_image, [monster['x'], monster['y']])

	# 7. Repeat 6 over and over over...
	pygame.display.flip()
