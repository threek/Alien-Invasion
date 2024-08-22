import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

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

            # 关于子弹位置的变化 移到 _update_bullet（）方法中了
            # self.bullets.update()
            # # 删除消失的子弹
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom < 0:
            #         self.bullets.remove(bullet)
            # print(len(self.bullets))


            self._update_bullet()

            self._update_aliens()

            # 每次循环时都重绘屏幕。
            self._update_screen()

            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()


    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人。
        #  外星人的间距为外星人宽度。
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size

        # 计算可以容纳多少行外星人
        available_space_x = self.settings.screen_width - (2 * alien_width)

        number_alien_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        number_rows = available_space_y //(2 * alien_height)




        # 创建第一行外星人
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)


    def _create_alien(self,alien_number,row_number):
        # 创建一个外星人并将其加入当前行
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number

        self.aliens.add(alien)

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
        elif event.key == pygame.K_SPACE :
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

        if  len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullet(self):
        """更新子弹的位置 并删除消失的子弹"""

        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self.aliens.update()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)


        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并开始游戏
    ai = AlienInvasion()

    ai.__init__()
    ai.run_game()

