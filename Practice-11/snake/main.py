import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

FOOD_COLORS = {
    1: (255, 50,  50),
    2: (255, 165,  0),
    3: (180,  0, 255),
}

snake = [(300, 300)]
dx = CELL
dy = 0

score = 0


def spawn_food():
    r = random.random()
    if r < 0.50:
        weight = 1
    elif r < 0.85:
        weight = 2
    else:
        weight = 3

    life = {1: 7, 2: 5, 3: 4}

    return {
        "x":      random.randrange(0, WIDTH,  CELL),
        "y":      random.randrange(0, HEIGHT, CELL),
        "weight": weight,
        "born":   time.time(),
        "life":   life[weight],
    }


food = spawn_food()

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)

    if new_head == (food["x"], food["y"]):
        score += food["weight"]
        food = spawn_food()
    else:
        snake.pop()

    if time.time() - food["born"] > food["life"]:
        food = spawn_food()

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False

    if new_head in snake[1:]:
        running = False

    screen.fill(BLACK)

    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL, CELL))

    food_size = CELL + food["weight"] * 4
    food_color = FOOD_COLORS[food["weight"]]

    pygame.draw.rect(screen, food_color,
                     (food["x"], food["y"], food_size, food_size))
    screen.blit(font.render(f"+{food['weight']}",
                True, WHITE), (food["x"], food["y"] - 25))

    remaining = max(0, food["life"] - (time.time() - food["born"]))
    ratio = remaining / food["life"]
    bar_w = int(food_size * ratio)
    pygame.draw.rect(screen, WHITE,
                     (food["x"], food["y"] + food_size + 2, food_size, 4))
    pygame.draw.rect(screen, food_color,
                     (food["x"], food["y"] + food_size + 2, bar_w,     4))

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))

    pygame.display.update()

screen.fill(BLACK)
screen.blit(font.render("Game Over",           True, WHITE), (220, 250))
screen.blit(font.render(f"Final Score: {score}", True, WHITE), (200, 290))
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
