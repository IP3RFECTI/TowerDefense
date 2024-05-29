import pygame


class Menu:
    """menu actions"""
    def __init__(self, screen):
        """init main menu params"""
        self._ARIAL_50 = pygame.font.SysFont('arial', 50)
        self._option_surfaces = []
        self._callback = []
        self._current_option_index = 0
        # self.screen = screen

    def append_option(self, option, callback):
        """add new option"""
        self._option_surfaces.append(self._ARIAL_50.render(option, True, (255, 255, 255)))
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
            option_rect.center = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surface, (0, 100, 0), option_rect)
            surface.blit(option, option_rect)

    def start_clicked(self):
        """start click check"""
        if len(self._option_surfaces) == 0:
            return True
        else:
            return False