import pygame 
import random
from pygame import mixer

pygame.init()
def welcome():
    run3 = True
    intro = pygame.image.load('intro_rg.jpg')
    screen_intro = pygame.display.set_mode((979,612))
    while run3:
        screen_intro.blit(intro,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run3 = False
                run = False
                run2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run3 = False
                    run = False
                    run2 = False

        pygame.display.update()
welcome()



mixer.init()
mixer.music.load('car_race.mp3')
mixer.music.set_volume(9)
mixer.music.play(-1)




display_width = 800
display_height = 600
y = 0
y_change = 10
background = pygame.image.load('bg_rg.png')
coin = pygame.image.load('coin.png')
red = (255,0,0)

game_Display = pygame.display.set_mode((display_width,display_height))
car1 = pygame.image.load('car1.png')
car2 = pygame.image.load('car2.png')
intro = pygame.image.load('intro_rg.jpg')
car1X = 520
car1Y = 380
car2X = random.randint(100,600)
car2Y = 40
car1XChange = 0
car2YChange = 0
coinX = random.randint(100,600)
coinY = 40
coinXChange = 0
coinYChange = 0
speedn = -6
speed = 6
score = 0
blue = (0,255,0)
font = pygame.font.SysFont(None, 53)
icon = pygame.image.load('car_icon.png')
pygame.display.set_icon(icon)

run = True


def end():
    scr2 = pygame.display.set_mode((1000,780))
    go = pygame.image.load('go_rg.jpg')
    run2 = True






    while run2:
        scr2.blit(go,(0,0))
        # text_screen(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2=False




        pygame.display.update()
            

clock = pygame.time.Clock()

    


while run:
    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        game_Display.blit(screen_text, [x,y])
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car1XChange = -speed
                car1X-=speed
            if event.key == pygame.K_RIGHT:
                car1XChange = speed
                car1X+=speed
    if car2Y>600:
        car2X = random.randint(100,600)
        car2Y = 0
    if coinY>600:
        coinX = random.randint(100,600)
        coinY = 0




    def draw_road():
        clock = pygame.time.Clock()
        global y, y_change
        game_Display.blit(background, (0, y))
        game_Display.blit(background, (0, y - display_height))
        y += y_change
        if y >= +display_height:
            y = 0
        clock.tick(900)
    draw_road()
    game_Display.blit(car1,(car1X,car1Y))
    game_Display.blit(car2,(car2X,car2Y))
    car2Y-=speedn
    car1X+=car1XChange
    coinY-=speedn
    
    if abs(car1X-car2X)<50 and abs(car1Y-car2Y)<50:
        mixer.music.load('explosion.mp3')
        mixer.music.set_volume(1)
        mixer.music.play()
        end()
        run = False
    if abs(car1X-coinX)<50 and abs(car1Y-coinY)<50:
        score+=100
        coinX = random.randint(100,600)
        coinY = 0
        print(score)
    if car1X>790:
        end()
        run = False
        # mixer.music.load('car_race.mp3')
        mixer.music.pause()
    if car1X<10:
        end()
        run = False
    game_Display.blit(coin,(coinX,coinY))
    text_screen('SCORE'+str(score),(255,0,25),50,30)
    # text_screen(score,(255,0,25),70,90)
    pygame.display.update()
    clock.tick(1000)
