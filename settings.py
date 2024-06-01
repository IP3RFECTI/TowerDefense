import csv
import pygame


class Settings:

    """settings"""
    def __init__(self, screen):
        """settings init"""
        self.path = 'assets/settings.txt'
        self.file_data = []
        self.titles = ["Эффекты", "Музыка"]
        self.check_file()
        self.ARIAL_50 = pygame.font.SysFont('arial', 50)
        self.screen = screen
        self.clicked = True

    def check_file(self):
        pass

    def draw_settings(self):
        counter = 0
        for name, val in self.file_data:
            if counter == 0:
                draw = self.ARIAL_50.render(name + "                  " +
                                            val, True, (255, 255, 255))
                self.screen.blit(draw, (200, 400 + (counter*50)))
            else:
                draw = self.ARIAL_50.render(name + ": ", True, (255, 255, 255))
                self.screen.blit(draw, (200, 400 + (counter*50)))
                draw = self.ARIAL_50.render(val, True, (255, 255, 255))
                self.screen.blit(draw, (510, 400 + (counter*50)))
            counter += 1


    def settings_clicked(self):
        """start click check"""
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True