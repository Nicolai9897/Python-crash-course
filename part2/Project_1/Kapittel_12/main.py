import sys
import pygame

from character import character


class Funsie:
    """A game to do pcc2 chapter 12 courses"""

    def __init__(self):
        """Initialize the game and create game assets"""
        pygame.init()


        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("FUNSIE!")

        self.character = character(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # color to fill the background with
            self.bg_color = (255, 255, 255)
            self.screen.fill(self.bg_color)
            self.character.blitme()


            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance
    fun = Funsie()
    fun.run_game()

