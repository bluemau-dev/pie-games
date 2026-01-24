import sys
import pygame

from settings import Settings
from player import Player


class Rocket:

    def __init__(self):

        # Initialize Settings
        self.settings = Settings()

        # Initialize Pygame
        pygame.init()

        # Settings Screen Size
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width, self.settings.screen_height))
        
        # Caption
        pygame.display.set_caption(self.settings.caption)
        
        
        # Initialize Player
        self.player = Player(self)

    def run_game(self):
        while(True):
            self._check_events()
            
            self._update_screen()
            self.player.update()

    def _check_events(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.is_moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.player.is_moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.is_moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.player.is_moving_left = False
                

    def _update_screen(self):
         self.screen.fill(self.settings.bg_color)
         self.player.blitme()
         pygame.display.flip()


if __name__ == "__main__":
        r = Rocket()
        r.run_game()

