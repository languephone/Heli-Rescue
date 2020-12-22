import pygame
from pygame.sprite import Sprite
from random import randint

class Shockwave(Sprite):
	"""A class to manage shockwaves generated by explosions."""

	def __init__(self, hr_game, pos_x, pos_y, colour='white'):
		"""Create a shockwave at a specified origin point."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		self.radius = self.settings.shockwave_radius
		self.border_width = self.settings.shockwave_border_width
		self.colour = colour
		self.pos_x = pos_x
		self.pos_y = pos_y

	def update(self):
		"""Expand the radius of the circle whilst shrinking border width."""
		self.radius += self.settings.shockwave_growth_speed
		self.border_width -= self.settings.shockwave_border_decay_speed
				
	def draw_wave(self):
		"""Draw the wave using its current size/border"""
		pygame.draw.circle(self.screen, self.colour, (self.pos_x, self.pos_y),
					self.radius, int(self.border_width))

class ParticleBreak(Sprite):
	"""A class to manage objects breaking up into particles."""

	def __init__(self, hr_game, pos_x, pos_y, colour='white'):
		"""Create a particle at a specified origin point."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		self.radius = self.settings.particle_radius
		self.colour = colour
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.direction_x = randint(-self.settings.particle_movement_speed,
			self.settings.particle_movement_speed)
		self.direction_y = randint(-self.settings.particle_movement_speed,
			self.settings.particle_movement_speed)

	def update(self):
		"""Reduce the radius of the circle and move along x/y axis."""
		self.radius -= self.settings.particle_decay_speed
		self.pos_x += self.direction_x
		self.pos_y += self.direction_y

	def draw_particle(self):
		"""draw the particle using its current size/location."""
		self.rect = (self.pos_x, self.pos_y, self.radius, self.radius)
		pygame.draw.rect(self.screen, self.colour, self.rect)

class Smoke(Sprite):
	"""A classs to manage smoke effects on damage and victory."""

	def __init__(self, hr_game, pos_x, pos_y, colour='white'):
		"""Create a smoke bubble at a specified origin point."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		self.radius = self.settings.smoke_radius
		self.colour = colour
		self.pos_x = pos_x
		self.pos_y = pos_y

	def update(self):
		"""Expand the radius of the circle whilst shrinking border width."""
		self.radius += self.settings.smoke_growth_speed
		self.pos_x -= self.settings.smoke_movement_speed
				
	def draw_smoke(self):
		"""Draw the smoke cloud using its current size/position"""
		pygame.draw.circle(self.screen, self.colour, (self.pos_x, self.pos_y),
					self.radius)

class Sparks(Sprite):
	"""A class to manage sparks."""

	def __init__(self, hr_game, pos_x, pos_y, colour='white'):
		"""Create a particle at a specified origin point."""
		super().__init__()
		self.screen = hr_game.screen
		self.settings = hr_game.settings
		self.radius = self.settings.spark_radius
		self.colour = colour
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.speed_x = randint(-self.settings.spark_movement_speed,
			self.settings.spark_movement_speed)
		self.speed_y = randint(-self.settings.spark_movement_speed,
			0)
		self.gravity = 0.15

	def update(self):
		"""Reduce the radius of the circle and move along x/y axis."""
		self.radius -= self.settings.spark_decay_speed
		self.pos_x += self.speed_x
		self.pos_y += self.speed_y
		self.speed_y += self.gravity

	def draw_spark(self):
		"""draw the spark using its current size/location."""
		self.rect = (self.pos_x, self.pos_y, self.radius, self.radius / 2)
		pygame.draw.rect(self.screen, self.colour, self.rect)
