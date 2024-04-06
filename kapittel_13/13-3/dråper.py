import pygame
from pygame.sprite import Sprite

pic = pygame.image.load("bilder/regndraape.bmp")
pic = pygame.transform.scale(pic, (80, 68))


class Drops(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.drop_speed = 0.7

        # Laster bildet og dens rektangler attributer
        self.image = pic

        self.rect = self.image.get_rect()

        # starter ny dråpe i topp venstre hjørnet
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Lagrer dråpens nøyaktige  horisontale posisjon
        self.y = float(self.rect.y)

    def check_edges(self):
        """Funskjon for å se om dråpen har nådd bunnen av skjermen"""
        screen_rect = self.screen.get_rect()
        if self.rect.y > screen_rect.bottom:
            print("YES")
            return True


    def update(self):
        """flytter dråpen tilbake til toppen av siden"""
        screen_rect = self.screen.get_rect()
        if self.check_edges():
            self.y -= (screen_rect.bottom + self.rect.height)
        else:
            self.y += self.drop_speed
        self.rect.y = self.y




