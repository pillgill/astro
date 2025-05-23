import pygame
import sys
from constants import *
from player import *
from asteroid import *
from AsteroidField import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    
    

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)

    AsteroidField.containers = (updatable)
    Asteroid_Field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("game over")
                sys.exit()
            for shot in shots:

                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = (clock.tick(60)/1000)

     

    

if __name__ == "__main__":
    main()
