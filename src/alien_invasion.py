import sys
import pygame

from settings import Setting
from ship import Ship
from spaceman import Spaceman

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
        self.spaceman = Spaceman(self)

        

    def run_game(self):
        while True:
            """Check events and Updates Game"""
            self._check_events()
            self._update_screen()
            self.ship.update()
            
    
    def _check_events(self):
        """Respond to in game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.is_moving = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.is_moving = False
    
    def _update_screen(self):
        """Updates the Screen color and objects"""
        # Fill Screen with Color
        self.screen.fill(self.setting.bg_color)
        
        # Draws images to Screen
        self.ship.blitme()
        self.spaceman.blitme()
        
        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
