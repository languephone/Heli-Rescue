import pygame

class FramesPerSecond:
     """A class to manage the fps display."""
     def __init__(self, hr_object):
          """Initialize fps attributes."""
          self.font = pygame.font.SysFont('helveticaneue', 18)
          self.width, self.height = self.font.size('FPS: 100')
          self.text_color = (0, 255, 0) # Bright green
          self.h_pos = 5
          self.v_pos = hr_object.settings.screen_height - 25
          self.screen = hr_object.screen
          self.clock = hr_object.clock

     def display_fps(self):

          fps = 'FPS:' + str(int(self.clock.get_fps()))
          fps_text = self.font.render(fps, True, self.text_color)
          self.screen.blit(fps_text, (self.h_pos, self.v_pos))