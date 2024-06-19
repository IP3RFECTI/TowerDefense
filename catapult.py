import pygame
from rock import Rock


class Catapult(pygame.sprite.Sprite):
    """enemy actions"""

    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Catapult, self).__init__()
        self.screen = screen
        self.player = player
        self.height = self.screen.get_height() * 0.5
        self.spawn_point = spawn_point
        self.end_point = spawn_point / 10 * 9
        self.catapult_image = pygame.transform.flip \
            (pygame.image.load('assets/animations/catapult_throwing/1.png'), 1, 0)
        # Sounds
        self.throw_sound = pygame.mixer.Sound('assets/sounds/Throw.mp3')
        # Animation
        self.frame_images = []
        for i in range(1, 10):
            self.frame_images.append(
                pygame.transform.flip(pygame.image.load(f"assets/animations/catapult_throwing/{i}.png"), 1, 0))
        self.throw_index_len = len(self.frame_images)
        self.is_stopped = False
        self.rock_created = False

        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.cooldown_seconds = 3
        self.cooldown_timer = self.cooldown_seconds * self.clock.tick(self.FPS)/2
        self.cooldown_tick = self.cooldown_timer // self.clock.tick(self.FPS)/2
        self.cooldown_counter = 0

        self.throw_animation_speed_seconds = 3  # more means slower
        self.throw_animation_speed = (self.throw_animation_speed_seconds * self.clock.tick(self.FPS))
        self.throw_animation_tick = self.throw_animation_speed // self.throw_index_len
        self.throw_animation_counter = 0

        self.rocks = []

    def draw_catapult(self):
        """catapult rides"""
        if self.spawn_point >= self.end_point:
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            self.spawn_point -= 1
        else:
            self.catapult_animation()

    def catapult_animation(self):
        """catapult throws"""
        if not self.is_stopped:
            if self.throw_animation_counter // self.throw_animation_tick == 6 and not self.rock_created:
                self.create_rock()
                self.throw_sound.play()
                self.rock_created = True
            if self.throw_animation_counter // self.throw_animation_tick < self.throw_index_len:
                self.screen.blit(self.frame_images[self.throw_animation_counter // self.throw_animation_tick], (self.spawn_point, self.height))
            else:
                self.is_stopped = True
                self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            if self.cooldown_counter == self.cooldown_timer:
                self.is_stopped = True
                self.cooldown_counter = 0
            if self.throw_animation_counter > self.throw_animation_speed:
                self.throw_animation_counter = 0
                self.rock_created = False

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.throw_animation_counter += 1
            self.cooldown_counter += 1
        else:
            self.is_stopped = self.animation_is_stopped()
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def animation_is_stopped(self):
        if self.cooldown_counter <= self.cooldown_timer:
            self.cooldown_counter += 1
            return True
        self.cooldown_counter = 0
        return False

    def create_rock(self):
        self.rocks.append(Rock(self.screen, self.spawn_point, self.player))