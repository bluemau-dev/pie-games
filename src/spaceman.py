import pygame

class Spaceman:
    def __init__(self, ai_game):
        """Define our Spaceman in Game"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('assets/spaceship.bmp')
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the Spaceman"""
        self.screen.blit(self.image, self.rect)