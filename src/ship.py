import pygame

class Ship:
    """A class to manage the ship/player"""
    def __init__(self, ai_game):
        
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.setting

        # Load the ship image and get its rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.is_moving_right = False
        self.is_moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.is_moving_right and self.rect.right < self.screen_rect:
            self.x += self.settings.ship_speed
        if self.is_moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)