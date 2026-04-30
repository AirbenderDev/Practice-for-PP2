import pygame
import random
import json
import os
from config import WIDTH, HEIGHT, CELL

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (45, 45, 45)
LIGHT = (220, 220, 220)
RED = (220, 0, 0)
DARK_RED = (120, 0, 0)
BLUE = (0, 120, 255)
YELLOW = (240, 220, 0)
PURPLE = (150, 0, 200)
ORANGE = (255, 150, 0)


def load_settings():
    if not os.path.exists("settings.json"):
        return {"snake_color": [0, 200, 0], "grid": True, "sound": False}
    with open("settings.json", "r") as f:
        return json.load(f)


def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=2)


class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen, font):
        pygame.draw.rect(screen, LIGHT, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        img = font.render(self.text, True, BLACK)
        screen.blit(img, img.get_rect(center=self.rect.center))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class SnakeGame:
    def __init__(self, screen, username, best, db_module):
        self.screen = screen
        self.username = username
        self.best = best
        self.db = db_module
        self.font = pygame.font.SysFont("Arial", 24)
        self.big = pygame.font.SysFont("Arial", 42)
        self.settings = load_settings()
        self.reset()

    def reset(self):
        self.snake = [(300, 300), (280, 300), (260, 300)]
        self.dx, self.dy = CELL, 0
        self.next_dx, self.next_dy = CELL, 0
        self.score = 0
        self.level = 1
        self.eaten = 0
        self.speed = 8
        self.game_over = False
        self.saved = False
        self.obstacles = []
        self.active_power = None
        self.active_until = 0
        self.shield = False
        self.food = self.new_item()
        self.food_value = random.choice([1, 2, 3])
        self.food_time = pygame.time.get_ticks()
        self.poison = self.new_item()
        self.power = None
        self.power_type = None
        self.power_time = 0
        self.last_power_spawn = pygame.time.get_ticks()
        self.move_timer = 0

    def cells(self):
        for x in range(0, WIDTH, CELL):
            for y in range(0, HEIGHT, CELL):
                yield (x, y)

    def new_item(self):
        busy = set(self.snake + self.obstacles)
        free = [c for c in self.cells() if c not in busy]
        return random.choice(free)

    def make_obstacles(self):
        self.obstacles = []
        if self.level < 3:
            return
        count = min(5 + self.level, 20)
        head = self.snake[0]
        while len(self.obstacles) < count:
            block = self.new_item()
            # do not put blocks near head, so snake is not trapped immediately
            if abs(block[0] - head[0]) <= CELL * 2 and abs(block[1] - head[1]) <= CELL * 2:
                continue
            self.obstacles.append(block)

    def draw_grid(self):
        if not self.settings.get("grid", True):
            return
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(self.screen, (230, 230, 230), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(self.screen, (230, 230, 230), (0, y), (WIDTH, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.dy == 0:
                self.next_dx, self.next_dy = 0, -CELL
            elif event.key == pygame.K_DOWN and self.dy == 0:
                self.next_dx, self.next_dy = 0, CELL
            elif event.key == pygame.K_LEFT and self.dx == 0:
                self.next_dx, self.next_dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and self.dx == 0:
                self.next_dx, self.next_dy = CELL, 0

    def current_speed(self):
        sp = self.speed
        now = pygame.time.get_ticks()
        if self.active_power == "speed" and now < self.active_until:
            sp += 5
        if self.active_power == "slow" and now < self.active_until:
            sp = max(4, sp - 4)
        if self.active_power in ["speed", "slow"] and now >= self.active_until:
            self.active_power = None
        return sp

    def update(self, dt):
        now = pygame.time.get_ticks()
        if self.power is None and now - self.last_power_spawn > 7000:
            self.power = self.new_item()
            self.power_type = random.choice(["speed", "slow", "shield"])
            self.power_time = now
            self.last_power_spawn = now
        if self.power is not None and now - self.power_time > 8000:
            self.power = None
            self.power_type = None

        self.move_timer += dt
        if self.move_timer < 1000 / self.current_speed():
            return
        self.move_timer = 0

        self.dx, self.dy = self.next_dx, self.next_dy
        head = self.snake[0]
        new_head = (head[0] + self.dx, head[1] + self.dy)

        hit = (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake or
            new_head in self.obstacles
        )
        if hit:
            if self.shield:
                self.shield = False
                self.active_power = None
                new_head = head
            else:
                self.game_over = True
                return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += self.food_value * 10
            self.eaten += 1
            self.food = self.new_item()
            self.food_value = random.choice([1, 2, 3])
            self.food_time = now
            if self.eaten % 4 == 0:
                self.level += 1
                self.speed += 1
                self.make_obstacles()
        elif new_head == self.poison:
            for _ in range(2):
                if len(self.snake) > 1:
                    self.snake.pop()
            self.poison = self.new_item()
            if len(self.snake) <= 1:
                self.game_over = True
                return
        elif self.power is not None and new_head == self.power:
            if self.active_power is None:
                self.active_power = self.power_type
                if self.power_type in ["speed", "slow"]:
                    self.active_until = now + 5000
                if self.power_type == "shield":
                    self.shield = True
            self.score += 20
            self.power = None
            self.power_type = None
        else:
            self.snake.pop()

        if now - self.food_time > 6000:
            self.food = self.new_item()
            self.food_value = random.choice([1, 2, 3])
            self.food_time = now

    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()

        for b in self.obstacles:
            pygame.draw.rect(self.screen, GRAY, (*b, CELL, CELL))

        pygame.draw.rect(self.screen, RED, (*self.food, CELL, CELL))
        val = self.font.render(str(self.food_value), True, WHITE)
        self.screen.blit(val, val.get_rect(center=(self.food[0] + 10, self.food[1] + 10)))

        pygame.draw.rect(self.screen, DARK_RED, (*self.poison, CELL, CELL))

        if self.power:
            color = ORANGE
            if self.power_type == "slow":
                color = BLUE
            if self.power_type == "shield":
                color = PURPLE
            pygame.draw.rect(self.screen, color, (*self.power, CELL, CELL))

        snake_color = tuple(self.settings.get("snake_color", [0, 200, 0]))
        for part in self.snake:
            pygame.draw.rect(self.screen, snake_color, (*part, CELL, CELL))
            pygame.draw.rect(self.screen, BLACK, (*part, CELL, CELL), 1)

        now = pygame.time.get_ticks()
        info = f"Player: {self.username}  Score: {self.score}  Level: {self.level}  Best: {self.best}"
        self.screen.blit(self.font.render(info, True, BLACK), (10, 10))
        if self.active_power:
            if self.active_power in ["speed", "slow"]:
                left = max(0, (self.active_until - now) // 1000)
                text = f"Power: {self.active_power} {left}s"
            else:
                text = "Power: shield ready"
            self.screen.blit(self.font.render(text, True, BLACK), (10, 40))

    def save_result(self):
        if not self.saved:
            self.db.save_result(self.username, self.score, self.level)
            self.saved = True
