import pygame

from settings import Setting
from ship import Ship
import game_functions as gf

class AlienInvasion():
    def run_game(self):
        pygame.init()
        setting = Setting()
        screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
        pygame.display.set_caption('Alien invasion')
        ship = Ship(screen)

        while True:
            gf.check_events(ship)
            ship.update()
            gf.update_screen(setting, screen, ship)





obj = AlienInvasion()
obj.run_game()
