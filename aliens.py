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