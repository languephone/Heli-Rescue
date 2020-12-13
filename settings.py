class Settings:
	"""A class to store all settings for Heli Rescue."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.small_screen_size = (self.screen_width // 2, self.screen_height // 2)
		self.small_screen_width = self.small_screen_size[0]
		self.small_screen_height = self.small_screen_size[1]
		self.bg_color = (135, 206, 235)
		self.bg_image = 'images/sunset_gradient.png'

		# Chopper settings
		self.chopper_speed = 2
		self.chopper_max_tilt = 8
		self.chopper_tilt_speed = 0.5
		self.chopper_limit = 3

		# Bullet settings
		self.bullet_speed = 5
		self.bullet_width = 10
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullet_firing_threshold = 8
		self.bullet_damage = 1

		# Asteroid Settings
		self.asteroid_speed = 1
		self.asteroid_offset = 750
		self.asteroid_health = 5
		self.asteroid_max_count = 4

		# Cloud Settings
		self.cloud_offset = 750
		self.cloud_speed = 1
		self.cloud_max_speed = 3
		self.cloud_max_count = 3
		self.cloud_maximum_y = int(self.screen_height / 2)

		# Shockwave Settings
		self.shockwave_radius = 10
		self.shockwave_border_width = 4
		self.shockwave_colour = (81, 69, 69)
		self.shockwave_growth_speed = 5
		self.shockwave_border_decay_speed = 0.1
		
		# ParticleBreak Settings
		self.particle_radius = 8
		self.particle_decay_speed = 0.15
		self.particle_colour = (81, 69, 69)
		self.particle_movement_speed = 2
		self.particle_count = 15

		# Smoke Settings
		self.smoke_radius = 3
		self.smoke_colour = (81, 69, 69)
		self.smoke_growth_speed = 0.12
		self.smoke_movement_speed = 2.5
		self.smoke_max_radius = 15
		self.smoke_emitting_threshold = 30

		# Scoring
		self.asteroid_points = 10