import pygame
from plane_sprites import *

class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        #1.创建游戏主窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        #2.创建游戏时钟
        self.clock = pygame.time.Clock()

        #3.调用私有方法，创建精灵和精灵组
        self.__create_sprites()

        #4.设置定时器事件-创建敌机,
        #第一个参数是事件id，第二个参数是时间，毫秒为单位
        pygame.time.set_timer(ENEMY_EVENT,1000)
        #设置定时器事件，创造子弹，每0.5秒发射3个
        pygame.time.set_timer(BULLET_EVENT,500)

    def __create_sprites(self):
        #创建背景精灵及精灵组,一般只有被多个方法共用的的变量才会被声明为self变量
        bg1 = Background()
        bg2 = Background()
        bg2.rect.y = -SCREEN_RECT.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #创建英雄的精灵和精灵组，要把英雄设置成属性以供别的方法使用
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")
        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2.监听事件
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()




    def __event_handler(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == ENEMY_EVENT:
                #创建敌机精灵
                enemy = Enemy()
                #将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            if event.type == BULLET_EVENT:
                self.hero.fire()
            #注意press和keydown的区别，press会一直反应
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        #敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if enemies:
            self.hero.kill()
            PlaneGame.__game_over()
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
