import pygame
import math

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("-- Paint")

clock = pygame.time.Clock()

BLACK = (0,   0,   0)
BLUE = (0,   0, 255)
RED = (255, 0,   0)
GREEN = (0, 255,   0)
WHITE = (255, 255, 255)
GRAY = (40,  40,  40)

canvas = pygame.Surface((640, 480))
canvas.fill(BLACK)

color = BLUE
radius = 5
mode = "pen"

drawing = False
last_pos = None
start_pos = None

font = pygame.font.SysFont("Arial", 20)

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
            elif event.key == pygame.K_4:
                mode = "square"
            elif event.key == pygame.K_5:
                mode = "rtriangle"
            elif event.key == pygame.K_6:
                mode = "etriangle"
            elif event.key == pygame.K_7:
                mode = "rhombus"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

                if mode != "pen" and start_pos:
                    end_pos = event.pos
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    x = min(x1, x2)
                    y = min(y1, y2)
                    w = abs(x2 - x1)
                    h = abs(y2 - y1)

                    if mode == "rect":
                        pygame.draw.rect(canvas, color, (x, y, w, h), 3)

                    elif mode == "circle":
                        r = max(w, h) // 2
                        pygame.draw.circle(canvas, color, start_pos, r, 3)

                    elif mode == "triangle":
                        points = [((x1 + x2) // 2, y1), (x1, y2), (x2, y2)]
                        pygame.draw.polygon(canvas, color, points, 3)

                    elif mode == "square":
                        side = min(w, h)
                        pygame.draw.rect(canvas, color, (x, y, side, side), 3)

                    elif mode == "rtriangle":
                        points = [(x1, y1), (x1, y2), (x2, y2)]
                        pygame.draw.polygon(canvas, color, points, 3)

                    elif mode == "etriangle":
                        base = abs(x2 - x1)
                        height = int(base * math.sqrt(3) / 2)
                        points = [((x1 + x2) // 2, y2 - height),
                                  (x1, y2), (x2, y2)]
                        pygame.draw.polygon(canvas, color, points, 3)

                    elif mode == "rhombus":
                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2
                        points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                        pygame.draw.polygon(canvas, color, points, 3)

                last_pos = None
                start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pen":
                pygame.draw.line(canvas, color, last_pos, event.pos, radius)
                last_pos = event.pos

    screen.blit(canvas, (0, 0))

    hud_bg = pygame.Surface((640, 24))
    hud_bg.set_alpha(200)
    hud_bg.fill(GRAY)
    screen.blit(hud_bg, (0, 0))

    hud_surf = font.render(
        f"Mode: {mode}  |  P=pen 1=rect 2=circle 3=tri 4=square 5=rtri 6=etri 7=rhombus  |  R/G/B=color",
        True, WHITE
    )
    screen.blit(hud_surf, (4, 2))

    pygame.display.update()

pygame.quit()
