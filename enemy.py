import random

import pygame
from random import randrange


class Enemy(pygame.sprite.Sprite):
    """enemy actions"""
    def __init__(self, screen, direction, spawn_point, screen_section):
        """start position"""
        super(Enemy, self).__init__()
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

    def draw(self):
        """show alien"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """allies move"""
        if self.screen_section == 0:
            self.y += self.direction * self.speed
            self.rect.y = self.y
        elif self.screen_section == 1:
            self.y += self.direction * self.speed
            self.rect.y = self.y
        elif self.screen_section == 2:
            self.x += self.direction * self.speed
            self.rect.x = self.x
        elif self.screen_section == 3:
            self.x += self.direction * self.speed
            self.rect.x = self.x