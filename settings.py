import csv
import pygame

class Settings():

    """settings"""
    def __init__(self, screen, width, height):
        """settings init"""
        self.path = 'assets/leaderboard/settings.txt'
        self.file_data = []
        self.titles = ["Эффекты", "Музыка"]
        self.check_file()
        self.ARIAL_50 = pygame.font.SysFont('arial', 50)
        self.screen = screen
        self.clicked = True

    def check_file(self):
        try:
            with open(self.path, encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file)
                for val in file_reader:
                    self.file_data.append(val)
        except FileNotFoundError:
            with open(self.path, mode="w", encoding='utf-8') as w_file:
                file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=self.titles)
                file_writer.writeheader()
                file_writer.writerow({self.titles[0]: "Alex", self.titles[1]: str(1000)})
                file_writer.writerow({self.titles[0]: "Player", self.titles[1]: str(0)})

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