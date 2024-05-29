import pygame


class Player(pygame.sprite.Sprite):
    """player actions"""
    def __init__(self, screen):
        """player init"""
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/images/player.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.cx = float(self.rect.centerx)

        self.rect.centery = self.screen_rect.centery
        self.cy = float(self.rect.centerx)

        self.rect.bottom = self.screen_rect.bottom

        self.mright, self.mleft, self.mup, self.mdown = False, False, False, False

    def update_player(self):
        """update player position"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.cx += 5
        if self.mleft and self.rect.left > 0:
            self.cx -= 5
        if self.mup and self.rect.top > 0:
            self.cy -= 5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.cy += 5
        self.rect.centerx = self.cx
        self.rect.centery = self.cy

    def create_player(self):
        """create player on center"""
        self.center = self.screen_rect.centerx
        self.cx = 375
        self.cy = 425

    def draw_player(self):
        """"draw player"""
        self.screen.blit(self.image, (self.rect.x, self.rect.y))