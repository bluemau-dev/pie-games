import sys
import pygame

from settings import Setting
from ship import Ship
from spaceman import Spaceman
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """Initialization of Game Screen"""
        # Reference Settings Class
        self.setting = Setting()

        # Initiliaze Background
        pygame.init()

        # Set Window Dimension
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        
        # Set Window Caption
        pygame.display.set_caption(self.setting.caption)

        # Reference Game Modules
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        #self.spaceman = Spaceman(self)

        

    def run_game(self):
        while True:
            """Check events and Updates Game"""
            self._check_events()
            
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
    
    def _check_events(self):
        """Respond to in game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self,event):
        """Respond to Keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """Respond to Key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = False
        
    
    def _update_screen(self):
        """Updates the Screen color and objects"""
        # Fill Screen with Color
        self.screen.fill(self.setting.bg_color)
        
        # Draws images to Screen
        self.ship.blitme()
        #self.spaceman.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        # Make most recently drawn screen visible
        pygame.display.flip()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet groups"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
