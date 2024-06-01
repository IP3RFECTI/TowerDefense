import random
import pygame
from random import randrange


class Catapult(pygame.sprite.Sprite):
    """enemy actions"""
    def __init__(self, screen, spawn_point):
        """start position"""
        super(Catapult, self).__init__()
        self.screen = screen
        # self.direction = direction
        self.spawn_point = spawn_point
        self.tower_image = pygame.transform.flip(pygame.image.load('assets/animations/katapulthrowing/1.png'), 1, 0)
        self.screen.blit(self.tower_image, (spawn_point, 0))
        """animation"""
        self.frame_images = []
        for i in range(1, 9):
            self.frame_images.append(pygame.transform.flip(pygame.image.load(f"assets/animations/katapulthrowing/{i}.png"), 1, 0))
        self.animation_length = len(self.frame_images)
        self.animation_speed = 15
        self.current_frame_index = 0
        self.animation_timer = 0
        self.frame_position = [0, 0]
        self.window_height = self.screen.get_height()
        self.frame_height = self.frame_images[0].get_height()
        self.frame_position[1] = int(self.window_height * 0.45) - int(self.frame_height / 2)
        self.clock = pygame.time.Clock()
        """moving"""
        self.rect = self.tower_image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = 1
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw_catapult(self):
        """show catapult"""
        self.screen.blit(self.tower_image, (self.spawn_point, self.screen.get_height()*0.6))


    def play_animation(self):
        """catapult rides"""
        # обновление состояния
        time_delta = self.clock.tick(60) / 1000.0
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            current_frame_index = (self.current_frame_index + 1) % self.animation_length
            self.animation_timer -= 1.0 / self.animation_speed

        self.frame_position[0] -= 1  # сдвигаем кадр влево
        # выводим кадры, обновляем экран
        current_frame = self.frame_images[self.current_frame_index]
        self.screen.blit(current_frame, self.frame_position)
        pygame.display.flip()
