import pygame


# throw direction formula
# -x^2-y  || y = -x^2 || x = -sqrt(y)
class Rock(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Rock, self).__init__()
        self.damage_position = player.rect  # На данный момент нет
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.spawn_point = spawn_point

        self.current_point_x = spawn_point
        self.current_point_y = self.height/2

        self.end_point_x = self.width * 0.1
        self.end_point_y = self.height * 0.2

        self.stone_image = pygame.transform.flip(pygame.image.load('assets/animations/rock/1.png'), 1, 0)
        self.frame_images = []
        for i in range(1, 14):
            self.frame_images.append(pygame.image.load(f"assets/animations/rock/{i}.png"))
        self.animation_length = 5

        self.clock = pygame.time.Clock()
        self.is_hit = False
        self.counter = 0
        self.animation_counter = 7

    def rock_update(self):
        """catapult rides"""
        if self.current_point_x >= self.end_point_x:
            self.current_point_x -= self.current_point_x*0.05
            self.rock_animation()
        else:
            print("Game Over")
            self.is_hit = True

    def rock_animation(self):
        """rock animation"""
        self.counter += 1
        if self.counter >= self.animation_length:
            self.counter = 1
            self.is_hit = True
            self.func()
        self.screen.blit(self.frame_images[self.counter], (self.current_point_x, self.current_point_y))
        pygame.display.flip()
        self.clock.tick(self.animation_counter)

    def func(self):
        if self.current_point_x >= self.width/2:
            self.current_point_y -= 1 * self.current_point_x ** 0.5*1.5
        else:
            self.current_point_y += 1 * self.current_point_x ** 0.5*1.5

