import pygame.freetype
from pygame.sprite import Group
from chopper import Chopper

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, hr_game):
		"""Initialize scorekeeping attributes."""
		self.hr_game = hr_game
		self.screen = hr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = hr_game.settings
		self.stats = hr_game.stats

		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.freetype.SysFont('Impact', 32)

		# Prepare the initial score image.
		self.prep_score()
		self.prep_choppers()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str,
			self.text_color)

		# Display the score at the top right of the screen.
		self.score_image[1][0] = (self.screen_rect.right - 
			self.score_image[1][2] - 20)

	def show_score(self):
		"""Draw score and reserve choppers to the screen."""
		self.screen.blit(self.score_image[0], self.score_image[1])
		self.choppers.draw(self.screen)

	def prep_choppers(self):
		"""Show how many choppers are left."""
		self.choppers = Group()
		for chopper_number in range(self.stats.choppers_left):
			chopper = Chopper(self.hr_game)
			chopper.rect.x = 10 + chopper_number * (chopper.rect.width / 3)
			chopper.rect.y = 10
			self.choppers.add(chopper)
