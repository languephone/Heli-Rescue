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
		self.chopper_speed = 4
		self.chopper_max_tilt = 8
		self.chopper_tilt_speed = 0.5
		self.chopper_limit = 3

		# Bullet settings
		self.bullet_speed = 10
		self.bullet_width = 15
		self.bullet_height = 4
		self.bullet_color = (60, 60, 60)
		self.bullet_firing_threshold = 8
		self.bullet_damage = 1

		# Asteroid Settings
		self.asteroid_speed = 2
		self.asteroid_offset = 1500
		self.asteroid_health = 5
		self.asteroid_max_count = 4

		# Cloud Settings
		self.cloud_offset = 1500
		self.cloud_speed = 1
		self.cloud_max_speed = 3
		self.cloud_max_count = 3
		self.cloud_maximum_y = int(self.screen_height / 2)

		# Shockwave Settings
		self.shockwave_radius = 20
		self.shockwave_border_width = 8
		self.shockwave_colour = (81, 69, 69)
		self.shockwave_growth_speed = 5
		self.shockwave_border_decay_speed = 0.1
		
		# ParticleBreak Settings
		self.particle_radius = 12
		self.particle_decay_speed = 0.15
		self.particle_colour = (81, 69, 69)
		self.particle_movement_speed = 4
		self.particle_count = 15

		# Spark Settings
		self.spark_radius = 5
		self.spark_decay_speed = 0.1
		self.spark_colour = (243, 190, 51)
		self.spark_movement_speed = 5
		self.spark_count = 3

		# Smoke Settings
		self.smoke_radius = 10
		self.smoke_colour = (81, 69, 69)
		self.smoke_growth_speed = 0.25
		self.smoke_movement_speed = 5
		self.smoke_max_radius = 50
		self.smoke_emitting_threshold = 50

		# Scoring
		self.asteroid_points = 10