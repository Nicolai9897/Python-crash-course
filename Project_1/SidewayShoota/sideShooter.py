import sys
from time import sleep

import pygame

from settings import Settings
from GameStats import GameStats
from ship import Ship
from bullet import Bullet
from ali import Ali


class SideShooter:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Side Shoota!")

        # create an instance to store game statistcs
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alis = pygame.sprite.Group()

        self._create_alis()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alis()
                self._update_screen()

    def _check_events(self):
        """respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            bullet_end = self.screen.get_rect().width
            if bullet.rect.left >= bullet_end:
                self.bullets.remove(bullet)
        self._check_bullet_ali_colllision()

    def _check_bullet_ali_colllision(self):
        """Respond to bullet-ali collisions"""

        # Check for any bullets that have hit alis.
        #   If so, get rid of the bullet and the ali.
        pygame.sprite.groupcollide(
            self.bullets, self.alis, True, True)

        if not self.alis:
            # Destroy existing bullets and create new alis
            self.bullets.empty()
            self._create_alis()

    def _update_alis(self):
        """
        check if alis is on the bottom or top of screen,
        then update the position of all the alis in the alis
        """
        self._check_alis_edges()
        self.alis.update()

        # Look for ali-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.alis):
            self._ship_hit()

        # look for alis hitting the left of the screen.
        self._check_alis_left()

    def _create_alis(self):
        """create alis of ali"""
        # Create an ali and find the number of alis in a row
        # spacing between each ali is equal to one ali width
        ali = Ali(self)
        ali_width, ali_height = ali.rect.size
        available_space_y = self.settings.screen_height - ali_height
        number_ali_y = available_space_y // (2 * ali_height)
        # Determine the number of rows of aliens that fit on the screen.
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width -
                             (5 * ali_width) - ship_width)
        number_of_coloums = available_space_x // (2 * ali_width)
        # Create full fleet of alis
        for number_coloum in range(number_of_coloums):
            for ali_number in range(number_ali_y):
                self._create_ali(ali_number, number_coloum)

    def _create_ali(self, ali_number, number_coloum):
        """Create an ali and place it in the coloumn"""
        ali = Ali(self)
        ali_width, ali_height = ali.rect.size
        ali.y = ali_height + 2 * ali_height * ali_number
        ali.rect.x = self.settings.screen_width - (ali_width + 2 * ali.rect.width * number_coloum)
        ali.x = ali.rect.x
        self.alis.add(ali)

    def _check_alis_edges(self):
        """Respond appropriately if any alis have reached an edge"""
        for ali in self.alis.sprites():
            if ali.check_edges():
                self._change_fleet_direction()
                break

    def _check_alis_left(self):
        """check if any alis have reached the left of the scrren"""
        screen_rect = self.screen.get_rect()
        for ali in self.alis.sprites():
            if ali.rect.left <= screen_rect.left:
                """Treat this the same as if the ship got hit."""
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """move the entire alis and change horixontal direction"""

        self.settings.alis_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        print(self.stats.ships_left)
        if self.stats.ships_left > 1:
            # Decrement ships left.
            self.stats.ships_left -= 1

            # Get rid of any remaining alis and bullets
            self.alis.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_alis()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alis.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game
    ss = SideShooter()
    ss.run_game()
