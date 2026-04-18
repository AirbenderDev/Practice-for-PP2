import pygame


class Ball:
    def __init__(self, x: int, y: int, radius: int = 25, step: int = 20):
        self.x = x
        self.y = y
        self.radius = radius
        self.step = step
        self.color = (255, 0, 0)

    def move_left(self, screen_width: int) -> None:
        if self.x - self.step - self.radius >= 0:
            self.x -= self.step

    def move_right(self, screen_width: int) -> None:
        if self.x + self.step + self.radius <= screen_width:
            self.x += self.step

    def move_up(self, screen_height: int) -> None:
        if self.y - self.step - self.radius >= 0:
            self.y -= self.step

    def move_down(self, screen_height: int) -> None:
        if self.y + self.step + self.radius <= screen_height:
            self.y += self.step

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
