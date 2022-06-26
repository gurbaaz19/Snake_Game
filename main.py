import pygame
import random
import os

pygame.init()

# Handling High Score if it doesnt exit
if not os.path.exists("high_score"):
    f = open("high_score", "w")
    f.write("0")
    f.close()

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
navy_blue = (0, 0, 83)

# Screen Size
screen_width = 800
screen_height = 500

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('The Snakes Game')
pygame.display.update()

# Some Constants
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
fps = 60


def textOnScreen(text, color, pos_x, pos_y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [pos_x, pos_y])


def plotSnakeOnScreen(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Home Screen
def homeScreen():
    exit_home = False
    while not exit_home:
        gameWindow.fill(navy_blue)
        textOnScreen("Welcome to The Snakes Game!!! Press ENTER to continue", yellow, 10, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_home = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_home = True
                    gameLoop()

                if event.key == pygame.K_ESCAPE:
                    exit_home = True

        pygame.display.update()
        clock.tick(fps)


# Game Loop
def gameLoop():
    f = open("high_score")
    high_score = f.read()
    f.close()

    if high_score == "":
        high_score = 0
    else:
        high_score = int(high_score)

    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 400
    snake_y = 250
    snake_size = 10
    initial_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(int(screen_width / 6), int(5 * screen_width / 6))
    food_y = random.randint(int(screen_height / 6), int(5 * screen_height / 6))
    food_size = 5.0
    snake_list = []
    snake_length = 1
    score = 0

    # Actual Loop
    while not exit_game:

        if game_over:
            gameWindow.fill(black)
            textOnScreen(f"Game Over, Your score is {score}!!! Press ENTER to Continue, or ESC to exit", red, 10, 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x == 0:
                        velocity_x = initial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT and velocity_x == 0:
                        velocity_x = -initial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP and velocity_y == 0:
                        velocity_x = 0
                        velocity_y = -initial_velocity

                    if event.key == pygame.K_DOWN and velocity_y == 0:
                        velocity_x = 0
                        velocity_y = initial_velocity

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(int(screen_width / 6), int(5 * screen_width / 6))
                food_y = random.randint(int(screen_height / 6), int(5 * screen_height / 6))
                snake_length += 2
                if score > high_score:
                    high_score = score
                    with open("high_score", "w") as f:
                        f.write(str(high_score))

            gameWindow.fill(black)
            scoreOnScreenText = "Score: " + str(score) + ", High Score: " + str(high_score)
            textOnScreen(scoreOnScreenText, yellow, 10, 10)

            pygame.draw.circle(gameWindow, red, (food_x, food_y), food_size)

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plotSnakeOnScreen(gameWindow, green, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)


homeScreen()

pygame.quit()
quit()
