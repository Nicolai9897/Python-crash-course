import pygame
pic = pygame.image.load('12-4/images/Ali2.bmp')
pic = pygame.transform.scale(pic, (150, 75))

class character:
    """A class for the main game character"""

    def __init__(self, fun_game):
        """Initialize the game character, and its starting position"""
        self.screen = fun_game.screen
        self.screen_rect = fun_game.screen.get_rect()

        #load the character image, and its rectangle
        self.image = pic
        self.rect = self.image.get_rect()

        #start each new character in the middle of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """"Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)


