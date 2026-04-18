import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

player = MusicPlayer("music")

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    title = font.render("Simple Music Player", True, (0, 0, 0))
    track_text = small_font.render(
        f"Current track: {player.get_current_track()}", True, (0, 0, 0))
    controls1 = small_font.render(
        "P = Play   S = Stop   N = Next", True, (0, 0, 255))
    controls2 = small_font.render("B = Back   Q = Quit", True, (0, 0, 255))

    screen.blit(title, (220, 40))
    screen.blit(track_text, (180, 110))
    screen.blit(controls1, (170, 170))
    screen.blit(controls2, (250, 210))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
