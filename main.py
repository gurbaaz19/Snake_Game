import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Screen Size
screen_width = 800
screen_height = 500

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('Snakes Game')
pygame.display.update()

# Game Specific Window
exit_game = False
game_over = False
snake_x = 400
snake_y = 250
snake_size = 15
velocity_x = 0
velocity_y = 0
food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)
food_size = 5.0
fps = 60

clock = pygame.time.Clock()
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -10

            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 10

    snake_x += velocity_x
    snake_y += velocity_y

    gameWindow.fill(white)
    pygame.draw.circle(gameWindow, red,(food_x,food_y),food_size)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
