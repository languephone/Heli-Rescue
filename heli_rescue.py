import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button, Prompt
from chopper import Chopper
from bullet import Bullet
from asteroids import Asteroid
from background_elements import Cloud
from particle_effects import Shockwave, ParticleBreak, Smoke

class HeliRescue:
	"""Overall class to run the Heli Rescue game."""

	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.mixer.pre_init(frequency = 22050, size = 8, channels = 1, buffer = 256)
		pygame.init()
		self.clock = pygame.time.Clock()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.bg_surface = pygame.transform.scale(
			pygame.image.load(self.settings.bg_image),
			 (self.settings.small_screen_size)).convert()
		pygame.display.set_caption("Heli Rescue")	
		
		# Create smaller screen at half size to scale all pixels
		self.small_screen = pygame.Surface(self.settings.small_screen_size)

		# Create game objects
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.chopper = Chopper(self)
		self.bullets = pygame.sprite.Group()
		self.asteroids = pygame.sprite.Group()
		self.clouds = pygame.sprite.Group()
		self.shockwaves = pygame.sprite.Group()
		self.particles = pygame.sprite.Group()
		self.smoke_puffs = pygame.sprite.Group()

		# Tutorial Prompts.
		self.press_spacebar = Prompt(self, "Hold spacebar to fire bullets")

		# Make the 'play' button.
		self.play_button = Button(self, "Play Heli Rescue")


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			
			if self.stats.game_active:
				self.chopper.update()
				self._fire_bullet()
				self._update_bullets()
				self._hurl_asteroids()
				self._update_asteroids()
				self._update_shockwaves()
				self._update_particles()
				self._generate_smoke(self.chopper)
				self._update_smoke()
				self._create_clouds()
				self._update_clouds()
				self._check_tutorial_prompts()
			
			self._update_screen()
			self.clock.tick(120)

	def intro_game(self):
		"""A temporary loop to create an intro scene."""
		while self.chopper.centery > self.settings.small_screen_height / 2:
			self._check_events()
			
			if self.stats.game_active:
				self.chopper.center_chopper()
				self._check_tutorial_prompts()
			self._update_screen()
			self.clock.tick(120)

	def pause_menu(self):
		"""A loop to stop chopper, asteroids and bullets from updating."""
		self.chopper.motor_sound.set_volume(0.2)
		
	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		
		# convert mouse_pos to scale of screen
		#mouse_pos_scaled = (mouse_pos[0] / 2, mouse_pos[1] / 2)
		
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_RIGHT:
			self.chopper.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.chopper.moving_left = True
		elif event.key == pygame.K_UP:
			self.chopper.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.chopper.moving_down = True
		elif event.key == pygame.K_SPACE:
			self.chopper.firing_bullets = True
			self.stats.spacebar_pressed = True
		elif event.key == pygame.K_ESCAPE:
			self.stats.game_active = False
			self.chopper.motor_sound.fadeout(1000)
			pygame.mouse.set_visible(True)
		elif event.key == pygame.K_q:
			pygame.quit()
			sys.exit()


	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.chopper.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.chopper.moving_left = False
		elif event.key == pygame.K_UP:
			self.chopper.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.chopper.moving_down = False
		elif event.key == pygame.K_SPACE:
			self.chopper.firing_bullets = False

	def _check_tutorial_prompts(self):
		if self.stats.spacebar_pressed == False:
			self.press_spacebar.update()

	def _start_game(self):
		# Clear screen of asteroids and bullets.
		#self.asteroids.empty()
		#self.bullets.empty()

		# Create a chopper instance and make the mouse invisible.
		#self.chopper = Chopper(self)
		pygame.mouse.set_visible(False)

		# Set game to active to start main loop.
		self.stats.game_active = True

		# Play chopper sound
		self.chopper.motor_sound.play(-1).set_volume(0.1)

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if (self.chopper.firing_bullets == True and 
				self.chopper.bullet_firing_state > 
				self.settings.bullet_firing_threshold):
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			self.chopper.bullet_firing_state = 0
			
			# Play sound effect
			self.chopper.gun_sound.play().set_volume(0.1)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		self.bullets.update()
		
		# Get rid of bullets that are off the edge of the screen.
		for bullet in self.bullets.copy():
			if bullet.rect.left > self.settings.small_screen_width:
				self.bullets.remove(bullet)

		self._check_bullet_asteroid_collisions()

	def _update_shockwaves(self):
		"""Update size and border of shockwaves and get rid of old waves."""
		self.shockwaves.update()

		# Get rid of waves that have a border approaching zero.
		for wave in self.shockwaves.copy():
			if wave.border_width <= 1.5:
				self.shockwaves.remove(wave)

	def _update_particles(self):
		"""Update size/position of particles and get rid of old particles."""
		self.particles.update()

		# Get rid of particles that have a radius approaching zero.
		for particle in self.particles.copy():
			if particle.radius <=0:
				self.particles.remove(particle)

	def _update_smoke(self):
		"""Update size/position of puffs and get rid of old puffs."""
		self.smoke_puffs.update()

		# Get rid of particles that have moved offscreen."""
		for puff in self.smoke_puffs.copy():
			if puff.pos_x < -puff.radius:
				self.smoke_puffs.remove(puff)

	def _check_bullet_asteroid_collisions(self):
		"""Respond to bullet-asteroid collisions."""
		# Remove bullets that have collided with asteroids.
		collisions = pygame.sprite.groupcollide(
			self.asteroids, self.bullets, False, True)
		# Reduce asteroid health for each bullet hit
		for asteroid in collisions.keys():
			asteroid.health -= 1

	def _chopper_hit(self):
		"""Respond to the chopper hitting an asteroid."""

		# Play sound effect and change image to explosion
		self.chopper.crash_sound.play()	
		self.chopper.emitting_smoke = True	

		# Get rid of any remaining asteroids and bullets.
		self.asteroids.empty()
		self.bullets.empty()

		# Re-center the chopper.
		self.chopper.center_chopper()

		# Pause.
		sleep(1)

		# Remove 1 chopper from the reserve
		self.stats.choppers_left -= 1
		self.sb.prep_choppers()
 
	def _create_asteroid(self):
		"""Create an asteroid and add it to the list of asteroids."""
		asteroid = Asteroid(self)
		self.asteroids.add(asteroid)

	def _hurl_asteroids(self):
		"""Add an asteroid if there are fewer than 4 on screen"""
		if len(self.asteroids) < self.settings.asteroid_max_count:
			self._create_asteroid()

	def _update_asteroids(self):
		"""Move asteroids to the left"""
		self.asteroids.update()

		# Get rid of asteroids that have moved beyond the screen.
		for asteroid in self.asteroids.copy():
			if asteroid.rect.right <= 0:
				self.asteroids.remove(asteroid)

		# Get rid of asteroids with 0 health:
		for asteroid in self.asteroids.copy():
			if asteroid.health <= 0:
				asteroid.explosion_sound.play()
				#self._generate_shockwave(asteroid)
				self._generate_particle_break(asteroid)
				self.stats.score += self.settings.asteroid_points
				self.sb.prep_score()
				self.asteroids.remove(asteroid)

		# Look for asteroid-chopper collisions.
		if pygame.sprite.spritecollideany(self.chopper, self.asteroids, 
										self._collide_hit_rect):
			self._chopper_hit()
	
	def _generate_shockwave(self, asteroid):
		"""Create a shockwave on destruction of item."""
		new_wave = Shockwave(self, asteroid.rect.centerx, 
						asteroid.rect.centery, self.settings.shockwave_colour)
		self.shockwaves.add(new_wave)

	def _generate_particle_break(self, asteroid):
		"""Create group of particles on destruction of item."""
		for i in range(self.settings.particle_count):
			new_particle = ParticleBreak(self, asteroid.rect.centerx, 
					asteroid.rect.centery, self.settings.particle_colour)
			self.particles.add(new_particle)

	def _generate_smoke(self, chopper):
		"""Create smoke particles on hitting asteroid."""
		if (self.chopper.emitting_smoke == True and 
				self.chopper.smoke_emitting_state > 
				self.settings.smoke_emitting_threshold):
			new_puff = Smoke(self, chopper.rect.centerx, chopper.rect.centery,
							 colour='grey')
			self.smoke_puffs.add(new_puff)
			self.chopper.smoke_emitting_state = 0

	def _collide_hit_rect(self, one, two):
		return one.hitbox.colliderect(two.rect)

	def _create_cloud(self):
		"""Create a cloud and add it to the list of clouds."""
		cloud = Cloud(self)
		self.clouds.add(cloud)

	def _create_clouds(self):
		"""Add a cloud if there are fewer than 3 on screen"""
		if len(self.clouds) < self.settings.cloud_max_count:
			self._create_cloud()

	def _update_clouds(self):
		"""Move clouds to the left"""
		self.clouds.update()

		# Get rid of clouds that have moved beyond the screen.
		for cloud in self.clouds.copy():
			if cloud.rect.right <= 0:
				self.clouds.remove(cloud)
	
	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.small_screen.blit(self.bg_surface, (0,0))
		self.clouds.draw(self.small_screen)
		self.chopper.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for wave in self.shockwaves.sprites():
			wave.draw_wave()
		for particle in self.particles.sprites():
			particle.draw_particle()
		for puff in self.smoke_puffs.sprites():
			puff.draw_smoke()
		self.asteroids.draw(self.small_screen)
		
		# Draw prompt information.
		if self.stats.spacebar_pressed == False:
			self.press_spacebar.show_prompt()

		# Draw small screen onto the big screen
		self.screen.blit(pygame.transform.scale(self.small_screen,
			 (self.settings.screen_width, self.settings.screen_height)), (0,0))
		
		# Draw the score information.
		self.sb.show_scoreboard()

		# Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()

		# Make the most recently drawn screen visible.
		pygame.display.flip()
			
if __name__ == '__main__':
	# Make a game instance, and run the game.
	hr = HeliRescue()
	hr.intro_game()
	hr.run_game()