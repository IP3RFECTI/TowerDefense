import pygame.font
from player import Player
from pygame.sprite import Group


class Scores():
    """game info output"""
    def __init__(self, screen, stats):
        """score init"""
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 0, 0)
        self.font = pygame.font.Font('assets/fonts/appetite.ttf', 50)
        self.image_score()
        self.image_lifes()

    def image_score(self):
        """concert score text to gui"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_lifes(self):
        """show lives"""
        self.lifes = Group()
        for life_number in range(self.stats.lifes_left):
            player = Player(self.screen)
            player.rect.x = 15 + life_number * player.rect.width
            player.rect.y = 20
            self.lifes.add(player)

    def show_score(self):
        """score output"""
        self.screen.blit(self.score_img, self.score_rect)
        self.lifes.draw(self.screen)
