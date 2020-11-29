import pygame
from pygame.sprite import Sprite
from random import randint

class Cloud(Sprite):
	"""A class to represent clouds on the screen."""
	def __init__(self, hr_game):
		"""Initialize the cloud and set its starting position."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings

		# Load the cloud image and set its rect attribute.
		self.image = pygame.image.load('images/cloud_5.png').convert_alpha()
		self.rect = self.image.get_rect()

		# Start each new cloud in a random vertical space on the right of the screen
		self.rect.x = randint(self.settings.screen_width, self.settings.screen_width
						 + self.settings.asteroid_offset)
		self.rect.y = randint(0, self.settings.screen_height - self.rect.height)

		self.x = float(self.rect.x)

		# Asteroid attributes
		self.health = self.settings.asteroid_health

	def update(self):
		"""Move the asteroid to the left and rotate."""
		# Set rotation
		# self.rotation += 10
		# self.rotated_image = pygame.transform.rotozoom(self.image, self.rotation, 1)
		
		# Move to left
		self.x -= self.settings.asteroid_speed
		self.rect.x = self.x