import pygame
from plane_sprites import *
导入模块顺序：标准模块，第三方模块，应用程序模块




def main():
    pygame.init()
    #创建游戏主窗口
    screen = pygame.display.set_mode((480,700))
    #绘制背景图像,三步，加载图片，绘制图片，刷新屏幕
    background = pygame.image.load("./images/background.png")
    screen.blit(background,(0,0))
    # pygame.display.update()
    #绘制英雄的飞机
    hero_image = pygame.image.load("./images/me1.png")
    screen.blit(hero_image,(200,500))
    pygame.display.update()
    #定义游戏时钟
    clock = pygame.time.Clock()
    hero_rect = pygame.Rect(200,500,102,126)


    #设计敌机的精灵
    enemy1 = GameSprite("./images/enemy1.png")
    enemy2 = GameSprite("./images/enemy2.png",2)

    #创建精灵组
    enemy_group = pygame.sprite.Group(enemy1,enemy2)



    #游戏循环
    while True:
        #设定循环的刷新率
        clock.tick(60)




        #监听事件，返回的是一个事件的列表
        for event in pygame.event.get():
            #event.type是一个数字，记录event的类型
            #设置定时器，所谓定时器就是每隔一段时间执行一个动作，定时器其实是一个事件，定义了一个事件，由监听器来监听这个事件
            #使用步骤：命名事件，设置定时器。监听事件
            #用户事件的常量是USER_EVENT，所有自定义的事件常量要用这个常量 
            if event.type == 12:
                pygame.quit()
                exit()
        hero_rect.y -= 1
        #通过重画背景来覆盖之前的图像,注意涂层会互相覆盖，所以一定要在调用upadte方法之前用这个重画背景，
        #draw方法内部应该采用了不同方法，不会覆盖之前的内容
        screen.blit(background,(0,0))
        #rect对象也可以传给blit函数
        screen.blit(hero_image,hero_rect)

         #精灵组控制游戏循环内的代码
        enemy_group.update()
        enemy_group.draw(screen)



        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()