import unittest

import unit_tests
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
from tensorflow.keras.models import load_model
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
import random
import itertools
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
is_stopped = False
myfont = pygame.font.Font('assets/fonts/Molot.otf', 30)
text_pause = myfont.render('Игра приостановлена', True, 'red')
model = load_model('mnist_dense.h5')


def run():
    """run game"""
    pygame.init()
    width = 800
    height = 360
    main_res = (width, height)
    pygame.display.set_caption("Towers")
    screen = pygame.display.set_mode(main_res)
    is_paused = False
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
    radius = 5
    model = load_model('mnist_dense.h5')
    last_pos = (150, 200)
    draw_on = False
    start_position = end_position = None
    mouse_positions = []
    white_square = pygame.Surface((150, 200))
    white_square.fill('#FFFFFF')

    while True:
        start = main_menu.start_clicked()
        show_leaders = leaderboard.clicked
        controls.events(screen, main_menu, player, square, radius, myfont, model, last_pos, draw_on, catapult, score)
        controls.show_menu(screen, background, main_menu)
        if not start:
            player.draw_player()
        keys = pygame.key.get_pressed()
        if start:
            screen.blit(white_square, (130, 100))
            controls.update(player, None, score)
            if keys[pygame.K_ESCAPE]:
                time.sleep(0.5)
                is_paused = pause(is_paused)
            if not is_paused:
                controls.update_catapult(catapult)
                controls.update_rocks(catapult.rocks)
                player.draw_player_hp()
                draw(mouse_positions, screen, start_position, white_square, catapult)
            else:
                screen.blit(text_pause, (250, 145))
        elif show_leaders:
            leaderboard.draw_leaderboards()
        pygame.time.Clock().tick(60)
        pygame.display.flip()


def draw(mouse_positions, screen, start_position, squaree, catapult):
    global is_stopped
    mouse_pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    for i in range(len(mouse_positions)):
        pygame.draw.circle(screen, 'black', mouse_positions[i], 10)
    if pressed[0]:
        if start_position is None:
            start_position = mouse_pos
        mouse_positions.append(mouse_pos)
        is_stopped = True
    elif is_stopped:
        rect = pygame.Rect(130, 100, 150, 200)
        sub = screen.subsurface(rect)
        pygame.image.save(sub, "screenshot.jpg")
        img_path = 'screenshot.jpg' # число которое предсказано
        squaree.fill("white")
        mouse_positions.clear()
        start_position = None
        is_stopped = False
    pygame.display.update()


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
    main_menu.append_option("Назад", lambda: [show_menu(main_menu, screen, leaderboard, settings),
                                              leaderboard.leaderboard_clicked()])


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

def pause(is_paused):
    if not is_paused:
        return True
    else:
        return False

def game_over():
    start = False


if __name__ == '__main__':
    """run"""
    test = unittest.Test()
    run()
