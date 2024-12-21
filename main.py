import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ## Initialization ##
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Setup asteroid groups and asteroids:
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #Setup handling the shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Setup player groups and player:
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    ## Game Loop ##
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if asteroid.hasCollided(player):
                print("Game over!")
                exit()

            for shot in shots:
                if asteroid.hasCollided(shot):
                    asteroid.split()
                    shot.kill()
                    break

        #Last:
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


