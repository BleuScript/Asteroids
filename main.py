import pygame # pyright: ignore[reportMissingImports]
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
import player
import asteroidfield
import asteroid


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = asteroidfield.AsteroidField()
    clock = pygame.time.Clock()
    c_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        updatable.update(dt)
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip() 
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
