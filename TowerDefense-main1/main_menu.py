import pygame
pygame.init()
myfont = pygame.font.Font('assets/fonts/Montserrat-ExtraBold.ttf', 50)
text = myfont.render('Башня Мага', True, '#000B24')
from leadearboard import *

#pygame.draw.rect(surface, ('#D9D9D9'), (275, 64, 250, 60), border_radius=12)
#pygame.draw.rect(surface, ('#D9D9D9'), (275, 139, 250, 60), border_radius=12)
#pygame.draw.rect(surface, ('#D9D9D9'), (275, 214, 250, 60), border_radius=12)
#pygame.draw.rect(surface, ('#D9D9D9'), (275, 289, 250, 60), border_radius=12)
#surface.blit(text, (230, 0))

class Menu:
    """menu actions"""
    def __init__(self, screen):
        """init main menu params"""
        self._ARIAL_50 = pygame.font.Font('assets/fonts/Montserrat-ExtraBold.ttf', 35)
        self._option_surfaces = []
        self._callback = []
        self._current_option_index = 0
        # self.screen = screen

    def append_option(self, option, callback):
        """add new option"""
        self._option_surfaces.append(self._ARIAL_50.render(option, True, ('#002069')))
        self._callback.append(callback)

    def delete_options(self):
        """delete options"""
        self._option_surfaces.clear()
        self._callback.clear()

    def switch(self, direction):
        """next option"""
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        """select option"""
        try:
            self._callback[self._current_option_index]()
        except IndexError:
            pass

    def draw(self, surface, x, y, option_y_padding):
        """draw text"""

        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.center = (x, y + i * option_y_padding+23)
            if i == self._current_option_index:
                pygame.draw.rect(surface, ('#FFFFFF'), option_rect)
            surface.blit(option, option_rect)

    def start_clicked(self):
        """start click check"""
        if len(self._option_surfaces) == 0:
            return True
        else:
            return False