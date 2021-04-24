import pygame

class Menu():
	"""A class to manage the menus of the game."""

	def __init__(self, hr_game):
		self.hr_game = hr_game
		self.mid_w = self.hr_game.settings.screen_width //  2
		self.mid_h = self.hr_game.settings.screen_height // 3
		self.run_display = True
		self.cursor_rect = pygame.Rect(0, 0, 20, 20)
		self.cursor_offset = -120
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(hr_game.settings.font_family, 
			hr_game.settings.font_size, False)


	def draw_text(self, msg, x, y):
		"""Turn msg into a rendered image and center text on the button."""
		msg_image = self.font.render(msg, True, self.text_color, self.hr_game.settings.bg_color)
		msg_image_rect = msg_image.get_rect()
		msg_image_rect.center = (x, y)
		self.hr_game.screen.blit(msg_image, msg_image_rect)

	def draw_cursor(self):
		"""Draw cursor to be used next to menu options."""
		self.draw_text("*", self.cursor_rect.x, self.cursor_rect.y)


class MainMenu(Menu):

	def __init__(self, hr_game):
		super().__init__(hr_game)
		self.state = "Start"
		self.startx, self.starty = self.mid_w, self.mid_h + 180
		self.optionsx, self.optionsy = self.mid_w, self.mid_h + 250
		self.creditsx, self.creditsy = self.mid_w, self.mid_h + 320
		self.cursor_rect.midtop  = (self.startx + self.cursor_offset, self.starty)


	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.hr_game._check_events()
			self.check_input()
			self.hr_game.screen.fill(self.hr_game.settings.bg_color)
			self.draw_text("Heli Rescue", self.mid_w, self.mid_h)
			self.draw_text("Start Game", self.startx, self.starty)
			self.draw_text("Options", self.optionsx, self.optionsy)
			self.draw_text("Credits", self.creditsx, self.creditsy)
			self.draw_cursor()
			pygame.display.flip()

	def move_cursor(self):
		if self.hr_game.chopper.moving_down:
			if self.state == "Start":
				self.cursor_rect.midtop = (self.optionsx + self.cursor_offset, self.optionsy)
				self.state = "Options"
			elif self.state == "Options":
				self.cursor_rect.midtop = (self.creditsx + self.cursor_offset, self.creditsy)
				self.state = "Credits"
			else:
				self.cursor_rect.midtop = (self.startx + self.cursor_offset, self.starty)
				self.state = "Start"
			self.hr_game.chopper.moving_down = False
		elif self.hr_game.chopper.moving_up:
			if self.state == "Start":
				self.cursor_rect.midtop = (self.creditsx + self.cursor_offset, self.creditsy)
				self.state = "Credits"
			elif self.state == "Options":
				self.cursor_rect.midtop = (self.startx + self.cursor_offset, self.starty)
				self.state = "Start"
			else:
				self.cursor_rect.midtop = (self.optionsx + self.cursor_offset, self.optionsy)
				self.state = "Options"
			self.hr_game.chopper.moving_up = False

	def check_input(self):
		self.move_cursor()
		if self.hr_game.return_pressed:
			if self.state == "Start":
				self.hr_game._start_game()
				self.run_display = False
			elif self.state == "Options":
				pass
			elif self.state == "Credits":
				pass
			