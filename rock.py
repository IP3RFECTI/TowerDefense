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
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        abs_h =
        abs_w =

        self.direction = -x^2-y
        self.spawn_point = spawn_point
        self.end_point = spawn_point / 10 * 2
        self.frame_images = []
        for i in range(1, 14):
            self.frame_images.append(pygame.image.load(f"assets/animations/catapult_throwing/{i}.png"))


    def draw_stone(self):
        """catapult rides"""
        if self.spawn_point >= self.end_point:
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            self.spawn_point -= 1
        elif self.counter >= self.animation_length:
            pass
        else:
            self.play_animation()

    def stone_animation(self):
        """catapult throws"""
        self.counter += 1
        if self.counter >= self.animation_length:
            self.counter = 1
        self.screen.blit(self.frame_images[self.counter], (self.spawn_point, self.height))
        pygame.display.flip()
        self.clock.tick(8)

    def stone_reached_tower(self, x_stone_position):
        """stone animation"""
        if (x_stone_position >= self.damage_position):
            return True
        return False