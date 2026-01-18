import sys
import pygame

from settings import Setting
from ship import Ship
from spaceman import Spaceman

class AlienInvasion:
    def __init__(self):
        # Reference Settings Class
        self.setting = Setting()

        # Initiliaze Background
        pygame.init()

        # Set Window Dimension
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        
        # Set Window Caption
        pygame.display.set_caption(self.setting.caption)

        self.ship = Ship(self)
        self.spaceman = Spaceman(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill Screen with Color
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            self.spaceman.blitme()
            pygame.display.flip()
            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
