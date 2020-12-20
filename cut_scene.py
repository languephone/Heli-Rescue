class CutScene():
	"""A class to manage cut scenes."""

	def __init__(self, name, hr_game):
		"""Initialize the cut scene."""
		self.name = name
		self.screen = hr_game.screen
		self.screen_rect = hr_game.screen.get_rect()
		self.chopper = hr_game.chopper
		self.settings = hr_game.settings
		self.vertical_offset = 
		self.horizontal_offset = 

	def temp_loop(self):
		"""A temporary loop to run the scene."""
		while True:
			hr_game._check_events()
			self.update()
			hr_game._update_screen()
			hr_game.clock.tick(120)

	def update(self):
		"""The actions of the cut scene."""
		while self.chopper.center != self.chopper.screen_rect.center:
			self.chopper.centery -= self.settings.chopper_speed / 2
			self.rect.centery = int(self.centery)
			self.hitbox.centerx = self.rect.centerx + 26
			self.hitbox.centery = self.rect.centery + 6
			self._animate_chopper()
			self._rotate_chopper()