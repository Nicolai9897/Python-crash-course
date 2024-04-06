import pygame
from pygame.sprite import Sprite



class Ali(Sprite):
    """A class representing Alis for the player to shoot down"""

    def __init__(self, ss_game):
        """Initialize the ali and set his starting position"""
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen

        # Load the Ali picture and set his starting position
        self.image = pygame.image.load('images/ali.bmp')
        self.image = pygame.transform.scale(self.image, (46, 60))
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()

        # start each new Ali near the top right of the scree
        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height

        # Store ali's position exact  position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def print_position(self):
        print("TEST")
        print(self.x, self.y)

    def check_edges(self):
        """Return True if ali is at the bottom or top  of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:

            return True

    def update(self):
        """Change ali horizontal direction"""
        self.y += (self.settings.ali_speed * self.settings.alis_direction)
        #self.x += self.settings.alis_horizontal_speed
        self.rect.y = self.y
        #self.rect.x = self.x
        #print(self.x, self.y)
        self._move_side()


    def _move_side(self):
        """Move the ali to the right or left."""
        self.rect.x = self.x

        self.x -= (self.settings.alis_left_speed)
        self.rect.x = self.x
