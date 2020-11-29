class GameStats:
	"""Track Statistics for Heli Rescue."""
	def __init__(self, hr_game):
		"""Initialize statistics."""
		self.settings = hr_game.settings
		self.reset_stats()

		# Start Heli Rescue in an inactive state.
		self.game_active = False

		# Game tracking flags
		self.spacebar_pressed = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.choppers_left = self.settings.chopper_limit
		self.score = 0