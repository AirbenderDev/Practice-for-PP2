import pygame
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer FOR Real Players")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

background = pygame.image.load("sources/AnimatedStreet.png")
car = pygame.image.load("sources/Player.png")
enemy = pygame.image.load("sources/Enemy.png")

background = pygame.transform.scale(background, (400, 600))
car = pygame.transform.scale(car,   (60, 100))
enemy = pygame.transform.scale(enemy, (60, 100))

pygame.mixer.music.load("sources/background.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound("sources/crash.wav")

car_x = 170
car_y = 480

enemy_x = random.randint(0, 340)
enemy_y = -100
enemy_speed = 5

COIN_TYPES = [
    {"weight": 1, "color": (200, 200, 200), "label": "+1"},
    {"weight": 3, "color": (255, 215,   0), "label": "+3"},
    {"weight": 5, "color": (0,   200, 255), "label": "+5"},
]


def spawn_coin():
    r = random.random()
    if r < 0.60:
        coin_type = COIN_TYPES[0]
    elif r < 0.90:
        coin_type = COIN_TYPES[1]
    else:
        coin_type = COIN_TYPES[2]

    return {
        "x":      random.randint(20, 370),
        "y": -50,
        "weight": coin_type["weight"],
        "color":  coin_type["color"],
        "label":  coin_type["label"],
    }


coin = spawn_coin()
coins = 0

SPEED_THRESHOLD = 5

running = True
game_over = False
crash_played = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        screen.fill((0, 0, 0))
        screen.blit(font.render("GAME OVER",       True,
                    (255, 0,   0)),   (105, 220))
        screen.blit(font.render(
            f"Coins: {coins}", True, (255, 255, 255)), (135, 280))
        screen.blit(font.render("Press Q to quit",
                    True, (200, 200, 200)), (95,  340))

        if keys[pygame.K_q]:
            running = False

        pygame.display.update()
        continue

    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < 340:
        car_x += 5

    enemy_y += enemy_speed
    if enemy_y > 600:
        enemy_y = -100
        enemy_x = random.randint(0, 340)

    coin["y"] += 4
    if coin["y"] > 600:
        coin = spawn_coin()

    car_rect = pygame.Rect(car_x,          car_y,          60, 100)
    enemy_rect = pygame.Rect(enemy_x,        enemy_y,        60, 100)
    coin_rect = pygame.Rect(coin["x"] - 15, coin["y"] - 15, 30,  30)

    if car_rect.colliderect(enemy_rect):
        pygame.mixer.music.stop()
        if not crash_played:
            crash_sound.play()
            crash_played = True
        game_over = True

    if car_rect.colliderect(coin_rect):
        coins += coin["weight"]
        enemy_speed = 5 + (coins // SPEED_THRESHOLD)
        coin = spawn_coin()

    screen.blit(background, (0, 0))
    screen.blit(car,        (car_x,   car_y))
    screen.blit(enemy,      (enemy_x, enemy_y))

    pygame.draw.circle(screen, coin["color"], (coin["x"], coin["y"]), 15)
    screen.blit(font.render(coin["label"],      True,
                (0,   0,   0)),   (coin["x"] - 12, coin["y"] - 10))
    screen.blit(font.render(f"Coins: {coins}",
                True, (255, 255, 255)), (250, 10))
    screen.blit(font.render(
        f"Speed: {enemy_speed}", True, (255, 200, 0)), (10, 10))

    pygame.display.update()

pygame.quit()
