import pygame
from pygame.sprite import Sprite
from random import randint

class Cloud(Sprite):
	"""A class to represent clouds on the screen."""
	def __init__(self, hr_game):
		"""Initialize the cloud and set its starting position."""
		super().__init__()
		self.screen = hr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = hr_game.settings

		# Load the cloud image and set its rect attribute.
		self.image = pygame.image.load('images/cloud5.png').convert_alpha()
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()

		# Start each new cloud in a random vertical space on the right of the screen
		self.rect.x = randint(self.settings.screen_width, self.settings.screen_width
						 + self.settings.cloud_offset)
		self.rect.y = randint(0, self.settings.cloud_maximum_y)

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Assign a speed between min and max
		self.speed = randint(1, self.settings.cloud_max_speed)

	def update(self):
		"""Move the cloud to the left"""
		self.x -= self.speed
		self.rect.x = self.x

	def move_up(self):
		"""Move the cloud up off the screen."""
		if self.y > 0 - self.rect.height:
			self.y -= self.settings.asteroid_speed
			self.rect.y = int(self.y)

		# Remove any clouds that are off-screen
		if self.y <= -self.rect.height:
			self.kill()

class Ground(Sprite):
	"""A class to create and manage a finished floor to land on."""
	def __init__(self, hr_game):
		"""Initialize a floor tile and set its position."""
		
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		
		# Load the image and set a rect attribute.
		self.image = pygame.image.load('images/ground_tile.png').convert_alpha()
		self.rect = self.image.get_rect()

		# Store the tile's exact vertical position.
		self.y = float(self.rect.y)


	def update(self):
		"""Move the tile up."""
		self.y += self.settings.ground_speed * self.settings.ground_direction
		self.rect.y = int(self.y)


