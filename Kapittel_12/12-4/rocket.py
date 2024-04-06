import pygame

class Rocket:
    """a class to manage the rocket"""

    def __init__(self, r_game):
        """Initialize the ship and set its starting position."""
        self.screen = r_game.screen
        self.rocket_settings = r_game.rocket_settings
        self.screen_rect = r_game.screen.get_rect()

        # Load the rocket image and gat its rect.
        self.image = pygame.image.load('images/Ali2.bmp')
        self.rect = self.image.get_rect()

        # Start each  new rocket in the center of the screen
        self.rect.center = self.screen_rect.center

        # store a decimal value for the ship's  position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the ship's position based on the movement of the flag."""
        # Updates the ship's values, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_settings.rocket_x_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_settings.rocket_x_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_settings.rocket_y_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_settings.rocket_y_speed

        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket and its current location."""
        self.screen.blit(self.image, self.rect)
