

import pygame
import random
import os


x = pygame.init()
s_width = 900
s_height = 600
#game
game_window = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("snake")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
pygame.mixer.init()
bgimg = pygame.image.load("res/12.png")
bgimg= pygame.transform.scale(bgimg,(s_width,s_height)).convert_alpha()
#col
pink=	(255,20,147)
orange =(255,69,0)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,250,0)
yellow = (250,250,0)
#game
game_window = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("snake")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()

#func
def text_screen(text, color ,x ,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window, color, snake_list, snake_width, snake_height):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color, [x,y, snake_width, snake_height])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)
#game loop
def game_loop():
    pygame.mixer.music.load("res/Snake Music.mp3")
    pygame.mixer.music.play(-1)
    # var
    hiscore = ""
    if not os.path.exists("res/highscore.txt"):
        with open ("res/highscore.txt","w") as fl:
            fl.write("0")
    with open("res/highscore.txt","r") as f:
        hiscore = f.read()

    game_exit = False
    game_over = False
    snake_width = 30
    snake_height = 30
    snake_x = 100
    snake_y = 100
    fps = 60
    velocity_x = 2
    velocity_y = 2

    food_x = random.randint(30, s_width / 1.5)
    food_y = random.randint(30, s_height / 1.5)
    score = 0
    init_velocity = 4
    font = pygame.font.SysFont(None, 35)
    snake_len = 1
    snake_list = []


    while not game_exit :
        if game_over:
            game_window.fill(white)
            text_screen("Game over , enter to play again", red, s_width/5.2, s_height/3)
            with open('res/highscore.txt', "w") as f:
                f.write(str(hiscore))

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    game_exit=True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    game_exit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity
                    if event.key == pygame.K_d:
                        score+=50

            if snake_x < 0 or snake_y < 0 or snake_x > s_width or snake_y > s_height:
                        game_over = True
                        pygame.mixer.music.load("res/bomb.mp3")
                        pygame.mixer.music.play()

            if abs(snake_x-food_x)<snake_width/1.5 and abs(snake_y-food_y)<snake_height/1.5:

                score+=10
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("res/Beep.mp3"))
                food_x = random.randint(30, s_width / 1.5)
                food_y = random.randint(30, s_height / 1.5)
                snake_len+=7


                if int(hiscore) < int(score):
                    hiscore = str(score)


            if len(snake_list)>snake_len:
                del snake_list[0]



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            game_window.fill(yellow)
            game_window.blit(bgimg,(0,0))
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load("res/bomb.mp3")
                pygame.mixer.music.play()

            plot_snake(game_window,orange,snake_list,snake_width,snake_height)

            text_screen("Score = "+str(score) + " Highscore = " + str(hiscore),red,5,5)

            pygame.draw.rect(game_window, pink, [food_x, food_y, snake_width, snake_height])

        pygame.display.update()

        clock.tick(fps)


    pygame.quit()
    quit()

    ##################
welcome()
