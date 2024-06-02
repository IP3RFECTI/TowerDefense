import pygame


# throw direction formulaffffffffffff
# -x^2-y  || y = -x^2 || x = -sqrt(y)
class Stone(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_point, player):
        """start position"""
        super(Stone, self).__init__()
        self.damage_position = player.posititon # На данный момент нет
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.spawn_point = spawn_point

        self.start_point_x = spawn_point
        self.start_point_y = -(spawn_point**(1/2))

        self.end_point_x = self.width * 0.2
        self.end_point_y = self.height * 0.3

        self.stone_image = pygame.transform.flip(pygame.image.load('assets/animations/rock/1.png'), 1, 0)
        self.frame_images = []
        for i in range(1, 14):
            self.frame_images.append(pygame.image.load(f"assets/animations/rock/{i}.png"))

        self.is_stopped = False
        self.counter = 0
        self.animation_counter = 5

    def draw_stone(self):
        """catapult rides"""
        if self.spawn_point >= self.end_point:
            self.screen.blit(self.stone_image, (self.spawn_point, self.height))
            self.spawn_point -= 1
        else:
            self.stone_animation()

    def stone_animation(self):
        """catapult throws"""
        if not self.is_stopped:
            self.counter += 1
            if self.counter >= self.animation_length:
                self.counter = 1
                self.is_stopped = True
            self.screen.blit(self.frame_images[self.counter], (self.spawn_point, self.height))
            pygame.display.flip()
            self.clock.tick(self.animation_counter)
        else:
            self.animation_is_stopped()
            self.screen.blit(self.catapult_image, (self.spawn_point, self.height))
            pygame.display.flip()
            self.clock.tick(self.cooldown_timer)

    def stone_reached_tower(self, x_stone_position):
        """stone animation"""
        if (x_stone_position >= self.damage_position):
            return True
        return False