import pygame
import random
import time

pygame.init()

# screen settings
WIDTH = 600
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# snake settings
snake = [(300, 300)]
dx = CELL
dy = 0

score = 0

# food settings
food_x = random.randrange(0, WIDTH, CELL)
food_y = random.randrange(0, HEIGHT, CELL)
food_weight = random.randint(1, 3)
food_time = time.time()
food_life = 5   # food dissapears after 5 seconds

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            if event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL

    # snake new head
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    snake.insert(0, new_head)

    # check eating food
    if new_head == (food_x, food_y):
        score += food_weight

        # new random food
        food_x = random.randrange(0, WIDTH, CELL)
        food_y = random.randrange(0, HEIGHT, CELL)
        food_weight = random.randint(1, 3)
        food_time = time.time()
    else:
        snake.pop()

    # food timer
    if time.time() - food_time > food_life:
        food_x = random.randrange(0, WIDTH, CELL)
        food_y = random.randrange(0, HEIGHT, CELL)
        food_weight = random.randint(1, 3)
        food_time = time.time()

    # wall crash
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    # self crash
    if new_head in snake[1:]:
        running = False

    # draw background
    screen.fill(BLACK)

    # draw snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL, CELL))

    # draw food
    food_size = CELL + food_weight * 4
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))

    # draw food weight
    weight_text = font.render(f"+{food_weight}", True, WHITE)
    screen.blit(weight_text, (food_x, food_y - 25))

    # draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

screen.fill(BLACK)

game_over_text = font.render("Game Over", True, WHITE)
score_text = font.render(f"Final Score: {score}", True, WHITE)

screen.blit(game_over_text, (220, 250))
screen.blit(score_text, (200, 290))

pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
