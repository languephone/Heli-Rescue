import pygame
from pygame.sprite import Sprite
from random import randint

class Asteroid(Sprite):
	"""A class to represent a single asteroid in a field of asteroids."""
	def __init__(self, hr_game):
		"""Initialize the asteroid and set its starting position."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings

		# Load the asteroid image and set its rect attribute.
		self.image_bank = ['images/asteroid_4.png', 'images/asteroid_2.png',
						'images/asteroid_3.png']
		self.random_index = randint(0, 2)
		self.image = pygame.transform.scale(pygame.image.load(
				self.image_bank[self.random_index]), (90, 80)).convert_alpha()
		self.rect = self.image.get_rect()

		# Start each new asteroid in a random vertical space on the right of the screen
		self.rect.x = randint(self.settings.screen_width, self.settings.screen_width
						 + self.settings.asteroid_offset)
		self.rect.y = randint(0, self.settings.screen_height - self.rect.height)

		self.x = float(self.rect.x)

		# Asteroid attributes
		self.health = self.settings.asteroid_health

		# Sound effects
		self.explosion_sound = pygame.mixer.Sound('sounds/explosion2.ogg')

	def update(self):
		"""Move the asteroid to the left and rotate."""
		# Set rotation
		# self.rotation += 10
		# self.rotated_image = pygame.transform.rotozoom(self.image, self.rotation, 1)
		
		# Move to left
		self.x -= self.settings.asteroid_speed
		self.rect.x = int(self.x)