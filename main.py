import pygame # type: ignore
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
import player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    c_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}") # type: ignore
    print(f"Screen height: {constants.SCREEN_HEIGHT}") # type: ignore

    


if __name__ == "__main__":
    main()
