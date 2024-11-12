import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #init and start clock
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    #init containers, add Player to both of them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #create Player and set their position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #init screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))





    while True:

        #tick the clock
        dt = clock.tick(60) / 1000

        #close the window when I click X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        
        #update all in updatable container, draw all in drawaböe container
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        
        #refresh screen
        pygame.display.flip()

        






#only run main when the file is run directly, not when it is imported as a module
if __name__ == "__main__":
    main()


