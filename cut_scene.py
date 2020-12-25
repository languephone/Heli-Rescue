import pygame
from background_elements import Ground

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
		self.ground = pygame.sprite.Group()
		self._create_floor()

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

			self._update_screen()

			self.hr_game.clock.tick(120)

	def update(self):
		"""The actions of the cut scene."""
		self.chopper.center_chopper()

		if self.chopper.rect.center == ((self.screen_rect.width / 2, 
									self.screen_rect.height / 2)):
		
			# Move clouds up off the screen.
			if self.hr_game.clouds or self.hr_game.asteroids:
				for cloud in self.hr_game.clouds.copy():
					cloud.move_up()

				for asteroid in self.hr_game.asteroids.copy():
					asteroid.move_up()
			
			# End CutScene when all elements have been removed from the screen.
			
			else:
				self.active = False
	
	def _create_ground_tile(self, tile_number):
		"""Create a single tile and place it in a row."""

		ground_tile = Ground(self.hr_game)
		ground_tile_width, ground_tile_height = ground_tile.rect.size
		
		ground_tile.x = ground_tile_width * tile_number
		ground_tile.rect.x = ground_tile.x
		ground_tile.rect.y = self.screen_rect.height - ground_tile_height

		self.ground.add(ground_tile)


	def _create_floor(self):
		"""Create a floor from ground tiles."""

		# Create a floor tile and find the number of tiles needed
		ground_tile = Ground(self.hr_game)
		ground_tile_width, ground_tile_height = ground_tile.rect.size

		available_space_x = self.screen_rect.width
		number_tiles = available_space_x // ground_tile_width

		for tile in range(number_tiles):
			self._create_ground_tile(tile)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.hr_game.screen.blit(self.hr_game.bg_surface, (0,0))
		self.hr_game.clouds.draw(self.hr_game.screen)
		self.hr_game.chopper.blitme()
		for bullet in self.hr_game.bullets.sprites():
			bullet.draw_bullet()
		for wave in self.hr_game.shockwaves.sprites():
			wave.draw_wave()
		for particle in self.hr_game.particles.sprites():
			particle.draw_particle()
		for spark in self.hr_game.sparks.sprites():
			spark.draw_spark()
		for puff in self.hr_game.smoke_puffs.sprites():
			puff.draw_smoke()
		self.hr_game.asteroids.draw(self.hr_game.screen)
		self.ground.draw(self.screen)
		
		# Show asteroid hitboxes
		for asteroid in self.hr_game.asteroids:
			pygame.draw.rect(self.hr_game.screen, 'magenta', asteroid.rect, 2)

		# Draw prompt information.
		if self.hr_game.stats.spacebar_pressed == False:
			self.hr_game.press_spacebar.show_prompt()

		# Draw the score information.
		self.hr_game.sb.show_score()
		
		# Draw the play button if the game is inactive.
		if not self.hr_game.stats.game_active:
			self.hr_game.play_button.draw_button()

		# Make the most recently drawn screen visible.
		pygame.display.flip()