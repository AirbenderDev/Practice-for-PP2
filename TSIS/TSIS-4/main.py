import pygame
import sys
from game import SnakeGame, Button, load_settings, save_settings, BLACK, WHITE, LIGHT, RED, BLUE
import db
from config import WIDTH, HEIGHT, FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 4 Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
big = pygame.font.SysFont("Arial", 42)

DB_OK = db.init_db()
username = "player"
settings = load_settings()


def draw_text(text, x, y, size="normal", color=BLACK):
    f = big if size == "big" else font
    screen.blit(f.render(text, True, color), (x, y))


def username_input():
    global username
    name = ""
    while True:
        screen.fill(WHITE)
        draw_text("Enter username", 160, 170, "big")
        pygame.draw.rect(screen, LIGHT, (150, 250, 300, 50))
        pygame.draw.rect(screen, BLACK, (150, 250, 300, 50), 2)
        draw_text(name, 160, 260)
        draw_text("Press ENTER to continue", 155, 330)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    username = name.strip()[:50]
                    return
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 15 and event.unicode.isprintable():
                    name += event.unicode


def main_menu():
    play = Button("Play", 200, 190, 200, 45)
    lb = Button("Leaderboard", 200, 250, 200, 45)
    st = Button("Settings", 200, 310, 200, 45)
    qt = Button("Quit", 200, 370, 200, 45)
    while True:
        screen.fill(WHITE)
        draw_text("Snake Game", 180, 80, "big")
        draw_text("Username: " + username, 190, 140)
        if not DB_OK:
            draw_text("DB not connected. Check config.py", 135, 500, color=RED)
        for b in [play, lb, st, qt]:
            b.draw(screen, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.clicked(event.pos):
                    return "play"
                if lb.clicked(event.pos):
                    return "leaderboard"
                if st.clicked(event.pos):
                    return "settings"
                if qt.clicked(event.pos):
                    pygame.quit(); sys.exit()


def leaderboard_screen():
    back = Button("Back", 220, 525, 160, 45)
    rows = db.get_top10()
    while True:
        screen.fill(WHITE)
        draw_text("Top 10", 230, 40, "big")
        draw_text("Rank   Name        Score   Level   Date", 50, 120)
        y = 160
        if not rows:
            draw_text("No scores or database is not connected", 100, 240)
        for i, row in enumerate(rows, 1):
            name, score, level, date = row
            draw_text(f"{i:<5} {name[:10]:<10} {score:<7} {level:<7} {date}", 50, y)
            y += 32
        back.draw(screen, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back.clicked(event.pos):
                return


def settings_screen():
    global settings
    colors = [[0, 200, 0], [0, 120, 255], [220, 0, 0], [180, 0, 220]]
    color_index = 0
    if settings.get("snake_color") in colors:
        color_index = colors.index(settings.get("snake_color"))
    grid_btn = Button("Toggle Grid", 180, 180, 240, 45)
    sound_btn = Button("Toggle Sound", 180, 240, 240, 45)
    color_btn = Button("Change Color", 180, 300, 240, 45)
    save_btn = Button("Save & Back", 180, 390, 240, 45)
    while True:
        screen.fill(WHITE)
        draw_text("Settings", 220, 80, "big")
        draw_text("Grid: " + str(settings.get("grid", True)), 190, 145)
        draw_text("Sound: " + str(settings.get("sound", False)), 190, 205)
        draw_text("Color:", 190, 365)
        pygame.draw.rect(screen, tuple(colors[color_index]), (280, 360, 40, 30))
        for b in [grid_btn, sound_btn, color_btn, save_btn]:
            b.draw(screen, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_btn.clicked(event.pos):
                    settings["grid"] = not settings.get("grid", True)
                if sound_btn.clicked(event.pos):
                    settings["sound"] = not settings.get("sound", False)
                if color_btn.clicked(event.pos):
                    color_index = (color_index + 1) % len(colors)
                    settings["snake_color"] = colors[color_index]
                if save_btn.clicked(event.pos):
                    save_settings(settings)
                    return


def game_over_screen(game):
    retry = Button("Retry", 170, 370, 120, 45)
    menu = Button("Main Menu", 310, 370, 140, 45)
    while True:
        screen.fill(WHITE)
        draw_text("Game Over", 190, 100, "big")
        draw_text(f"Score: {game.score}", 220, 190)
        draw_text(f"Level: {game.level}", 220, 225)
        draw_text(f"Personal best: {max(game.best, game.score)}", 220, 260)
        retry.draw(screen, font)
        menu.draw(screen, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry.clicked(event.pos):
                    return "retry"
                if menu.clicked(event.pos):
                    return "menu"


def play_game():
    best = db.get_personal_best(username)
    game = SnakeGame(screen, username, best, db)
    while True:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            game.handle_event(event)
        game.update(dt)
        game.draw()
        pygame.display.flip()
        if game.game_over:
            game.save_result()
            action = game_over_screen(game)
            if action == "retry":
                best = db.get_personal_best(username)
                game = SnakeGame(screen, username, best, db)
            else:
                return


def main():
    username_input()
    while True:
        action = main_menu()
        if action == "play":
            play_game()
        elif action == "leaderboard":
            leaderboard_screen()
        elif action == "settings":
            settings_screen()


if __name__ == "__main__":
    main()
