class CutScene():
	"""A class to manage cut scenes."""

	def __init__(self, name, hr_game):
		"""Initialize the cut scene."""
		self.name = name
		self.hr_game = hr_game
		self.screen = hr_game.screen
		self.screen_rect = hr_game.screen.get_rect()
		self.chopper = hr_game.chopper
		self.settings = hr_game.settings
		self.active = False

	def temp_loop(self):
		"""A temporary loop to run the scene."""
		while self.active:
			
			# Continue to check for 'quit' events
			self.hr_game._check_events()
			
			# Run cut scene
			self.update()
			
			# Update on-screen items so that they do not appear to freeze
			self.hr_game._update_bullets()
			self.hr_game._update_asteroids()
			self.hr_game._update_shockwaves()
			self.hr_game._update_particles()
			self.hr_game._generate_smoke(self.chopper)
			self.hr_game._update_smoke()
			self.hr_game._update_clouds()
			self.hr_game._check_tutorial_prompts()

			self.hr_game._update_screen()
			self.hr_game.clock.tick(120)

	def update(self):
		"""The actions of the cut scene."""
		self.chopper.center_chopper()

		if self.chopper.rect.center == ((self.settings.screen_width / 2, self.settings.screen_height / 2)):
		
			# Move clouds up off the screen.
			if self.hr_game.clouds or self.hr_game.asteroids:
				for cloud in self.hr_game.clouds.copy():
					cloud.move_up()

				for asteroid in self.hr_game.asteroids.copy():
					asteroid.move_up()
			
			# End CutScene when all elements have been removed from the screen.
			else:
				self.active = False


	def landing(self):
		"""Create a scene where the chopper lands."""
		
		# Move all sprite groups up off the screen
		#self.hr_game.bullets.move_up()
		#self.hr_game.asteroids.move_up()
		self.hr_game.clouds.move_up()