import pygame
import random
pygame.init()

class Rock(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Rock, self).__init__()
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()

        self.hitted = pygame.mixer.Sound('assets/sounds/Touch.mp3')
        self.breaking = pygame.mixer.Sound('assets/sounds/Breaking.mp3')

        self.current_point_x = spawn_point
        self.current_point_y = self.height/2 - 30
        self.end_point_x = self.width * 0.1     # Left side of screen (to trigger Game Over)
        # images
        self.stone_image = pygame.transform.flip(pygame.image.load('assets/animations/rock/1.png'), 1, 0)
        self.frame_images_rock = []
        self.frame_images_rock_destruction = []
        for i in range(1, 14):
            self.frame_images_rock.append(pygame.image.load(f"assets/animations/rock/{i}.png"))
        for i in range(1, 13):
            self.frame_images_rock_destruction.append(pygame.image.load(f"assets/animations/stonebraking/{i}.png"))
        self.animation_length = 5
        self.counter = 0
        self.animation_counter = 7
        self.animation_destruction_length = 5
        self.counter2 = 0
        self.animation_counter_destruction = 26

        self.is_hit = False
        self.is_destroyed = False
        self.breaking_sound_played = False
        self.clock = pygame.time.Clock()
        #number
        self.rnd_number = str(random.randint(0, 9))
        self._ARIAL_50 = pygame.font.SysFont('arial', 50)
        self.rnd_number_surface = self._ARIAL_50.render(self.rnd_number, True, ('#FFFFFF'))

    def rock_update(self):
        """catapult rides"""
        if self.current_point_x >= self.end_point_x:
            self.current_point_x -= self.current_point_x*0.05   # x update
            if self.is_destroyed:
                self.rock_animation_destruction()
            else:
                self.rock_animation()
        else:
            self.is_hit = True

    def rock_animation(self):
        """rock animation"""
        self.counter += 1
        if self.counter >= self.animation_length:
            self.counter = 1
            self.is_hit = True
            if self.current_point_x <= self.end_point_x:
                self.hitted.play()
            self.rock_direction()
        self.screen.blit(self.frame_images_rock[self.counter], (self.current_point_x, self.current_point_y))
        self.screen.blit(self.rnd_number_surface, (self.current_point_x+30, self.current_point_y))
        pygame.display.flip()
        self.clock.tick(self.animation_counter)

    def rock_direction(self):
        a = random.uniform(0.1, 1)
        if self.current_point_x >= self.width/2:
            self.current_point_y -= 1 * self.current_point_x ** 0.5*a
        else:
            self.is_destroyed = True
            if not self.breaking_sound_played:
                self.breaking.play()
                self.breaking_sound_played = True
            # self.current_point_y += 1 * self.current_point_x ** 0.5*a

    def rock_animation_destruction(self):
        """rock animation destruction"""
        self.counter2 += 1
        if self.counter2 <= self.animation_destruction_length:
            self.screen.blit(self.frame_images_rock_destruction[self.counter2],
                             (self.current_point_x, self.current_point_y))
            pygame.display.flip()
            self.clock.tick(self.animation_counter_destruction)
