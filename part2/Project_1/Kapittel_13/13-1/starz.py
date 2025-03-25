import sys

import pygame
from pygame.sprite import Sprite
from random import randint

class SZ(Sprite):

    random_number = 0

    def __init__(self, stars):
        super().__init__()
        self.screen = stars.screen

        self.image = pygame.image.load('13-1/bilder/stjerne.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.x = float(self.rect.x)




class Stars():
    """Class to represent random placement of stars"""

    def __init__(self):
        """Initialize the stars"""
        self.random_number = None
        pygame.init()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("STARZ")

        self.stars = pygame.sprite.Group()

        self._place_stars()




    def run_simulation(self):
        """Starts running the simulation loop."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """checks if user presses 'q' to quit the game"""
        if event.key == pygame.K_q:
            sys.exit()

    def _place_stars(self):
        """method for placing the stars"""
        star = SZ(self)

        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        x_spacing = available_space_x // (2 * star_width)

        available_space_y = (self.screen_height - ( 3 * star_height))
        y_spacing = available_space_y // (2 * star_height)

        for row_number in range(x_spacing):
            randx = randint(-50, 50)
            for coulm_number in range(y_spacing):
                randy = randint(-50, 50)
                self._create_star(row_number, coulm_number, randx, randy)


    def _create_star(self, coulm_number, row_number, randx, randy):
        """Helper method to create a star"""
        star = SZ(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star.rect.width * coulm_number + randx
        star.rect.x = star.x
        star.y = star_height + 2 * star.rect.height * row_number + randy
        star.rect.y = star.y
        self.stars.add(star)

    def _update_screen(self):
        """update the screen during each pass through the loop."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    st = Stars()
    st.run_simulation()