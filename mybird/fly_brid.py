import pygame,sys
from pygame.locals import *
from mybird.bird.Bird import *

def main():
    WINDOW_WIDTH, WINDOW_HEIGHT=800,600
    BACKGROUND_COLOR=(255,255,255)
    IMAGE_WIDTH,IMAGE_HEIGHT=50,54
    x,y=WINDOW_WIDTH/2,WINDOW_HEIGHT/2
    FPS=60


    start=False
    #刚进入游戏，并未开始时的界面显示
    pygame.init()
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    bird=Bird(IMAGE_WIDTH,IMAGE_HEIGHT,x,y)
    pygame.display.set_caption("飞行小鸟")
    screen.fill((BACKGROUND_COLOR))

    reload_bird_event = USEREVENT + 1
    pygame.time.set_timer(reload_bird_event, 300)
    main_clock = pygame.time.Clock()
    screen.blit(bird.birdImage, bird.rect)
    pygame.display.update()


    while True:
        if start:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==reload_bird_event:
                    bird.kill()
                    y+=10
                    bird = Bird(IMAGE_WIDTH, IMAGE_HEIGHT, x, y)

                elif event.type==MOUSEBUTTONDOWN:
                    bird.kill()
                    y -= 15
                    bird = Bird(IMAGE_WIDTH, IMAGE_HEIGHT, x, y)

            screen.blit(bird.birdImage, bird.rect)
            pygame.display.flip()
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