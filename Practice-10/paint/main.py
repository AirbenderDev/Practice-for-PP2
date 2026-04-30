import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("-- Paint")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

screen.fill(BLACK)

color = BLUE
radius = 5

mode = "pen"  # pen, rect, circle, triangle

drawing = False
last_pos = None
start_pos = None

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE

            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_1:
                mode = "rect"
            elif event.key == pygame.K_2:
                mode = "circle"
            elif event.key == pygame.K_3:
                mode = "triangle"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

                if mode != "pen":
                    end_pos = event.pos

                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    x = min(x1, x2)
                    y = min(y1, y2)
                    w = abs(x2 - x1)
                    h = abs(y2 - y1)

                    if mode == "rect":
                        pygame.draw.rect(screen, color, (x, y, w, h), 3)

                    elif mode == "circle":
                        radius_circle = max(w, h) // 2
                        pygame.draw.circle(
                            screen, color, start_pos, radius_circle, 3)

                    elif mode == "triangle":
                        points = [
                            ((x1 + x2) // 2, y1),
                            (x1, y2),
                            (x2, y2)
                        ]
                        pygame.draw.polygon(screen, color, points, 3)

                last_pos = None
                start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pen":
                pygame.draw.line(screen, color, last_pos, event.pos, radius)
                last_pos = event.pos

    pygame.display.update()

pygame.quit()
