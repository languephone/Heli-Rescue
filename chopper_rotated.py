import pygame

class Chopper:
	"""A class to manage the chopper."""

	def __init__(self, hr_game):
		"""Initialize the chopper and set its starting position."""
		self.screen = hr_game.screen
		self.screen_rect = hr_game.screen.get_rect()
		self.settings = hr_game.settings

		# Load the chopper image and get its rect.
		self.images = []
		for i in range(8):
			self.images.append(pygame.image.load(
				f'images/helicopter_{i+1}.png').convert_alpha())
		self.current_image = 0
		self.image = self.images[self.current_image]
		self.rotated_image = pygame.transform.rotozoom(self.image, 0, 3)
		self.rect = self.rotated_image.get_rect()
		self.hitbox = pygame.Rect(0, 0, 96, 63)
		
		# Start each new chopper below the center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.y = self.screen_rect.bottom

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
		self.crash_sound = pygame.mixer.Sound('sounds/explosion1.ogg')
		self.gun_sound = pygame.mixer.Sound('sounds/shot.wav')

	def update(self):
		"""Update position and rotation of chopper."""
		self._move_chopper()
		self._animate_chopper()
		self._rotate_chopper()
		self.rect = self.rotated_image.get_rect()
		self.rect.centerx = int(self.centerx)
		self.rect.centery = int(self.centery)
		self.hitbox.centerx = self.rect.centerx + 40
		self.hitbox.centery = self.rect.centery + 10

		# Update the bullet firing state
		if self.firing_bullets:
			self.bullet_firing_state += 1

	def _move_chopper(self):
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

	def _rotate_chopper(self):
		if self.moving_right and (self.tilt > 
				self.settings.chopper_max_tilt * -1):
			self.tilt -= self.settings.chopper_tilt_speed
		elif self.moving_left and (self.tilt < 
				self.settings.chopper_max_tilt):
			self.tilt += self.settings.chopper_tilt_speed
		else:
			if not self.moving_right and self.tilt < 0:
				self.tilt += self.settings.chopper_tilt_speed
			elif not self.moving_left and self.tilt > 0:
				self.tilt -= self.settings.chopper_tilt_speed
		self.rotated_image = pygame.transform.rotozoom(self.image, 
														self.tilt, 3)

	def _animate_chopper(self):
		self.current_image += 0.25
		if self.current_image >= len(self.images):
			self.current_image = 0
		self.image = self.images[int(self.current_image)]

	def blitme(self):
		"""Draw the chopper at its current location."""
		self.screen.blit(self.rotated_image, self.rect)
		pygame.draw.rect(self.screen, 'Red', self.rect, 2)
		pygame.draw.rect(self.screen, 'Green', self.hitbox, 2)

	def center_chopper(self):
		"""Center the chopper on the screen."""
		self.centery -= self.settings.chopper_speed / 2
		self.rect.centery = int(self.centery)
		self._animate_chopper()
		self._rotate_chopper()