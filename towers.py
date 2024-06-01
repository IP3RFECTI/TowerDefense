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
    # For sounds
    # sound1 = pg.mixer.Sound('boom.wav')
    # sound2 = pg.mixer.Sound('one.ogg')
    """objects"""
    player = Player(screen)
    catapult = Catapult(screen, width * 0.9)
    """menu interface"""
    # show_leaders = False
    leaderboard = Leaderboard(screen)
    settings = Settings(screen)
    main_menu = Menu(screen)
    show_menu(main_menu, screen, leaderboard, settings)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        start = main_menu.start_clicked()
        show_leaders = leaderboard.clicked
        controls.events(screen, main_menu, player)
        controls.show_menu(screen, background, main_menu)
        player.create_player()
        if start:
            controls.update(player, None, score)
            controls.update_catapult(catapult)
            # start = controls.game_over(stats, screen, score, player, leaderboard)
        elif show_leaders:
            leaderboard.draw_leaderboards()

        pygame.display.flip()
        pygame.time.Clock().tick(60)


def game_start(main_menu):
    """hide menu"""
    main_menu.delete_options()


def show_menu(main_menu, screen, leaderboard, settings):
    """start menu"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Играть", lambda: game_start(main_menu))
    main_menu.append_option("Рекорды", lambda: show_leaders(main_menu, screen, leaderboard, settings))
    main_menu.append_option("Настройки", lambda: show_settings(main_menu, screen, leaderboard, settings))
    main_menu.append_option("Выход", lambda: quit())


def show_leaders(main_menu, screen, leaderboard, settings):
    """show leaderboards"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Назад", lambda: show_menu(main_menu, screen, leaderboard, settings))


def show_settings(main_menu, screen, leaderboard, settings):
    """show settings"""
    main_menu.delete_options()
    settings.settings_clicked()
    main_menu.append_option("Назад", lambda: show_menu(main_menu, screen, leaderboard, settings))


if __name__ == '__main__':
    """run"""
    run()
