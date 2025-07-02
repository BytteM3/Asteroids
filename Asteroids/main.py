import pygame
from constants import *
from player import *

pygame.init()
clock = pygame.time.Clock()
dt = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill("black")
    player.update(dt)
    player.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
