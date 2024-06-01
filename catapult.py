import random
import pygame
from random import randrange


class Catapult(pygame.sprite.Sprite):
    """enemy actions"""

    def __init__(self, screen, spawn_point):
        """start position"""
        super(Catapult, self).__init__()
        self.screen = screen
        self.height = self.screen.get_height() * 0.6
        # self.direction = direction
        self.spawn_point = spawn_point
        self.end_point = spawn_point / 10 * 9
        self.catapult_image = pygame.transform.flip(pygame.image.load('assets/animations/katapulthrowing/1.png'), 1, 0)
        """animation"""
        self.frame_images = []
        for i in range(1, 9):
            self.frame_images.append(
                pygame.transform.flip(pygame.image.load(f"assets/animations/katapulthrowing/{i}.png"), 1, 0))
        self.counter = 0
        self.animation_length = len(self.frame_images)

        self.clock = pygame.time.Clock()

    def draw_catapult(self):
        """catapult rides"""
        if self.spawn_point >= self.end_point:
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            self.spawn_point -= 1
        else:
            self.play_animation()

    def play_animation(self):
        """catapult throws"""
        self.counter += 1
        if (self.counter >= self.animation_length):
            self.counter = 1
        self.screen.blit(self.frame_images[self.counter], (self.spawn_point, self.height))
        pygame.display.flip()
        self.clock.tick(8)
