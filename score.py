import pygame.font
from player import Player
from pygame.sprite import Group


class Scores:
    """game info output"""
    def __init__(self, screen, stats):
        """score init"""
        self.screen = screen
        self.stats = stats
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.screen_rect = screen.get_rect()
        self.text_color = (180, 0, 0)
        self.font = pygame.font.Font('assets/fonts/appetite.ttf', 50)
        self.image_score()
        # self.image_lifes()

    def image_score(self):
        """concert score text to gui"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, None)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right * 0.8
        self.score_rect.bottom = self.height * 0.95

    def image_lifes(self):
        """show lives"""
        pass

    def show_score(self):
        """score output"""
        self.screen.blit(self.score_img, self.score_rect)
        pygame.display.update()
        # self.lifes.draw(self.screen)
