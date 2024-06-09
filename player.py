import pygame


class Player(pygame.sprite.Sprite):
    """player actions"""
    def __init__(self, screen):
        """player init"""
        super(Player, self).__init__()
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.tower_image = pygame.image.load('assets/images/player.png')
        self.rect = self.tower_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.health = 100
        self.green_color = (0, 200, 64)
        self.hp_rect = pygame.Rect((self.width/25*1, self.height/10*9, self.health, 20))


    def draw_player(self):
        """"draw player"""
        self.screen.blit(self.tower_image, (0, 0))

    def update_player_hp(self, damage):
        """update player"""
        self.health -= damage
        self.hp_rect = pygame.Rect((self.width/25*1, self.height/10*9, self.health, 20))
        print(self.health)

    def draw_player_hp(self):
        pygame.draw.rect(self.screen, self.green_color, self.hp_rect)
        self.screen.blit(self.tower_image, (0, 0))