import pygame,sys
from pygame.locals import *
from mybird.bird.Bird import *

def main():
    WINDOW_WIDTH, WINDOW_HEIGHT=500,880
    BACKGROUND_COLOR=(255,255,255)
    IMAGE_WIDTH,IMAGE_HEIGHT=50,54
    x,y=WINDOW_WIDTH/3,WINDOW_HEIGHT/2
    FPS=60
    down='down'
    up='up'

    start=False
    #刚进入游戏，并未开始时的界面显示
    pygame.init()
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    bird=Bird(IMAGE_WIDTH,IMAGE_HEIGHT,x,y,down)
    pygame.display.set_caption("飞行小鸟")
    # screen.fill((BACKGROUND_COLOR))

    #加载标题图片
    title=pygame.image.load('./image/title.png').convert_alpha()
    title_text=pygame.font.SysFont(None,28)
    title_surfce=title_text.render('Click the left mouse button to start the game！',True,(205,105,201))

    BackGroumd=pygame.image.load('./image/backGround.jpg').convert()
    reload_bird_event = USEREVENT + 1
    pygame.time.set_timer(reload_bird_event, 300)
    main_clock = pygame.time.Clock()

    screen.blit(BackGroumd,(0,0))
    screen.blit(title, (100, 270))
    # screen.blit(bird.birdImage, bird.rect)



    pygame.display.update()


    while True:
        if start:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==reload_bird_event:
                    bird.kill()
                    y+=20
                    bird = Bird(IMAGE_WIDTH, IMAGE_HEIGHT, x, y,down)

                elif event.type==MOUSEBUTTONDOWN:
                    bird.kill()
                    y -= 40
                    bird = Bird(IMAGE_WIDTH, IMAGE_HEIGHT, x, y,up)
            screen.blit(BackGroumd,(0,0))
            screen.blit(bird.birdImage, bird.rect)

            pygame.display.update()

            main_clock.tick(FPS)


        else:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==MOUSEBUTTONDOWN:
                    start=not start

if __name__=='__main__':
    main()