import pygame
import controls
from player import Player
from score import Scores
from stats import Stats
from pygame.sprite import Group
from main_menu import Menu
from leadearboard import Leaderboard


def run():
    """run game"""
    pygame.init()
    #width = 800
    #height = 360
    width = 800
    height = 360
    main_res = (width, height)
    pygame.display.set_caption("Towers")
    screen = pygame.display.set_mode(main_res)

    """Fonts and images"""
    background = pygame.image.load('assets/images/background.png').convert()
    font = pygame.font.Font('assets/fonts/appetite.ttf', 70)    # НЕ используется на данный момент
    """Music"""
    pygame.mixer.music.load('assets/music/BGMusic1.mp3')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    """Sounds"""
    #For sounds
    #sound1 = pg.mixer.Sound('boom.wav')
    #sound2 = pg.mixer.Sound('one.ogg')

    player = Player(screen)
    enemies = Group()

    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 1000)

    # show_leaders = False
    leaderboard = Leaderboard(screen, width, height)
    main_menu = Menu(screen)
    show_menu(main_menu, screen, leaderboard)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        start = main_menu.start_clicked()
        show_leaders = leaderboard.clicked
        controls.events(screen, main_menu, player, enemy_timer, enemies, width, height)
        controls.show_menu(screen, background, main_menu, width, height)
        if start:
            controls.update(player, score)
            player.update_player()
            controls.update_enemies(enemies, height, score)
            start = controls.game_over(stats, screen, score, player, enemies, height, leaderboard)
        elif show_leaders:
            leaderboard.draw_leaderboards()

        pygame.display.flip()
        pygame.time.Clock().tick(60)


def game_start(main_menu):
    """hide menu"""
    main_menu.delete_options()


def show_menu(main_menu, screen, leaderboard):
    """start menu"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Играть", lambda: game_start(main_menu))
    main_menu.append_option("Рекорды", lambda: show_leadears(main_menu, screen, leaderboard))
    main_menu.append_option("Настройки", lambda: show_settings(main_menu, screen, leaderboard))
    main_menu.append_option("Выход", lambda: quit())


def show_leadears(main_menu, screen, leaderboard):
    """show leaderboards"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Назад", lambda: show_menu(main_menu, screen, leaderboard))
def show_settings(main_menu, screen, leaderboard):
    """show leaderboards"""
    main_menu.delete_options()
    leaderboard.leaderboard_clicked()
    main_menu.append_option("Назад", lambda: show_menu(main_menu, screen, leaderboard))

    # names = []
    # scores = []
    # with open("assets/leaderboard/leaderboard.csv", encoding='utf-8') as r_file:
    #     file_reader = csv.reader(r_file, delimiter="\t")
    #     for row in file_reader:
    #         names.append(row[0])
    #         scores.append(row[1])
    # other_text_font = pygame.font.Font('assets/fonts/appetite.ttf', 50)
    # text1 = other_text_font.render('Hello Привет', True, (180, 0, 0))
    # screen.blit(text1, (100, 100))


if __name__ == '__main__':
    """run"""
    run()