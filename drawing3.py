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

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
# Screen settings
W = 1280
H = 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от мыши")

FPS = 60
clock = pygame.time.Clock()
# Coordinates
start_position = end_position = None
mouse_positions = []
save_screen = None
predicted = None

screen.fill('black')
#background = pygame.image.load('assets/images/background.png').convert()
#screen.blit(background, (0, 0))
pygame.display.update()
is_stopped = False
white_square = pygame.Surface((150, 200))
white_square.fill('white')


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

    pygame.display.update()
    screen.fill('#D9D9D9')
    screen.blit(white_square, (200, 200))
    mouse_pos = pygame.mouse.get_pos()
    #if pygame.mouse.get_focused():
        #pygame.draw.circle(square, 'black', mouse_pos, 10)

    pressed = pygame.mouse.get_pressed()
    for i in range(len(mouse_positions)):
        pygame.draw.circle(screen, 'black', mouse_positions[i], 15)
    if pressed[0]:
        if start_position is None:
            start_position = mouse_pos
        mouse_positions.append(mouse_pos)
        is_stopped = True
    elif is_stopped:
        rect = pygame.Rect(200, 200, 150, 200)
        sub = screen.subsurface(rect)
        pygame.image.save(sub, "screenshot.jpg")
        img_path = 'screenshot.jpg'
        predicted = predict_digit(img_path)  # число которое предсказано
        white_square.fill("white")
        mouse_positions.clear()
        start_position = None
        is_stopped = False
        print(predicted)



if __name__ == '__main__':
    """run"""
    run()
