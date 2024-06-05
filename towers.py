import pygame
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
from tensorflow.keras.models import load_model
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
import random
import pyglet
model = load_model('mnist_dense.h5')
import itertools
# 123455 test
def run():
    """run game"""
    pygame.init()
    width = 800
    height = 360
    main_res = (width, height)
    pygame.display.set_caption("Towers")
    screen = pygame.display.set_mode(main_res)
    """Fonts and images"""
    background = pygame.image.load('assets/images/background.png').convert()
    font_Montserrat = pygame.font.Font('assets/fonts/Montserrat-ExtraBold.ttf', 70)  # НЕ используется здесь
    # Рисование изображения в правой части экрана
    """Music"""
    pygame.mixer.music.load('assets/music/BGMusic1.mp3')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    """Sounds"""
    throw = pygame.mixer.Sound('assets/sounds/Throw.mp3')
    touch = pygame.mixer.Sound('assets/sounds/Touch.mp3')
    breaking = pygame.mixer.Sound('assets/sounds/Breaking.mp3')
    """objects"""
    player = Player(screen)
    catapult = Catapult(screen, width * 0.9, player)
    """menu interface"""
    # show_leaders = False
    leaderboard = Leaderboard(screen)
    settings = Settings(screen)
    main_menu = Menu(screen)
    show_menu(main_menu, screen, leaderboard, settings)
    stats = Stats()
    score = Scores(screen, stats)
    """AI surface"""
    square = pygame.Surface(main_res)
    myfont = pygame.font.Font('assets/fonts/Molot.otf')
    radius = 5
    model = load_model('mnist_dense.h5')
    last_pos = (150, 200)
    draw_on = False


    while True:
        start = main_menu.start_clicked()
        show_leaders = leaderboard.clicked
        controls.events(screen, main_menu, player, square, radius, myfont, model, last_pos, draw_on)
        controls.show_menu(screen, background, main_menu)
        player.create_player()
        if start:
            controls.update(player, None, score)
            controls.update_catapult(catapult)
            controls.update_rocks(catapult.rocks, score)
            screen.blit(square, (0, 0))
        elif show_leaders:
            leaderboard.draw_leaderboards()
        pygame.time.Clock().tick(60)
        pygame.display.flip()


def game_start(main_menu):
    """hide menu"""
    main_menu.delete_options()


def show_menu(main_menu, screen, leaderboard, settings):
    """start menu"""
    main_menu.delete_options()
    main_menu.append_option("Башня мага", lambda: passed())
    main_menu.append_option("Играть", lambda: game_start(main_menu))
    main_menu.append_option("Рекорды", lambda: show_leaders(main_menu, screen, leaderboard, settings))
    main_menu.append_option("Настройки", lambda: show_settings(main_menu, screen, leaderboard, settings))
    main_menu.append_option("Выход", lambda: quit())


def show_leaders(main_menu, screen, leaderboard, settings):
    """show leaderboards"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Рекорды", lambda: passed())
    main_menu.append_option("Назад", lambda: [show_menu(main_menu, screen, leaderboard, settings), leaderboard.leaderboard_clicked()])

def show_settings(main_menu, screen, leaderboard, settings):
    """show settings"""
    main_menu.delete_options()
    settings.settings_clicked()
    main_menu.append_option("Настройки", lambda: passed())
    main_menu.append_option("Музыка", lambda: on_click())
    main_menu.append_option("Назад", lambda: show_menu(main_menu, screen, leaderboard, settings))

def turn_on_music():
    pygame.mixer.music.unpause()
def passed():
    pass

def turn_off_music():
    pygame.mixer.music.pause()


cycled_commands = itertools.cycle([turn_off_music, turn_on_music])

def on_click():
    command = next(cycled_commands)
    return command()

if __name__ == '__main__':
    """run"""
    run()
