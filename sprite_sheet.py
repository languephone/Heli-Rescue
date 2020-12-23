# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

# Additional notes
# - Further adaptations from https://www.pygame.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

import pygame


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def load_grid_images(self, num_rows, num_cols, x_margin, x_padding, 
        y_margin, y_padding):
        """Load a grid of images and return them as a list."""
        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        x_sprite_size = (sheet_width - (2 * x_margin) 
            - ((num_cols - 1) * x_padding)) / num_cols

        y_sprite_size = (sheet_height - (2 * y_margin) 
            - ((num_rows - 1) * y_padding)) / num_rows

        grid_images = []
        for i in range(num_rows):
            for j in range(num_cols):
                rect = (x_margin + (j * (x_padding + x_sprite_size)),
                        y_margin + (i * (y_padding + y_sprite_size)), 
                        x_sprite_size, 
                        y_sprite_size)
                print(rect)
                image = self.image_at(rect)
                grid_images.append(image)

        return grid_images