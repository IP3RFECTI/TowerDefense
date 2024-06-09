import time
import pygame
import sys
from catapult import Catapult
from random import randrange

import numpy as np
import os
from tensorflow.keras.models import load_model
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
import random


def events(screen, main_menu, player, square, radius, myfont, model, last_pos, draw_on, catapult, score, is_paused):
    """events processes"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_menu.switch(-1)
            elif event.key == pygame.K_DOWN:
                main_menu.switch(1)
            elif event.key == pygame.K_SPACE:
                if not main_menu.start_clicked():
                    main_menu.select()
                    catapult = Catapult(screen, screen.get_width(), player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Selecting Color Code
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(square, 'black', event.pos, radius)
            draw_on = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            rect = pygame.Rect(0, 0, 150, 200)  # указать область где белый фон и он будет его фоткать
            sub = square.subsurface(rect)
            pygame.image.save(sub, "screenshot.jpg")
            img_path = 'screenshot.jpg'
            predicted = predict_digit(img_path, model)  # число которое предсказано
            check_rocks(catapult.rocks, score, predicted)
            text_surface = myfont.render(f'{predicted}', False, 'red')
            square.fill("white")
            square.blit(text_surface, (0, 100))
        elif event.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(square, 'black', event.pos, radius)
                roundline(square, 'black', event.pos, last_pos, radius)
                last_pos = event.pos
        elif event.type == pygame.USEREVENT:
            pass

def show_menu(screen, background, main_menu):
    """show main menu"""
    screen.blit(background, (0, 0))
    main_menu.draw(screen, screen.get_width() * 0.5, screen.get_height() * 0.2, 75)

def update(player, rocks, score):
    """"screen update"""
    # rocks.draw_rocks()
    player.draw_player()
    score.show_score()


def update_catapult(catapult):
    """"catapult update"""
    catapult.draw_catapult()

def update_rocks(rocks):
    """"enemies update amd score add"""
    for rock in rocks:
        rock.update()
def check_rocks(rocks, score, predicted):
    print("predicted", predicted)
    for rock in rocks:
        print("rnd_number", rock.rnd_number)
        if int(rock.rnd_number) == int(predicted):
            rocks.remove(rock)
            # +100 score

def game_over(screen, score, player, leaderboard, rocks, catapult):
    """update positions"""
    # rocks.update()
    # if pygame.sprite.spritecollideany(player, rocks):
    #     pass
    # enemies_check(screen, rocks)
    pass


def enemies_check(screen, enemies):
    """alliens check"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        break

def predict_digit(imgx, model):
    img_path = imgx
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    x = image.img_to_array(img)
    x = x.reshape(1, 784)
    x = 255 - x
    x /= 255
    prediction = model.predict(x)
    res = np.argmax(prediction)
    # print(res)
    return (res)

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

