import random
import pygame

#屏幕大小常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#背景图片地址
IMAGE_NAME = "./images/background.png"
#敌机定时器事件id常量
ENEMY_EVENT = pygame.USEREVENT
#子弹定时器事件id常量
BULLET_EVENT = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        #调用父类的init方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #在屏幕上向下运动
        self.rect.y += self.speed


class Background(GameSprite):
    '''背景精灵'''
    def __init__(self):
        super().__init__(IMAGE_NAME)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    '''敌机精灵'''
    def __init__(self):
        #1.调用父类方法创建敌机精灵，并指定敌机图片
        super().__init__("./images/enemy1.png")
        #2.指定敌机的初始随机速度1~3
        self.speed = random.randint(1,3)
        #3.指定敌机的初始随机位置
        self.rect.bottom = 0#设置y方向的初始位置使其平缓进入
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
         #1.调用父类方法，保持向下飞行
        super().update()
        #2.判断是否飞出屏幕，若是，则从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            #会自动调用del方法从内存中去除
            self.kill()

class Hero(GameSprite):
    '''英雄精灵'''
    def __init__(self):
        #1.调用父类方法，设置image/speed
        super().__init__("./images/me1.png",0)
        #2.设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120
        #3.创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group()
    def update(self):
        #英雄在水平方向移动
        self.rect.x+=self.speed
        #控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right >SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        for i in (0,1,2):
            #1.创建子弹精灵
            bullet = Bullet()
            #2.设置精灵的位置
            bullet.rect.bottom = self.rect.top-i*20
            bullet.rect.centerx = self.rect.centerx
            #3.添加到精灵组
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        #判断子弹是否飞出屏幕
        if self.rect.bottom<0:
            self.kill()