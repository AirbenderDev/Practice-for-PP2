import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK = (35, 35, 35)
GREEN = (0, 170, 0)
RED = (200, 0, 0)
BLUE = (0, 120, 220)
YELLOW = (230, 220, 0)


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen, font):
        mouse = pygame.mouse.get_pos()
        color = GRAY
        if self.rect.collidepoint(mouse):
            color = WHITE
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, txt.get_rect(center=self.rect.center))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)


def draw_text(screen, text, font, color, x, y, center=True):
    img = font.render(text, True, color)
    if center:
        rect = img.get_rect(center=(x, y))
    else:
        rect = img.get_rect(topleft=(x, y))
    screen.blit(img, rect)


def ask_name(screen, clock):
    font = pygame.font.SysFont("Arial", 28)
    small = pygame.font.SysFont("Arial", 22)
    name = ""
    active = True

    while active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 12 and event.unicode.isprintable():
                    name += event.unicode

        screen.fill(DARK)
        draw_text(screen, "Enter your name", font, WHITE, 200, 220)
        pygame.draw.rect(screen, WHITE, (80, 270, 240, 45))
        draw_text(screen, name, font, BLACK, 95, 278, center=False)
        draw_text(screen, "Press ENTER to start", small, WHITE, 200, 350)
        pygame.display.update()
