import pygame


class Player(pygame.sprite.Sprite):
    """player actions"""
    def __init__(self, screen):
        """player init"""
        super(Player, self).__init__()
        self.screen = screen
        self.tower_image = pygame.image.load('assets/images/player.png')
        self.rect = self.tower_image.get_rect()
        self.screen_rect = screen.get_rect()

    def update_player(self):
        """update player"""
        pass

    def create_player(self):
        """create player on center"""
        self.screen.blit(self.tower_image, (0, 0))

    def draw_player(self):
        """"draw player"""
        pass