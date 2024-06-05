import pygame
from rock import Rock
pygame.init()
throw = pygame.mixer.Sound('assets/sounds/Throw.mp3')

class Catapult(pygame.sprite.Sprite):
    """enemy actions"""

    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Catapult, self).__init__()
        self.screen = screen
        self.player = player
        self.height = self.screen.get_height() * 0.5
        # self.direction = direction
        self.spawn_point = spawn_point
        self.end_point = spawn_point / 10 * 9
        self.catapult_image = pygame.transform.flip \
            (pygame.image.load('assets/animations/catapult_throwing/1.png'), 1, 0)
        """animation"""
        self.frame_images = []
        for i in range(1, 9):
            self.frame_images.append(
                pygame.transform.flip(pygame.image.load(f"assets/animations/catapult_throwing/{i}.png"), 1, 0))
        self.is_stopped = False
        self.counter = 0
        self.animation_length = len(self.frame_images)
        self.animation_counter = 7

        self.clock = pygame.time.Clock()
        self.timer_counter = 0

        self.seconds = 2  # time between catapult animation
        self.cooldown_timer = self.seconds * self.clock.tick(30) # animation speed

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
            self.counter += 1
            if self.counter == 3:
                throw.play()
            if self.counter >= self.animation_length:
                self.counter = 1
                self.is_stopped = True
                self.create_rock()
            self.screen.blit(self.frame_images[self.counter], (self.spawn_point, self.height))
            pygame.display.flip()
            self.clock.tick(self.animation_counter)
        else:
            self.animation_is_stopped()
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            pygame.display.flip()
            self.clock.tick(self.cooldown_timer)

    def animation_is_stopped(self):
        if self.timer_counter <= self.cooldown_timer:
            self.timer_counter += 1
            # print(self.timer_counter)
            return True
        self.is_stopped = False
        self.timer_counter = 0
        return False

    def create_rock(self):
        self.rocks.append(Rock(self.screen, self.spawn_point, self.player))