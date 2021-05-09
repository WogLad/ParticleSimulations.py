import pygame
import math

from pygame import Vector2, Color

background_colour = (20,20,20)

screen_width = 200
screen_height = 200

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Particle Simulations")
screen.fill(background_colour)

pygame_colors = {
	"red": Color(255,0,0),
	"green": Color(0,255,0),
	"blue": Color(0,0,255),
	"pink": Color(255,0,255),
	"yellow": Color(255,255,0),
	"black": Color(0,0,0),
	"white": Color(255,255,255),
	"grey": Color(127,127,127),
}

pixel_map = [ [0 for x in range(screen_width)] for y in range(screen_height) ]

pygame.display.flip()

running = True

clock = pygame.time.Clock()

last_placed_pixel_x_pos = 0

# Spawns in a 25x25 block of sand.
# for g in range(25):
# 	for h in range(25):
# 		pixel_map[(g+88)][h] = 1

# Spawns in a 25x25 block of water.
for g in range(100):
	for h in range(100):
		pixel_map[(g+50)][h] = 2

while running:
	mouse_pos = pygame.mouse.get_pos()

	for event in pygame.event.get(): #Stops the game processes if the game is closed.
		if event.type == pygame.QUIT:
			running = False

	screen.fill(background_colour)

	# Drawing All the pixels
	if pygame.mouse.get_pressed()[0] == True:
		pixel_map[(mouse_pos[0]+last_placed_pixel_x_pos)][mouse_pos[1]] = 1
		if last_placed_pixel_x_pos == 0:
			last_placed_pixel_x_pos = -1
		else:
			last_placed_pixel_x_pos = 0

	if pygame.mouse.get_pressed()[2] == True:
		pixel_map[(mouse_pos[0]+last_placed_pixel_x_pos)][mouse_pos[1]] = 2
		if last_placed_pixel_x_pos == 0:
			last_placed_pixel_x_pos = -1
		else:
			last_placed_pixel_x_pos = 0

	if pygame.mouse.get_pressed()[1] == True:
		pixel_map[mouse_pos[0]][mouse_pos[1]] = 0

	y = (screen_height-1)
	while y > -1:
		x = (screen_width-1)
		while x > -1:
			if y < (screen_height-1) and pixel_map[x][y] > 0:
				if pixel_map[x][y] == 1:
					if pixel_map[x][(y+1)] == 0: # Down
						pixel_map[x][(y+1)] = 1
						pixel_map[x][y] = 0
					elif (x > 0) and (pixel_map[(x-1)][(y+1)] == 0): # Bottom Left
						pixel_map[(x-1)][(y+1)] = 1
						pixel_map[x][y] = 0
					elif (x < (screen_width-1)) and (pixel_map[(x+1)][(y+1)] == 0): # Bottom Right
						pixel_map[(x+1)][(y+1)] = 1
						pixel_map[x][y] = 0
				elif pixel_map[x][y] == 2:
					if pixel_map[x][(y+1)] == 0: # Down
						pixel_map[x][(y+1)] = 2
						pixel_map[x][y] = 0
					elif (x > 0) and (pixel_map[(x-1)][(y+1)] == 0): # Bottom Left
						pixel_map[(x-1)][(y+1)] = 2
						pixel_map[x][y] = 0
					elif (x < (screen_width-1)) and (pixel_map[(x+1)][(y+1)] == 0): # Bottom Right
						pixel_map[(x+1)][(y+1)] = 2
						pixel_map[x][y] = 0
					elif (x > 0) and (pixel_map[(x-1)][y] == 0): # Left
						pixel_map[(x-1)][y] = 2
						pixel_map[x][y] = 0
					elif (x < (screen_width-1)) and (pixel_map[(x+1)][y] == 0): # Right
						pixel_map[(x+1)][y] = 2
						pixel_map[x][y] = 0
			x -= 1
		y -= 1

	for y in range(len(pixel_map)):
		for x in range(len(pixel_map[y])):
			if pixel_map[x][y] == 1:
				pygame.draw.rect(screen, pygame_colors["yellow"], pygame.Rect(x, y, 1, 1))
			elif pixel_map[x][y] == 2:
				pygame.draw.rect(screen, Color(0, 255, 255), pygame.Rect(x, y, 1, 1))

	# for pixel in sand_pixels:
	# 	pygame.draw.rect(screen, pygame_colors["yellow"], pygame.Rect(pixel["x"], pixel["y"], 1, 1))

	pygame.display.update()
	clock.tick()

	print("FPS:", math.floor(clock.get_fps()))