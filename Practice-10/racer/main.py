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
car = pygame.transform.scale(car, (60, 100))
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

coin_x = random.randint(20, 370)
coin_y = -50
coins = 0

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

        text1 = font.render("GAME OVER", True, (255, 0, 0))
        text2 = font.render(f"Coins: {coins}", True, (255, 255, 255))
        text3 = font.render("Press Q to quit", True, (200, 200, 200))

        screen.blit(text1, (105, 220))
        screen.blit(text2, (135, 280))
        screen.blit(text3, (95, 340))

        if keys[pygame.K_q]:
            running = False

        pygame.display.update()
        continue

    # moving
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < 340:
        car_x += 5

    # enemy move
    enemy_y += enemy_speed
    if enemy_y > 600:
        enemy_y = -100
        enemy_x = random.randint(0, 340)

    # coin move
    coin_y += 4
    if coin_y > 600:
        coin_y = -50
        coin_x = random.randint(20, 370)

    car_rect = pygame.Rect(car_x, car_y, 60, 100)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 60, 100)
    coin_rect = pygame.Rect(coin_x - 15, coin_y - 15, 30, 30)

    # crash
    if car_rect.colliderect(enemy_rect):
        pygame.mixer.music.stop()

        if not crash_played:
            crash_sound.play()
            crash_played = True

        game_over = True

    # get coin
    if car_rect.colliderect(coin_rect):
        coins += 1
        coin_y = -50
        coin_x = random.randint(20, 370)

    screen.blit(background, (0, 0))
    screen.blit(car, (car_x, car_y))
    screen.blit(enemy, (enemy_x, enemy_y))

    pygame.draw.circle(screen, (255, 215, 0), (coin_x, coin_y), 15)

    text = font.render(f"Coins: {coins}", True, (255, 255, 255))
    screen.blit(text, (250, 10))

    pygame.display.update()

pygame.quit()
