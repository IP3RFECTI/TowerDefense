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
model = load_model('mnist_dense.h5')
import cv2
import numpy as np

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
# Screen settings
W = 600
H = 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от мыши")

FPS = 60
clock = pygame.time.Clock()
# Coordinates
start_position = end_position = None
mouse_positions = []
save_screen = None
predicted = None

screen.fill(WHITE)
#background = pygame.image.load('assets/images/background.png').convert()
#screen.blit(background, (0, 0))
pygame.display.update()
is_stopped = False

# значения для определения цвета min-max
pygame.mouse.set_visible(False)
hsv_min = np.array((0, 150, 0), np.uint8)
hsv_max = np.array((20, 255, 20), np.uint8)


def predict_digit(imgx):
    img_path = imgx
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    # Преобразуем картинку в массив
    x = image.img_to_array(img)
    # Меняем форму массива в плоский вектор
    x = x.reshape(1, 784)
    # Инвертируем изображение
    x = 255 - x
    # Нормализуем изображение
    x /= 255
    prediction = model.predict(x)
    res = np.argmax(prediction)
    return res

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(screen, BLUE, mouse_pos, 10)

    pressed = pygame.mouse.get_pressed()
    for i in range(len(mouse_positions)):
        pygame.draw.circle(screen, GREEN, mouse_positions[i], 15)
    if pressed[0]:
        if start_position is None:
            start_position = mouse_pos
        mouse_positions.append(mouse_pos)
        width = mouse_pos[0] - start_position[0]
        height = mouse_pos[1] - start_position[1]
        is_stopped = True
    elif is_stopped:
        save_screen = pygame.image.save(screen, "screenshot.jpg")
        img = cv2.imread('screenshot.jpg')
        hsv = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
        result = cv2.inRange(img, hsv_min, hsv_max)
        cv2.imwrite('result.png', result)

        predicted = predict_digit('screenshot.jpg')
        print(predicted)
        predicted = predict_digit('result.png')
        print(predicted)
        mouse_positions.clear()
        start_position = None
        is_stopped = False

    pygame.display.update()

