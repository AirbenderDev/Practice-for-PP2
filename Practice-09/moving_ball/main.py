import pygame
from ball import Ball


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    ball = Ball(x=WIDTH // 2, y=HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.move_left(WIDTH)
                elif event.key == pygame.K_RIGHT:
                    ball.move_right(WIDTH)
                elif event.key == pygame.K_UP:
                    ball.move_up(HEIGHT)
                elif event.key == pygame.K_DOWN:
                    ball.move_down(HEIGHT)

        screen.fill(WHITE)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
