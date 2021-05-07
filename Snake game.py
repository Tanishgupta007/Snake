import random
import pygame
import os


pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)


width = 1350
height = 720
GameWindow = pygame.display.set_mode((width, height))

bgimg = pygame.image.load("i.jpg")
bgimg = pygame.transform.scale(bgimg, (width, height)).convert_alpha()
pygame.display.set_caption("Snake Game - TANISH GUPTA")
pygame.display.update()
# Game Specific Variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("None", 55)
font2 = pygame.font.SysFont("None", 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x, y])


def text_name(text, color, x, y):
    name_text = font.render(text, True, color)
    GameWindow.blit(name_text, [x, y])


def plot_snake(GameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(GameWindow, black, [x, y, snake_size, snake_size])


# Creating Welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        GameWindow.fill(blue)
        text_screen("Welcome To Snakes", white, 500, 250)
        text_screen("Press Space Bar To Play", red, 480, 390)
        text_screen("TANISH GUPTA", yellow, 900, 650)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(120)


# Creating game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55

    velocity_x = 0
    velocity_y = 0
    width = 1350
    height = 720

    snk_list = []
    snk_length = 1

    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(0, width / 2)
    food_y = random.randint(0, height / 2)
    score = 0
    init_velocity = 2
    snake_size = 20
    fps = 120
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            GameWindow.fill(white)
            text_screen(f"Game Over!!! , Press enter to continue ", red, 360, 300)
            #text_name("@ TANISH GUPTA", blue, 1300, 800)
            text_screen(" @ TANISH GUPTA", blue, 900, 650)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_KP_6:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP_4:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_KP_8:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN or event.key == pygame.K_KP_2:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 10
                pygame.mixer.music.load('Eating.mp3.mp3')
                pygame.mixer.music.play()
                snake_size = 20
                food_x = random.randint(0, width / 2)
                food_y = random.randint(0, height / 2)
                snk_length += 20
                if score > (int(hiscore)):
                    hiscore = score
            GameWindow.fill(white)
            GameWindow.blit(bgimg, (0, 0))
            text_screen("score =" + str(score) + " Hiscore = " + str(hiscore), red, 3, 3)
            pygame.draw.rect(GameWindow, red, [food_x, food_y, snake_size, snake_size])
           # text_name("Tanish Gupta", yellow, 300, 300)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('out.mp3.mp3')
                pygame.mixer.music.play()
                with open("hiscore.txt", "w") as f:
                    f.write(str(hiscore))
            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                pygame.mixer.music.load('out.mp3.mp3')
                pygame.mixer.music.play()
                with open("hiscore.txt", "w") as f:
                    f.write(str(hiscore))
                print("Game over")
            plot_snake(GameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
