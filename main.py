import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import circleshape

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt =0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables,drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers =(updateables,)
    Shot.containers = (shots,updateables,drawables)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    asteroidfield = AsteroidField()


    print("Starting asteroids!")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for updateable in updateables:
            updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                exit()
        for shot in shots:
            shot.position += shot.velocity * dt
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()