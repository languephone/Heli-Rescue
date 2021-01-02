import csv, time
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien."""

	def __init__(self, x_position, y_position, direction, hr_game):
		"""Initialize the alien and set its attributes."""
		super().__init__()

		# Set image and create rect from image
		self.image = pygame.image.load('images/spaceship3.png').convert_alpha()
		self.image_rect = self.image.get_rect()

		# Set position and direction
		self.x = hr_game.settings.screen_width
		self.y = int(y_position)
		self.direction = int(direction)

		# Set health
		self.health = ai_game.settings.alien_health

	def update(self):
		"""Move the alien to the left."""
		self.x -= ai_game.settings.alien_speed
		self.image_rect.x = int(self.x)
	


filename = 'enemy_map.csv'
with open(filename, encoding='utf-8-sig') as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get list of values from the file.
	aliens = []
	for row in reader:
		alien = {}
		for i in range(len(header_row)):
			alien[header_row[i]] = row[i]
		aliens.append(alien)

	#print(aliens)

	start_values = []
	for alien in aliens:
		start_values.append(int(alien['Start']))


alien_test_list = []

# Start timer------------
t0 = time.time()

max_x = max(start_values)

x = 0

while x <= max_x:
	if start_values[0] <= x:
		for i in range(len(start_values.copy())):
			if start_values[i] <= x:
				alien_test_list.append(aliens.pop(i))
				start_values.remove(start_values[i])
				break

	x += 1

# End timer--------------
t1 = time.time()

total_time = t1 - t0
print(total_time)
#print(alien_test_list)