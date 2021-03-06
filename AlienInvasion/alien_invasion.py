import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship
import game_functions  as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一搜飞船
    ship = Ship(ai_settings ,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人
    alien = Alien(ai_settings,screen)
    """开始游戏的主循环"""
    while True:
        #监视键盘和鼠标事件
            #检查玩家的输入
            gf.check_events(ai_settings, screen, ship, bullets)
            #更新飞船的位置
            ship.update()           
            #未消失的子弹
            gf.update_bullets(bullets)
            #绘制屏幕
            gf.update_screen(ai_settings, screen, ship, alien, bullets)        
run_game()