import pygame
from pygame.sprite import Sprite
from random import choice, randint

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
		self.image = pygame.transform.scale(pygame.image.load(
				choice(self.image_bank)), (90, 80)).convert_alpha()
		self.rect = self.image.get_rect()

		# Start each new asteroid in a random vertical space on the right of the screen
		self.rect.x = randint(self.settings.screen_width,
					self.settings.screen_width + self.settings.asteroid_offset)
		self.rect.y = randint(0, self.settings.screen_height - self.rect.height)

		# maintain exact position of asteroid
		self.x = float(self.rect.x)

		# Create separate (smaller) rect for the hitbox
		self.hitbox = self.rect.inflate(-24, -24)

		# Asteroid attributes
		self.health = self.settings.asteroid_health
		self.speed = self.settings.asteroid_speed

		# Sound effects
		self.explosion_sound = pygame.mixer.Sound('sounds/explosion2.ogg')

	def update(self):
		"""Move the asteroid to the left and rotate."""
		# Set rotation
		# self.rotation += 10
		# self.rotated_image = pygame.transform.rotozoom(self.image, self.rotation, 1)
		
		# Move to left
		self.x -= self.speed
		self.rect.x = int(self.x)
		self.hitbox.center = self.rect.center
