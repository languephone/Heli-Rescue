import pygame.freetype

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, hr_game):
		"""Initialize scorekeeping attributes."""
		self.screen = hr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = hr_game.settings
		self.stats = hr_game.stats

		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.freetype.SysFont('Impact', 32)

		# Prepare the initial score image.
		self.prep_score()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str,
			self.text_color)

		# Display the score at the top right of the screen.
		self.score_image[1][0] = (self.screen_rect.right - 
			self.score_image[1][2] - 20)

	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image[0], self.score_image[1])
