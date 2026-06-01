# main.py
import pygame
from settings import *
from game_manager import *
from game_grid import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("CalmStack")
    
    # setup fonts
    font_title = pygame.font.SysFont(None, 64)
    font_button = pygame.font.SysFont(None, 48)
    
    game = GameManager()
    grid = GameGrid()
    
    # set the game state
    app_state = "MENU"
    
    # create play button
    play_button = pygame.Rect(150, 300, 200, 80)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if app_state == "MENU":
                    # check for mouse click in play button
                    if play_button.collidepoint(event.pos):
                        app_state = "PLAYING" # change state to playing (previously from menu)
                        game.startGame()

        screen.fill(bg_colour)
        
        if app_state == "MENU":
            # make title
            title_text = font_title.render("CalmStack", True, text_colour)
            screen.blit(title_text, (140, 150))
            
            # draw shape of button
            pygame.draw.rect(screen, button_colour, play_button, border_radius=10)
            
            # create text
            btn_text = font_button.render("PLAY", True, text_colour)
            screen.blit(btn_text, (205, 325))
            
        elif app_state == "PLAYING":
            # temporary placeholder
            play_text = font_title.render("Game is Running!", True, text_colour)
            screen.blit(play_text, (65, 300))
            # soon to add drawGrid and make it into classes

        # updates display
        pygame.display.flip()

    pygame.quit()
        
if __name__ == "__main__":
    main()