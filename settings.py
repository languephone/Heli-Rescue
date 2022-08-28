class Settings:
	"""A class to store all settings for Heli Rescue."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (135, 206, 235)
		self.bg_image = 'images/sunset_gradient.png'

		self.framerate = 120

		# Cloud Settings
		self.cloud_offset = 500
		self.cloud_speed = 1 / self.framerate * 60
		self.cloud_max_speed = 1 / self.framerate * 360
		self.cloud_max_count = 3
		self.cloud_maximum_y = int(self.screen_height / 2)