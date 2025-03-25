import sys

import pygame

from rocket_settings import Settings
from rocket import Rocket

class Rockets:
    """overall class to manage the rocket assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.rocket_settings = Settings()


        self.screen = pygame.display.set_mode((
            self.rocket_settings.screen_width, self.rocket_settings.screen_height
        ))

        self.rocket = Rocket(self)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypres"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """update the screen during each pass thought the loop."""
        self.screen.fill(self.rocket_settings.bg_color)
        self.rocket.blitme()


if __name__ == '__main__':
    # Make a game instance, and run the game
    r = Rockets()
    r.run_game()

