# main.py
import pygame
from settings import *
from game_manager import *
from game_logic import *
from blocks import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("CalmStack")
    
    font_title = pygame.font.SysFont(None, 64)
    font_button = pygame.font.SysFont(None, 48)
    
    game = GameManager()
    logic = GameLogic()
    
    app_state = "MENU"
    
    play_button = pygame.Rect(150, 300, 200, 80)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            # route events based on the current game state
            if app_state == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks for mouse click inside the play button area
                    if play_button.collidepoint(event.pos):
                        app_state = "PLAYING" # changes state to playing
                        game.startGame()
                        logic.drawGrid(screen)

        screen.fill(bg_colour)
        
        if app_state == "MENU":
            title = font_title.render("CalmStack", True, text_colour)
            screen.blit(title, (140, 150))
            
            # creates text
            pygame.draw.rect(screen, (155, 0, 155), (170, 315, 150, 50))
            button_text = font_button.render("PLAY", True, text_colour)
            screen.blit(button_text, (200, 325))
            
        elif app_state == "PLAYING":
            # draws the background grid map and the active block
            logic.drawGrid(screen)

        # updates display
        pygame.display.flip()

    pygame.quit()
        
if __name__ == "__main__":
    main()