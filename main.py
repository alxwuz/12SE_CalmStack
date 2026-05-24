import pygame

# set up window dimensions and colour
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
BG_COLOUR = (245, 245, 245)

def main():
    pygame.init()

    #create window and name
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("CalmStack")
    
    # keep program running
    running = True

    while running:
        for event in pygame.event.get():
            # check if window is closed, then quit
            if event.type == pygame.QUIT:
                pygame.quit()

        # fills bg colour
        screen.fill(BG_COLOUR)
        # updates display
        pygame.display.flip()
        
if __name__ == "__main__":
    main()