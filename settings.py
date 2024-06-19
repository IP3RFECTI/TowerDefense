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
        self.img_Off = pygame.image.load('assets/images/Off.png')
        self.img_On = pygame.image.load('assets/images/On.png')
        self.current_img = pygame.image.load('assets/images/On.png')
        self.music_is_paused = False
        self.clicked = False

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

    def switch_music(self):
        if self.music_is_paused:
            self.music_is_paused = False
            pygame.mixer.music.unpause()
            self.current_img = self.img_On
        else:
            self.music_is_paused = True
            pygame.mixer.music.pause()
            self.current_img = self.img_Off

    def image_music(self):
        self.screen.blit(self.current_img, (500, 90))
        pygame.display.flip()

    def settings_clicked(self):
        """start click check"""
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True