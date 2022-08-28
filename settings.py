class Settings:
	"""A class to store all settings for Heli Rescue."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (135, 206, 235)
		self.bg_image = 'images/sunset_gradient.png'

		# Chopper settings
		self.chopper_speed = 8
		self.chopper_max_tilt = 8
		self.chopper_tilt_speed = 1
		self.chopper_limit = 3

		# Bullet settings
		self.bullet_speed = 20
		self.bullet_width = 15
		self.bullet_height = 4
		self.bullet_color = (60, 60, 60)
		self.bullet_firing_threshold = 4
		self.bullet_damage = 1

		# Asteroid Settings
		self.asteroid_speed = 4
		self.asteroid_offset = 1500
		self.asteroid_health = 5
		self.asteroid_max_count = 4

		# Alien Settings
		self.alien_speed = 6
		self.alien_health = 10

		# Cloud Settings
		self.cloud_offset = 1500
		self.cloud_speed = 2
		self.cloud_max_speed = 6
		self.cloud_max_count = 3
		self.cloud_maximum_y = int(self.screen_height / 2)

		# Shockwave Settings
		self.shockwave_radius = 20
		self.shockwave_border_width = 8
		self.shockwave_colour = (81, 69, 69)
		self.shockwave_growth_speed = 10
		self.shockwave_border_decay_speed = 0.2
		
		# ParticleBreak Settings
		self.particle_radius = 7
		self.particle_decay_speed = 0.2
		self.particle_colour = (81, 69, 69)
		self.particle_movement_speed = 8
		self.particle_count = 30

		# Spark Settings
		self.spark_radius = 5
		self.spark_decay_speed = 0.2
		self.spark_colour = (243, 190, 51)
		self.spark_movement_speed = 10
		self.spark_count = 1

		# Smoke Settings
		self.smoke_radius = 10
		self.smoke_colour = (81, 69, 69)
		self.smoke_growth_speed = 0.5
		self.smoke_movement_speed = 10
		self.smoke_max_radius = 50
		self.smoke_emitting_threshold = 100

		# Scoring
		self.asteroid_points = 10

		# Menu Settings
		self.font_size = 48
		self.font_family = 'Impact'