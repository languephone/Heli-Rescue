import sys
from time import sleep
import pygame
from settings import Settings
from background_elements import Cloud
from debug import FramesPerSecond

class HeliRescue:
	"""Overall class to run the Heli Rescue game."""

	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()
		self.clock = pygame.time.Clock()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		
		self.bg_surface = pygame.transform.scale(
			pygame.image.load(self.settings.bg_image),
			(self.settings.screen_width, self.settings.screen_height)).convert()
		
		pygame.display.set_caption("Heli Rescue")	
		
		# Create game objects
		self.clouds = pygame.sprite.Group()
		self.fps = FramesPerSecond(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._create_clouds()
			self._update_clouds()
			self._update_screen()
			self.clock.tick(self.settings.framerate)
		
	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			pygame.quit()
			sys.exit()
		elif event.key == pygame.K_UP:
			self.settings.framerate += 10
		elif event.key == pygame.K_DOWN:
			self.settings.framerate -= 10

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
		self.screen.blit(self.bg_surface, (0,0))
		self.clouds.draw(self.screen)
		self.fps.display_fps()
		for cloud in self.clouds:
			cloud.show_speed()

		# Make the most recently drawn screen visible.
		pygame.display.flip()
			
if __name__ == '__main__':
	# Make a game instance, and run the game.
	hr = HeliRescue()
	hr.run_game()