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
model = load_model('mnist_dense.h5')


def events(screen, main_menu, player, square, radius, myfont, model, last_pos, draw_on, catapult, score):
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
            pygame.draw.circle(square, 'black', event.pos, radius)
            draw_on = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if draw_on:
                pygame.image.save(square.subsurface(pygame.Rect(130, 100, 150, 200)), "screenshot.jpg")
                img_path = "screenshot.jpg"
                predict_digit(img_path, model, catapult, score)
                square.fill("white")
            draw_on = False
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

def enemies_check(screen, enemies):
    """alliens check"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        break

def predict_digit(imgx, model, catapult, score):
    img_path = imgx
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    x = image.img_to_array(img)
    x = x.reshape(1, 784)
    x = 255 - x
    x /= 255
    prediction = model.predict(x)
    res = np.argmax(prediction)
    print("predicted", res)
    for rock in catapult.rocks:
        print("rnd_number", rock.rnd_number)
        if int(rock.rnd_number) == int(res):
            catapult.rocks.remove(rock)
            score.stats.score += 100
    score.image_score()
    # time.sleep(1)
    # return res


def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

