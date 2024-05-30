import time
import pygame
import sys
from enemy import Enemy
from random import randrange


def events(screen, main_menu, player, enemy_timer, enemies, width, height):
    """events processes"""
    for event in pygame.event.get():
        if event.type == enemy_timer:
            screen_section = randrange(0, 4)
            direction = 0
            spawn_point = 0
            if screen_section == 0:
                direction = 1
                spawn_point = randrange(0, width-9)
            elif screen_section == 1:
                direction = -1
                spawn_point = randrange(0, width-9)
            elif screen_section == 2:
                direction = 1
                spawn_point = randrange(0, height-9)
            elif screen_section == 3:
                direction = -1
                spawn_point = randrange(0, height-9)
            new_enemy = Enemy(screen, direction, spawn_point, screen_section)
            enemies.add(new_enemy)
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
            elif event.key == pygame.K_a:
                player.mleft = True
            elif event.key == pygame.K_d:
                player.mright = True
            elif event.key == pygame.K_w:
                player.mup = True
            elif event.key == pygame.K_s:
                player.mdown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.mleft = False
            elif event.key == pygame.K_d:
                player.mright = False
            elif event.key == pygame.K_w:
                player.mup = False
            elif event.key == pygame.K_s:
                player.mdown = False


def show_menu(screen, background, main_menu, width, height):
    """show main menu"""
    screen.blit(background, (0, 0))
    main_menu.draw(screen, width * 0.5, height * 0.2, 75)


def ship_kill(stats, score, player, enemies, height, leaderboard):
    """player-alliens contact"""
    if stats.lifes_left > 0:
        stats.lifes_left -= 1
        score.image_lifes()
        enemies.empty()
        update_enemies(enemies, height, score)
        player.create_player()
        time.sleep(1)
    else:
        stats.run_game = False
        leaderboard.write_new_record(score.stats.score)
        sys.exit()


def update(player, score):
    """"screen update"""
    player.draw_player()
    score.show_score()


def update_enemies(enemies, height, score):
    """"enemies update amd score add"""
    for enemy in enemies:
        enemy.draw()
    for enemy in enemies.copy():
        if enemy.rect.y >= height:
            enemies.remove(enemy)
            score.stats.score += 100
        if enemy.rect.x >= height:
            enemies.remove(enemy)
            score.stats.score += 100
    enemies.update()
    score.image_score()


def game_over(stats, screen, score, player, enemies, height, leaderboard):
    """update positions"""
    enemies.update()
    if pygame.sprite.spritecollideany(player, enemies):
        ship_kill(stats, score, player, enemies, height, leaderboard)
    enemies_check(screen, enemies)


def enemies_check(screen, enemies):
    """alliens check"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        break

