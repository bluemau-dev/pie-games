import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        """Initialize Bullet settings"""
        # Bullet is a Subclass/Child of Sprite
        super().__init__()

        # Reference Screen + Settings
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.color = self.settings.bullet_color

        # Create Rect of Bullet and Position it
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        # Position Bullets Rect with Ships Rect
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the Bullet's Position as a Decimal Value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the Rect Position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the Bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)


    # Rect:
    # Our self.y is a direct reference to our rect.y but as a float (decimal number) to make it easier to
    # calculate speed and distance traveled.