import pygame
import random
import time
from persistence import add_score
from ui import draw_text

WIDTH = 400
HEIGHT = 600
ROAD_LEFT = 40
ROAD_RIGHT = 358
LANES = [90, 160, 235, 305]
FINISH_DISTANCE = 2500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 120, 255)
YELLOW = (240, 220, 0)
PURPLE = (160, 0, 200)
ORANGE = (230, 120, 0)
GRAY = (100, 100, 100)


def load_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image


class Game:
    def __init__(self, screen, clock, settings, username):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.username = username
        self.font = pygame.font.SysFont("Arial", 22)
        self.big_font = pygame.font.SysFont("Arial", 32)

        self.road = load_image("assets/road.png", (WIDTH, HEIGHT))
        self.player_img = load_image("assets/player.png", (44, 96))
        self.enemy_img = load_image("assets/enemy.png", (48, 93))
        self.apply_car_color()

        self.crash_sound = None
        if self.settings["sound"]:
            try:
                self.crash_sound = pygame.mixer.Sound("assets/crash.wav")
            except Exception:
                self.crash_sound = None

        self.reset()

    def apply_car_color(self):
        if self.settings["car_color"] == "red":
            self.player_img.fill((255, 80, 80, 80), special_flags=pygame.BLEND_RGBA_ADD)
        elif self.settings["car_color"] == "green":
            self.player_img.fill((80, 255, 80, 80), special_flags=pygame.BLEND_RGBA_ADD)

    def reset(self):
        self.player = self.player_img.get_rect(center=(LANES[1], 500))
        self.traffic = []
        self.obstacles = []
        self.coins = []
        self.powerups = []
        self.road_y = 0
        self.distance = 0
        self.coins_count = 0
        self.score = 0
        self.speed = 5
        self.shield = False
        self.active_power = None
        self.power_end = 0
        self.spawn_timer = 0
        self.coin_timer = 0
        self.power_timer = 0
        self.game_over = False
        self.won = False

        if self.settings["difficulty"] == "easy":
            self.speed = 4
        elif self.settings["difficulty"] == "hard":
            self.speed = 6

    def safe_lane(self):
        safe = []
        for lane in LANES:
            if abs(lane - self.player.centerx) > 40:
                safe.append(lane)
        if not safe:
            return random.choice(LANES)
        return random.choice(safe)

    def spawn_traffic(self):
        lane = self.safe_lane()
        rect = self.enemy_img.get_rect(center=(lane, -70))
        self.traffic.append(rect)

    def spawn_obstacle(self):
        lane = self.safe_lane()
        kind = random.choice(["barrier", "oil", "pothole", "bump", "nitro_strip"])
        rect = pygame.Rect(lane - 22, -40, 44, 35)
        self.obstacles.append({"rect": rect, "kind": kind})

    def spawn_coin(self):
        lane = self.safe_lane()
        value = random.choice([1, 2, 3])
        rect = pygame.Rect(lane - 12, -25, 24, 24)
        self.coins.append({"rect": rect, "value": value})

    def spawn_powerup(self):
        lane = self.safe_lane()
        kind = random.choice(["nitro", "shield", "repair"])
        rect = pygame.Rect(lane - 15, -30, 30, 30)
        self.powerups.append({"rect": rect, "kind": kind, "born": time.time()})

    def activate_powerup(self, kind):
        if self.active_power is not None:
            return
        if kind == "nitro":
            self.active_power = "nitro"
            self.power_end = time.time() + 4
            self.score += 30
        elif kind == "shield":
            self.active_power = "shield"
            self.shield = True
            self.score += 20
        elif kind == "repair":
            if self.obstacles:
                self.obstacles.pop(0)
            self.score += 25

    def hit(self):
        if self.shield:
            self.shield = False
            self.active_power = None
            return
        if self.crash_sound:
            self.crash_sound.play()
        self.game_over = True
        add_score(self.username, self.score, self.distance)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.left > ROAD_LEFT:
            self.player.x -= 5
        if keys[pygame.K_RIGHT] and self.player.right < ROAD_RIGHT:
            self.player.x += 5
        if keys[pygame.K_UP] and self.player.top > 0:
            self.player.y -= 4
        if keys[pygame.K_DOWN] and self.player.bottom < HEIGHT:
            self.player.y += 4

        current_speed = self.speed + self.distance // 500
        if self.active_power == "nitro":
            current_speed += 4
            if time.time() > self.power_end:
                self.active_power = None

        self.road_y += current_speed
        if self.road_y >= HEIGHT:
            self.road_y = 0

        self.distance += current_speed * 0.08
        self.score = int(self.distance) + self.coins_count * 10

        self.spawn_timer += 1
        self.coin_timer += 1
        self.power_timer += 1

        spawn_limit = max(25, 70 - int(self.distance // 100))
        if self.spawn_timer > spawn_limit:
            self.spawn_timer = 0
            if random.random() < 0.65:
                self.spawn_traffic()
            else:
                self.spawn_obstacle()

        if self.coin_timer > 60:
            self.coin_timer = 0
            self.spawn_coin()

        if self.power_timer > 300:
            self.power_timer = 0
            self.spawn_powerup()

        for rect in self.traffic:
            rect.y += current_speed
            if self.player.colliderect(rect):
                self.hit()
        self.traffic = [r for r in self.traffic if r.top < HEIGHT]

        for item in self.obstacles:
            item["rect"].y += current_speed
            if self.player.colliderect(item["rect"]):
                if item["kind"] == "oil":
                    self.player.x += random.choice([-35, 35])
                elif item["kind"] == "nitro_strip":
                    self.active_power = "nitro"
                    self.power_end = time.time() + 3
                else:
                    self.hit()
                item["rect"].y = HEIGHT + 100
        self.obstacles = [o for o in self.obstacles if o["rect"].top < HEIGHT]

        for coin in self.coins:
            coin["rect"].y += current_speed
            if self.player.colliderect(coin["rect"]):
                self.coins_count += coin["value"]
                coin["rect"].y = HEIGHT + 100
        self.coins = [c for c in self.coins if c["rect"].top < HEIGHT]

        for power in self.powerups:
            power["rect"].y += current_speed
            if time.time() - power["born"] > 6:
                power["rect"].y = HEIGHT + 100
            if self.player.colliderect(power["rect"]):
                self.activate_powerup(power["kind"])
                power["rect"].y = HEIGHT + 100
        self.powerups = [p for p in self.powerups if p["rect"].top < HEIGHT]

        if self.distance >= FINISH_DISTANCE and not self.game_over:
            self.won = True
            self.game_over = True
            add_score(self.username, self.score + 500, self.distance)

    def draw_obstacle(self, item):
        rect = item["rect"]
        kind = item["kind"]
        if kind == "barrier":
            pygame.draw.rect(self.screen, RED, rect)
        elif kind == "oil":
            pygame.draw.ellipse(self.screen, BLACK, rect)
        elif kind == "pothole":
            pygame.draw.ellipse(self.screen, GRAY, rect)
        elif kind == "bump":
            pygame.draw.rect(self.screen, ORANGE, rect)
        elif kind == "nitro_strip":
            pygame.draw.rect(self.screen, BLUE, rect)

    def draw(self):
        self.screen.blit(self.road, (0, self.road_y))
        self.screen.blit(self.road, (0, self.road_y - HEIGHT))

        for coin in self.coins:
            pygame.draw.circle(self.screen, YELLOW, coin["rect"].center, 12)
            draw_text(self.screen, str(coin["value"]), self.font, BLACK, coin["rect"].centerx, coin["rect"].centery)

        for item in self.obstacles:
            self.draw_obstacle(item)

        for power in self.powerups:
            color = PURPLE
            if power["kind"] == "shield":
                color = GREEN
            elif power["kind"] == "repair":
                color = RED
            pygame.draw.circle(self.screen, color, power["rect"].center, 15)
            draw_text(self.screen, power["kind"][0].upper(), self.font, WHITE, power["rect"].centerx, power["rect"].centery)

        for rect in self.traffic:
            self.screen.blit(self.enemy_img, rect)

        self.screen.blit(self.player_img, self.player)
        if self.shield:
            pygame.draw.circle(self.screen, GREEN, self.player.center, 55, 3)

        remaining = max(0, FINISH_DISTANCE - int(self.distance))
        draw_text(self.screen, f"Score: {self.score}", self.font, WHITE, 10, 10, center=False)
        draw_text(self.screen, f"Coins: {self.coins_count}", self.font, WHITE, 10, 35, center=False)
        draw_text(self.screen, f"Distance: {int(self.distance)}", self.font, WHITE, 10, 60, center=False)
        draw_text(self.screen, f"Left: {remaining}", self.font, WHITE, 10, 85, center=False)

        if self.active_power == "nitro":
            left = max(0, int(self.power_end - time.time()))
            draw_text(self.screen, f"Power: Nitro {left}s", self.font, WHITE, 210, 10, center=False)
        elif self.active_power == "shield":
            draw_text(self.screen, "Power: Shield", self.font, WHITE, 210, 10, center=False)
        else:
            draw_text(self.screen, "Power: none", self.font, WHITE, 210, 10, center=False)

    def run(self):
        while not self.game_over:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "menu"

            self.update()
            self.draw()
            pygame.display.update()

        return "over"
