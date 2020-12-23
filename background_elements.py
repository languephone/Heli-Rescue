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
		for cloud in self.clouds:
			if cloud.y > 0 + cloud.rect.height:
				cloud.y -= self.settings.asteroid_speed
				cloud.rect.y = int(cloud.y)

		for cloud in self.clouds.copy():
			if cloud.y <= -cloud.rect.height:
				self.clouds.remove(cloud)