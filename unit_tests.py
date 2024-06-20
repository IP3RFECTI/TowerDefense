import unittest
import sys
import time
import pygame
import catapult
import controls
from player import Player
from score import Scores
from stats import Stats
from pygame.sprite import Group
from main_menu import Menu
from leadearboard import Leaderboard
from settings import Settings
from catapult import Catapult
import numpy as np
import os
from rock import Rock

pygame.init()
width = 800
height = 360
main_res = (width, height)
pygame.display.set_caption("Towers")
screen = pygame.display.set_mode(main_res)
stats = Stats()
score = Scores(screen, stats)
player = Player(screen)

class TestMyFunctions(unittest.TestCase):
    # Изменение координат камня
    def test_rock_direction_change(self):
        rock1 = Rock(screen, 10, player)
        first_point = rock1.current_point_y
        rock1.rock_direction()
        second_point = rock1.current_point_y
        if first_point != second_point:
            different = True
        else:
            different = False
        self.assertEqual(different, True)
    # Изменение прочности башни
    def test_player_health_90(self):
        player1 = Player(screen)
        player1.update_player_hp(10)
        self.assertEqual(player1.health, 90)
    # Изменение очков
    def test_score_points_100(self):
        score1 = Scores(screen, stats)
        score1.stats.score += 100
        self.assertEqual(score1.stats.score, 100)
    # Переключение музыки
    def test_music_is_paused(self):
        settings1 = Settings(screen)
        settings1.switch_music()
        self.assertEqual(settings1.music_is_paused, True)
    # Остановка анимации катапульты
    def test_catapult_animation_is_stopped(self):
        catapult1 = Catapult(screen, 0, player)
        catapult1.cooldown_counter = 0
        catapult1.cooldown_timer = 1
        is_stopped = catapult1.animation_is_stopped()
        self.assertEqual(is_stopped, True)
    # Разрушение камня
    def test_rock_is_destroyed(self):
        rock1 = Rock(screen, 0, player)
        rock1.predicted = 4
        rock1.rnd_number = 4
        rock1.update()
        self.assertEqual(rock1.is_destroyed, True)

    if __name__ == '__main__':
        """run"""
        unittest.main()