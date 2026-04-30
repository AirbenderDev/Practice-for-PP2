import pygame
from racer import Game, WIDTH, HEIGHT
from ui import Button, draw_text, ask_name, WHITE, BLACK, DARK, BLUE, RED, GREEN
from persistence import load_settings, save_settings, load_leaderboard

pygame.init()
try:
    pygame.mixer.init()
except Exception:
    pass

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS3 Racer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 36)
settings = load_settings()


def play_music():
    if not settings["sound"]:
        pygame.mixer.music.stop()
        return
    try:
        pygame.mixer.music.load("assets/background.wav")
        pygame.mixer.music.play(-1)
    except Exception:
        pass


def main_menu():
    buttons = [
        Button(100, 190, 200, 45, "Play"),
        Button(100, 250, 200, 45, "Leaderboard"),
        Button(100, 310, 200, 45, "Settings"),
        Button(100, 370, 200, 45, "Quit")
    ]
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if buttons[0].clicked(event):
                return "play"
            if buttons[1].clicked(event):
                return "leaderboard"
            if buttons[2].clicked(event):
                return "settings"
            if buttons[3].clicked(event):
                return "quit"

        screen.fill(DARK)
        draw_text(screen, "RACER GAME", big_font, WHITE, 200, 100)
        for button in buttons:
            button.draw(screen, font)
        pygame.display.update()


def settings_screen():
    global settings
    back = Button(100, 500, 200, 45, "Back")
    sound_btn = Button(80, 160, 240, 40, "")
    color_btn = Button(80, 230, 240, 40, "")
    diff_btn = Button(80, 300, 240, 40, "")
    colors = ["blue", "red", "green"]
    diffs = ["easy", "normal", "hard"]

    while True:
        clock.tick(60)
        sound_btn.text = "Sound: " + ("ON" if settings["sound"] else "OFF")
        color_btn.text = "Car color: " + settings["car_color"]
        diff_btn.text = "Difficulty: " + settings["difficulty"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if back.clicked(event):
                save_settings(settings)
                play_music()
                return "menu"
            if sound_btn.clicked(event):
                settings["sound"] = not settings["sound"]
                save_settings(settings)
                play_music()
            if color_btn.clicked(event):
                i = colors.index(settings["car_color"])
                settings["car_color"] = colors[(i + 1) % len(colors)]
                save_settings(settings)
            if diff_btn.clicked(event):
                i = diffs.index(settings["difficulty"])
                settings["difficulty"] = diffs[(i + 1) % len(diffs)]
                save_settings(settings)

        screen.fill(DARK)
        draw_text(screen, "SETTINGS", big_font, WHITE, 200, 80)
        sound_btn.draw(screen, font)
        color_btn.draw(screen, font)
        diff_btn.draw(screen, font)
        back.draw(screen, font)
        pygame.display.update()


def leaderboard_screen():
    back = Button(100, 520, 200, 45, "Back")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if back.clicked(event):
                return "menu"

        scores = load_leaderboard()
        screen.fill(DARK)
        draw_text(screen, "TOP 10", big_font, WHITE, 200, 50)
        draw_text(screen, "Rank  Name       Score   Dist",
                  font, WHITE, 40, 100, center=False)
        y = 140
        for i, item in enumerate(scores):
            text = f"{i + 1}.    {item['name'][:8]:8}  {item['score']:5}  {item['distance']:5}"
            draw_text(screen, text, font, WHITE, 40, y, center=False)
            y += 35
        back.draw(screen, font)
        pygame.display.update()


def game_over_screen(game):
    retry = Button(100, 390, 200, 45, "Retry")
    menu = Button(100, 450, 200, 45, "Main Menu")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if retry.clicked(event):
                return "retry"
            if menu.clicked(event):
                return "menu"

        screen.fill(DARK)
        title = "FINISH!" if game.won else "GAME OVER"
        draw_text(screen, title, big_font, WHITE, 200, 100)
        draw_text(screen, f"Score: {game.score}", font, WHITE, 200, 180)
        draw_text(
            screen, f"Distance: {int(game.distance)}", font, WHITE, 200, 220)
        draw_text(screen, f"Coins: {game.coins_count}", font, WHITE, 200, 260)
        retry.draw(screen, font)
        menu.draw(screen, font)
        pygame.display.update()


def main():
    play_music()
    state = "menu"
    last_game = None
    username = "Player"

    while True:
        if state == "menu":
            state = main_menu()
        elif state == "settings":
            state = settings_screen()
        elif state == "leaderboard":
            state = leaderboard_screen()
        elif state == "play":
            name = ask_name(screen, clock)
            if name is None:
                state = "quit"
            else:
                username = name
                game = Game(screen, clock, settings, username)
                result = game.run()
                last_game = game
                if result == "over":
                    state = "over"
                else:
                    state = result
        elif state == "retry":
            game = Game(screen, clock, settings, username)
            result = game.run()
            last_game = game
            state = "over" if result == "over" else result
        elif state == "over":
            state = game_over_screen(last_game)
        elif state == "quit":
            break

    pygame.quit()


if __name__ == "__main__":
    main()
