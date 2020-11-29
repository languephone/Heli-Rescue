import pygame

class Chopper:
	"""A class to manage the chopper."""

	def __init__(self, hr_game):
		"""Initialize the chopper and set its starting position."""
		self.screen = hr_game.screen
		self.screen_rect = hr_game.screen.get_rect()
		self.settings = hr_game.settings

		# Load the ship image and get its rect.
		self.image = pygame.transform.scale(pygame.image.load(
				'images/chopper.png'), (200, 103)).convert_alpha()
		self.rotated_image = pygame.transform.rotozoom(self.image, 0, 1)
		self.rect = self.rotated_image.get_rect()
		
		# Start each new chopper below the center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.bottom + 100

		# Store a decimal x & y value for the chopper's actual position
		self.centerx, self.centery = float(self.rect.centerx), float(self.rect.centery)

		# Movement Flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Rotation Flags
		self.tilt = 0
		self.rotation_point = 238
		
		# Bullet Status Flags
		self.firing_bullets = False
		self.bullet_firing_state = 0

		# Sound effects
		self.motor_sound = pygame.mixer.Sound('sounds/chopper.wav')

	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's x/y value, not the rect.
		if self.moving_right and self.rect.left < (self.screen_rect.right - 50):
			self.centerx += self.settings.chopper_speed
		if self.moving_left and self.rect.right > 50:
			self.centerx -= self.settings.chopper_speed
		if self.moving_down and self.rect.top < (self.screen_rect.bottom - 50):
			self.centery += self.settings.chopper_speed
		if self.moving_up and self.rect.bottom > 50:
			self.centery -= self.settings.chopper_speed

		self._rotate_chopper()
		self.rect = self.rotated_image.get_rect()
		self.rect.centerx = int(self.centerx)
		self.rect.centery = int(self.centery)

		# Update the bullet firing state
		if self.firing_bullets:
			self.bullet_firing_state += 1

		print(self.centery, self.rect.centery, self.centerx, self.rect.centerx)

	def _rotate_chopper(self):
		if self.moving_right and (self.tilt > 
				self.settings.chopper_max_tilt * -1):
			self.tilt -= 1
		elif self.moving_left and (self.tilt < 
				self.settings.chopper_max_tilt):
			self.tilt += 1
		self.rotated_image = pygame.transform.rotozoom(self.image, 
														self.tilt, 1)

	def blitme(self):
		"""Draw the chopper at its current location."""
		self.screen.blit(self.rotated_image, self.rect)

	def center_chopper(self):
		"""Center the chopper on the screen."""
		self.centery -= self.settings.chopper_speed / 2
		self.rect.centery = float(self.centery)