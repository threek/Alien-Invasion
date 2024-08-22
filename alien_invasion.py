import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings = Settings()


        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 想监控鼠标按键事件 和  屏幕更新 事件  单独作为方法独立出去
            # 监视键盘和鼠标事件
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()

            self._check_events()

            self.ship.update()
            self.bullets.update()
            # 每次循环时都重绘屏幕。
            self._update_screen()

            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()

    def _check_events(self):
        """响应鼠标和按键事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    def _check_keydown_event(self,event):
        """响应按键。"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_rigth = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # elif event.key == pygame.K_UP:
        #     self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #     self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_buttle()


    def _check_keyup_event(self,event):
        """响应松开。"""
        if event.key == pygame.K_RIGHT:
            # 停止向右移动飞船
            self.ship.moving_rigth = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # if event.key == pygame.K_UP:
        #     self.ship.moving_up = False
        # if event.key == pygame.K_DOWN:
        #     self.ship.moving_down = False

    def _fire_buttle(self):
        """创建一颗子弹，并加入其编组buttles"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并开始游戏
    ai = AlienInvasion()

    ai.__init__()
    ai.run_game()

