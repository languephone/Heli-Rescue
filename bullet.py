import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the chopper."""

	def __init__(self, hr_game):
		"""Create a bullet object at the chopper's current position."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet rect at (0,0) and then set correct position.
		self.rect = pygame.Rect(0,0, self.settings.bullet_width, 
			self.settings.bullet_height)
		self.rect.x = hr_game.chopper.rect.right
		self.rect.y = hr_game.chopper.rect.centery + 20

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.x += self.settings.bullet_speed
		# Update the rect position.
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)