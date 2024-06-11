import pygame
import numpy as np
import os
from tensorflow.keras.models import load_model

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
import random


def run():
    """run game"""
    W = 1280
    H = 720
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("События от мыши")
    start = True

    start_position = None
    mouse_positions = []
    predicted = None

    model = load_model('mnist_dense.h5')
    screen.fill('black')
    pygame.display.update()
    is_stopped = False
    white_square = pygame.Surface((150, 200))
    white_square.fill('white')

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        screen.fill('#D9D9D9')
        screen.blit(white_square, (200, 200))
        # background = pygame.image.load('assets/images/background.png').convert()
        # screen.blit(background, (200, 200))
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        for i in range(len(mouse_positions)):
            pygame.draw.circle(screen, 'black', mouse_positions[i], 15)
        if pressed[0]:
            if start_position is None:
                start_position = mouse_pos
            mouse_positions.append(mouse_pos)
            is_stopped = True
            print(pressed)
        elif is_stopped:
            rect = pygame.Rect(200, 200, 150, 200)
            sub = screen.subsurface(rect)
            pygame.image.save(sub, "screenshot.jpg")
            img_path = 'screenshot.jpg'
            predicted = predict_digit(img_path, model)
            white_square.fill("white")
            mouse_positions.clear()
            start_position = None
            is_stopped = False
            print(predicted)


def predict_digit(imgx, model):
    img_path = imgx
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    x = image.img_to_array(img)
    x = x.reshape(1, 784)
    x = 255 - x
    x /= 255
    prediction = model.predict(x)
    res = np.argmax(prediction)
    return res


if __name__ == '__main__':
    """run"""
    run()
