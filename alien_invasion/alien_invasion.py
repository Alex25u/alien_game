import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


# 由于我们不再在alien_invasion.py中直接创建外星人，因此无需在这个文件中导入Alien类


def run_game():
    # 初始化游戏并创建一个屏幕对象

    # 初始化背景设置
    pygame.init()

    ai_settings = Settings()

    # 设置游戏屏幕尺寸 （1200， 800）是一个元祖
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船

    # 已经导入Ship模块
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    # 设置背景色(浅灰色)
    bg_color = ai_settings.bg_color

    # 开始游戏的循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
