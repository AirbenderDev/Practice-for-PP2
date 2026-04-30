import pygame
import sys
from datetime import datetime
import tools

pygame.init()

W, H = 1100, 700
TOOLBAR_W = 120
CANVAS_W = W - TOOLBAR_W

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint")

canvas = pygame.Surface((CANVAS_W, H))
canvas.fill((255, 255, 255))

font = pygame.font.SysFont("Arial", 14)
big_font = pygame.font.SysFont("Arial", 20)

COLORS = [
    (0, 0, 0), (255, 255, 255), (200, 200, 200), (255, 0, 0),
    (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0),
    (128, 0, 128), (0, 255, 255), (255, 105, 180), (139, 69, 19),
]

TOOL_NAMES = ["pencil", "line", "rect", "circle", "square",
              "rtri", "etri", "rhombus", "fill", "text", "eraser"]
SIZES = [2, 5, 10]

tool = "pencil"
color = (0, 0, 0)
size_idx = 0
drawing = False
start_pos = None
prev_pos = None
preview = None

text_mode = False
text_pos = None
text_buf = ""


def canvas_pos(mx, my):
    return mx - TOOLBAR_W, my


def draw_toolbar():
    pygame.draw.rect(screen, (40, 40, 40), (0, 0, TOOLBAR_W, H))

    for i, name in enumerate(TOOL_NAMES):
        tx = 10
        ty = 10 + i * 36
        active = tool == name
        color_btn = (80, 120, 200) if active else (60, 60, 60)
        pygame.draw.rect(screen, color_btn, (tx, ty, 100, 30), border_radius=4)
        label = font.render(name, True, (255, 255, 255))
        screen.blit(label, (tx + 6, ty + 8))

    sy = 420
    screen.blit(font.render("Size:", True, (200, 200, 200)), (10, sy))
    for i, s in enumerate(SIZES):
        bx = 10 + i * 36
        by = sy + 20
        active = size_idx == i
        pygame.draw.rect(screen, (80, 120, 200) if active else (
            60, 60, 60), (bx, by, 30, 24), border_radius=3)
        screen.blit(font.render(str(s), True, (255, 255, 255)), (bx+8, by+5))

    cy_start = 470
    screen.blit(font.render("Colors:", True, (200, 200, 200)), (10, cy_start))
    for i, c in enumerate(COLORS):
        cx = 10 + (i % 3) * 35
        row = i // 3
        cy = cy_start + 18 + row * 35
        pygame.draw.rect(screen, c, (cx, cy, 28, 28))
        if c == color:
            pygame.draw.rect(screen, (255, 255, 255), (cx, cy, 28, 28), 2)

    screen.blit(font.render("Ctrl+S save", True, (150, 150, 150)), (5, H - 20))


clock = pygame.time.Clock()

while True:
    mx, my = pygame.mouse.get_pos()
    cx, cy = canvas_pos(mx, my)
    on_canvas = mx >= TOOLBAR_W

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_mods()

            if event.key == pygame.K_s and keys & pygame.KMOD_CTRL:
                name = "canvas_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
                pygame.image.save(canvas, name)
                print("Saved:", name)

            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                size_idx = event.key - pygame.K_1

            if event.key == pygame.K_ESCAPE and text_mode:
                text_mode = False
                text_buf = ""

            if event.key == pygame.K_RETURN and text_mode:
                surf = big_font.render(text_buf, True, color)
                canvas.blit(surf, text_pos)
                text_mode = False
                text_buf = ""

            if text_mode:
                if event.key == pygame.K_BACKSPACE:
                    text_buf = text_buf[:-1]
                elif event.unicode and event.key not in (pygame.K_RETURN, pygame.K_ESCAPE):
                    text_buf += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not on_canvas:
                for i, name in enumerate(TOOL_NAMES):
                    tx, ty = 10, 10 + i * 36
                    if tx <= mx <= tx+100 and ty <= my <= ty+30:
                        tool = name
                        text_mode = False
                        text_buf = ""

                sy = 440
                for i in range(3):
                    bx = 10 + i * 36
                    if bx <= mx <= bx+30 and sy <= my <= sy+24:
                        size_idx = i

                cy_start = 488
                for i, c in enumerate(COLORS):
                    bx = 10 + (i % 3) * 35
                    row = i // 3
                    bcy = cy_start + row * 35
                    if bx <= mx <= bx+28 and bcy <= my <= bcy+28:
                        color = c
            else:
                if tool == "fill":
                    tools.flood_fill(canvas, (cx, cy), color)
                elif tool == "text":
                    text_mode = True
                    text_pos = (cx, cy)
                    text_buf = ""
                else:
                    drawing = True
                    start_pos = (cx, cy)
                    prev_pos = (cx, cy)
                    preview = canvas.copy()

        if event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            s = SIZES[size_idx]
            if tool == "line":
                tools.draw_line(canvas, start_pos, (cx, cy), color, s)
            elif tool == "rect":
                tools.draw_rect(canvas, start_pos, (cx, cy), color, s)
            elif tool == "circle":
                tools.draw_circle(canvas, start_pos, (cx, cy), color, s)
            elif tool == "square":
                tools.draw_square(canvas, start_pos, (cx, cy), color, s)
            elif tool == "rtri":
                tools.draw_right_triangle(
                    canvas, start_pos, (cx, cy), color, s)
            elif tool == "etri":
                tools.draw_eq_triangle(canvas, start_pos, (cx, cy), color, s)
            elif tool == "rhombus":
                tools.draw_rhombus(canvas, start_pos, (cx, cy), color, s)
            preview = None

        if event.type == pygame.MOUSEMOTION and drawing and on_canvas:
            s = SIZES[size_idx]
            if tool == "pencil":
                tools.pencil(canvas, prev_pos, (cx, cy), color, s)
                prev_pos = (cx, cy)
            elif tool == "eraser":
                tools.pencil(canvas, prev_pos, (cx, cy), (255, 255, 255), s*3)
                prev_pos = (cx, cy)
            elif tool in ("line", "rect", "circle", "square", "rtri", "etri", "rhombus"):
                preview = canvas.copy()

    screen.fill((30, 30, 30))
    draw_toolbar()

    if drawing and preview and tool in ("line", "rect", "circle", "square", "rtri", "etri", "rhombus"):
        tmp = preview.copy()
        s = SIZES[size_idx]
        if tool == "line":
            tools.draw_line(tmp, start_pos, (cx, cy), color, s)
        elif tool == "rect":
            tools.draw_rect(tmp, start_pos, (cx, cy), color, s)
        elif tool == "circle":
            tools.draw_circle(tmp, start_pos, (cx, cy), color, s)
        elif tool == "square":
            tools.draw_square(tmp, start_pos, (cx, cy), color, s)
        elif tool == "rtri":
            tools.draw_right_triangle(tmp, start_pos, (cx, cy), color, s)
        elif tool == "etri":
            tools.draw_eq_triangle(tmp, start_pos, (cx, cy), color, s)
        elif tool == "rhombus":
            tools.draw_rhombus(tmp, start_pos, (cx, cy), color, s)
        screen.blit(tmp, (TOOLBAR_W, 0))
    else:
        screen.blit(canvas, (TOOLBAR_W, 0))

    if text_mode and text_pos:
        preview_text = big_font.render(text_buf + "|", True, color)
        screen.blit(preview_text, (TOOLBAR_W + text_pos[0], text_pos[1]))

    pygame.display.flip()
    clock.tick(60)
