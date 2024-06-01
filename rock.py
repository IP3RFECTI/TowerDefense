import random
import pygame
from random import randrange


# throw direction formula
# -x^2-y
class Stone(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Stone, self).__init__()
        self.damage_position = player.posititon # На данный момент нет

    def draw_stone(self):
        """show stone"""
        pass

    def stone_reached_tower(self, x_stone_position):
        """stone animation"""
        if (x_stone_position >= self.damage_position):
            return True
        return False