import pygame.font

class Button:
	"""A class to create a start button before the game begins."""

	def __init__(self, hr_game, msg):
		"""Initializes button attributes."""
		self.screen = hr_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 400, 100
		self.button_color = (111, 115, 120)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Impact', 48, False)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Prep the button message.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw a blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class Prompt:
	"""A class to create flashing text prompts on screen."""
	def __init__(self, hr_game, msg):
		"""Initializes prompt attributes."""
		self.screen = hr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = hr_game.stats
		self.settings = hr_game.settings
		self.chopper = hr_game.chopper

		# Font settings for prompt information.
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Impact', 36, False)

		# Prepare the prompt message.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn the msg into a rendered image and place beneath chopper
		rect."""
		self.prompt_image = self.font.render(msg, True, self.text_color)
		self.prompt_image.set_alpha(150)
		self.prompt_image_rect = self.prompt_image.get_rect()
		self.prompt_image_rect.midtop = self.chopper.rect.midbottom

	def show_prompt(self):
		"""Draw prompt to the screen."""
		self.screen.blit(self.prompt_image, self.prompt_image_rect)

	def update(self):
		# Keep text immediately below chopper
		self.prompt_image_rect.midtop = self.chopper.rect.midbottom