import time
import pygame
import sys
from catapult import Catapult
from random import randrange


def events(screen, main_menu, player):
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
                    catapult = Catapult(screen, screen.get_width())
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

# Rocks update
def game_over(stats, screen, score, player, leaderboard, rocks):
    """update positions"""
    rocks.update()
    if pygame.sprite.spritecollideany(player, rocks):
        # ship_kill(stats, score, player, enemies, height, leaderboard)
        pass
    enemies_check(screen, rocks)


def enemies_check(screen, enemies):
    """alliens check"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        break

