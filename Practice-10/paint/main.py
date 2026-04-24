import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Draw figures")

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen
    screen.fill((255, 255, 255))

    # square
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # right triangle
    right_triangle = [
        (200, 50),    # top
        (200, 150),   # down
        (300, 150)    # right
    ]
    pygame.draw.polygon(screen, (0, 255, 0), right_triangle)

    # equal triangle
    eq_triangle = [
        (400, 150),   # bottom left
        (500, 150),   # bottom right
        (450, 50)     # top center
    ]
    pygame.draw.polygon(screen, (0, 0, 255), eq_triangle)

    # rhombus
    rhombus = [
        (150, 300),   # top
        (200, 350),   # right
        (150, 400),   # bottom
        (100, 350)    # left
    ]
    pygame.draw.polygon(screen, (255, 255, 0), rhombus)

    pygame.display.update()

pygame.quit()
