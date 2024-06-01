import random
import pygame
from random import randrange


# throw direction formula
# -x^2-y
class Catapult(pygame.sprite.Sprite):
    """enemy actions"""
    def __init__(self, screen, direction, spawn_point, screen_section):
        """start position"""
        super(Catapult, self).__init__()
        self.screen = screen
        self.direction = direction
        self.spawn_point = spawn_point
        self.screen_section = screen_section
        self.image = pygame.image.load('assets/images/enemies/enemy' + str(randrange(1, 4)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = 1
        if self.screen_section == 0:
            self.rect.x = self.spawn_point
            self.rect.y = 0
        if self.screen_section == 1:
            self.rect.x = self.spawn_point
            self.rect.y = 890
        if self.screen_section == 2:
            self.rect.y = self.spawn_point
            self.rect.x = 0
        if self.screen_section == 3:
            self.rect.y = self.spawn_point
            self.rect.x = 890
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_stone(self):
        """show alien"""
        pass

    def stone_reached_tower(self, x_stone_position):
        if (x_stone_position <= self.screen.get_width()*0.15):
            return True
        return False
