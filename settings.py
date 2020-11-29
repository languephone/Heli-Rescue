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
		self.chopper_incline = 10
		self.chopper_limit = 3

		# Bullet settings
		self.bullet_speed = 10
		self.bullet_width = 20
		self.bullet_height = 6
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
		self.cloud_max_count = 3