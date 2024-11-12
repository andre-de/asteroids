import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))





    while True:

        dt = clock.tick(60) / 1000

        #close the window when i click X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        
        for u in updatable:
            u.update()
        for d in drawable:
            d.draw()


        #player.update(dt)
        #player.draw(screen)
        
        pygame.display.flip()

        






#only run main when the file is run directly, not when it is imported as a module
if __name__ == "__main__":
    main()


