import csv, time
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien."""

	def __init__(self, x_position, y_position, direction, hr_game):
		"""Initialize the alien and set its attributes."""
		super().__init__()
		self.settings = hr_game.settings

		# Set image and create rect from image
		self.image = pygame.image.load('images/spaceship3.png').convert_alpha()
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()

		# Set position and direction
		self.x = x_position
		self.y = int(y_position)
		self.direction = int(direction)
		self.rect.x, self.rect.y = int(self.x), int(self.y)

		# Alien attributes
		self.health = self.settings.alien_health
		self.speed = self.settings.alien_speed

		# Sound effects
		self.explosion_sound = pygame.mixer.Sound('sounds/explosion2.ogg')

	def update(self):
		"""Move the alien to the left."""
		self.x -= self.speed
		self.rect.x = int(self.x)


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
	#print(start_values)


alien_test_list = []

# Start timer------------
t0 = time.time()

max_x = max(start_values)

x = 0

while x <= max_x:
	if start_values[0] <= x:
		for start_value in start_values.copy():
			if start_value <= x:
				alien_created = aliens.pop(0)
				#print(f"{x}:creating alien {alien_created} at from start value {start_value}")
				alien_test_list.append(alien_created)
				start_values.remove(start_value)
			elif start_value > x:
				break

	x += 1

# End timer--------------
t1 = time.time()

total_time = t1 - t0
print(total_time)
# print(len(aliens))
# print(len(start_values))