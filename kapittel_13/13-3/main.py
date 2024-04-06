import sys

import pygame
from random import randint
from dråper import Drops


class RainDrops:
    """hoved klasse for regndråper"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("REGNDRÅPER")
        self.bg_color = (255, 255, 255)

        self.drops = pygame.sprite.Group()

        self._create_drops()

    def run_game(self):
        """Start the main loop for dråpene"""
        while True:
            self._check_events()
            self._update_drops()
            self._update_screen()

    def _create_drops(self):
        """Create the fleet of drops"""
        drop = Drops(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)


        for drop_number in range(number_drops_x):
            y_pos = randint(-1500, 0)
            print(y_pos)
            self._create_drop(drop_number, y_pos)

    def _create_drop(self, drop_number, y_pos):
        drop = Drops(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.rect.x = drop.x
        drop.rect.y = drop.y
        drop.rect.y = (self.screen.get_rect().bottom + y_pos)
        drop.y = y_pos
        self.drops.add(drop)


    def _check_events(self):
        """lar oss gå ut av appen"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()

    def _update_drops(self):
        """oppdaterer dråpene"""
        self._check_bottom()
        self.drops.update()

    def _check_bottom(self):
        """hjelper metode for å sjekke kantene"""
        for drop in self.drops.sprites():
            drop.check_edges()


    def _update_screen(self):
        """update the screen during each pass through the loop"""
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    drops = RainDrops()
    drops.run_game()
