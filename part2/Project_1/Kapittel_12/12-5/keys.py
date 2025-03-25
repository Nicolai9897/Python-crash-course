import sys

import pygame
from keySettings import Settings


class Key:
    """A class to print the keys that are being pressed by the user"""

    def __init__(self):
        """Initialize the key event logger"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("KEYLOGGER")

    def run_logger(self):
        """Start the main loop for the logger"""
        while True:
            self._check_events()
            self._update_Screen()

            pygame.display.flip()


    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.key)
            #elif event.type == pygame.KEYUP:
             #df   self._check_keyup_events(self, event)



    def _update_Screen(self):
        """update the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    k = Key()
    k.run_logger()