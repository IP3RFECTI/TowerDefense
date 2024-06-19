import pygame
import random


class Rock(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Rock, self).__init__()
        self.player = player
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        # Sounds
        self.hit_sound = pygame.mixer.Sound('assets/sounds/Touch.mp3')
        self.breaking = pygame.mixer.Sound('assets/sounds/Breaking.mp3')

        self.current_point_x = spawn_point
        self.current_point_y = self.height / 2 - 30
        self.end_point_x = self.width * 0.1  # Left side of screen (to trigger Game Over)
        # Images
        self.stone_image = pygame.transform.flip(pygame.image.load('assets/animations/rock/1.png'), 1, 0)
        self.frame_images_rock = []
        self.frame_images_rock_destruction = []
        # Animation
        for i in range(1, 14):
            self.frame_images_rock.append(pygame.image.load(f"assets/animations/rock/{i}.png"))
        self.rock_animation_length = len(self.frame_images_rock)
        for i in range(1, 13):
            self.frame_images_rock_destruction.append(pygame.image.load(f"assets/animations/stonebraking/{i}.png"))
        self.destruction_animation_length = len(self.frame_images_rock)-1

        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.rock_animation_speed_seconds = 10  # more means slower
        self.rock_animation_speed = self.rock_animation_speed_seconds * self.clock.tick(self.FPS)
        self.rock_animation_tick = self.rock_animation_speed // len(self.frame_images_rock)
        self.rock_animation_counter = 0
        self.rock_animation_tick_counter = 1

        self.rock_destruction_speed_seconds = 0.4
        self.rock_destruction_speed = self.rock_destruction_speed_seconds * self.clock.tick(self.FPS)
        self.rock_destruction_tick = self.rock_destruction_speed // len(self.frame_images_rock)
        self.rock_destruction_counter = 0
        self.rock_destruction_tick_counter = 1

        self.rock_velocity = 0.009
        self.predicted = -1
        self.is_hit = False
        self.is_destroyed = False
        self.breaking_sound_played = False
        self.destruction_animation_ended = False
        # Numbers
        self.rnd_number = str(random.randint(0, 9))
        self._ARIAL_50 = pygame.font.SysFont('arial', 40)
        self.rnd_number_surface = self._ARIAL_50.render(self.rnd_number, True, ('#FFFFFF'))

    def update(self):
        """rock flies"""
        if self.predicted == int(self.rnd_number) and not self.breaking_sound_played:
            self.is_destroyed = True
            self.breaking.play()
            self.breaking_sound_played = True
        if self.current_point_x >= self.end_point_x:
            self.current_point_x -= self.current_point_x * self.rock_velocity  # x update
            if not self.is_destroyed:
                self.rock_animation()
            else:
                self.rock_animation_destruction()
        else:
            if not self.breaking_sound_played:
                self.hit_sound.play()
                self.breaking_sound_played = True
                self.player.update_player_hp(100)

    def rock_direction(self):
        a = random.uniform(0.01, 0.1)
        if self.current_point_x >= self.width / 2:
            self.current_point_y -= 1 * self.current_point_x ** 0.5 * a
        else:
            self.current_point_y += 1 * self.current_point_x ** 0.5 * a

    def rock_animation(self):
        """rock animation"""
        self.rock_animation_counter += 1
        if self.rock_animation_counter >= self.rock_animation_length:
            self.rock_animation_counter = 1
            self.rock_animation_tick_counter += 1
            if self.current_point_x <= self.end_point_x:
                self.hit_sound.play()
            self.rock_direction()
        if self.rock_animation_tick_counter >= self.rock_animation_length:
            self.rock_animation_tick_counter = 1
        self.screen.blit(self.frame_images_rock[self.rock_animation_tick_counter * self.rock_animation_length // self.rock_animation_length],
                         (self.current_point_x, self.current_point_y))
        self.screen.blit(self.rnd_number_surface, (self.current_point_x + 40, self.current_point_y + 15))
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def rock_animation_destruction(self):
        """rock animation destruction"""
        if self.rock_destruction_tick_counter < self.destruction_animation_length:
            if self.rock_destruction_counter <= self.rock_destruction_tick:
                self.rock_destruction_counter += 1
            else:
                self.rock_destruction_counter = 0
                self.rock_destruction_tick_counter += 1
        else:
            self.destruction_animation_ended = True
        if self.rock_destruction_tick_counter < self.destruction_animation_length and not self.destruction_animation_ended:
            self.screen.blit(self.frame_images_rock_destruction[self.rock_destruction_tick_counter],
                             (self.current_point_x, self.current_point_y))
            pygame.display.flip()
            self.clock.tick(self.FPS)
