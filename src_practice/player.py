import pygame

class Player:
    def __init__(self, r):
        # References Game Screen
        self.screen = r.screen
        self.screen_rect = r.screen.get_rect()

        # References Settings
        self.settings = r.settings

        # Create the Player Image
        self.image = pygame.image.load('assets/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (64,64))
        self.image_rect = self.image.get_rect()

        # Start our Image at bottom of the Screen
        self.image_rect.center = self.screen_rect.center
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.image_rect.x)
        # Movement Flag
        self.is_moving_right = False
        self.is_moving_left = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.is_moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.is_moving_left and self.image_rect.left > 0:
            self.x -= self.settings.speed
            
        self.image_rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)

