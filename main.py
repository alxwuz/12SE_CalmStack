# main.py
import pygame
from settings import *
from game_manager import *
from game_logic import *
from blocks import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((resolution_x, resolution_y))
    pygame.display.set_caption("CalmStack")
    
    font_title = pygame.font.SysFont(None, 64)
    font_button = pygame.font.SysFont(None, 48)
    
    game = GameManager()
    logic = GameLogic()
    blocks = Blocks()
    
    app_state = "MENU"
    play_button = pygame.Rect(150, 300, 200, 80)
    dragging = False
    dragged_index = None
    drag_offset_x = 0
    drag_offset_y = 0

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

        screen.fill(bg_colour)
        
        if app_state == "MENU":
            title = font_title.render("CalmStack", True, text_colour)
            screen.blit(title, (140, 150))
            
            # creates text
            pygame.draw.rect(screen, (155, 0, 155), (170, 315, 150, 50))
            button_text = font_button.render("PLAY", True, text_colour)
            screen.blit(button_text, (200, 325))
            
        elif app_state == "PLAYING":
            # draws the background grid map and the blocks
            logic.drawGrid(screen)
            blocks.drawBlocks(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                idx = blocks.get_block_at(event.pos)
                if idx is not None:
                    dragging = True
                    dragged_index = idx
                    func, orient, colour, x, y = blocks.blocks_data[idx]
                    drag_offset_x = event.pos[0] - x # makes sure doesn't snap to top left corner
                    drag_offset_y = event.pos[1] - y

                    block = blocks.blocks_data.pop(idx)
                    blocks.blocks_data.append(block) 
                    dragged_index = len(blocks.blocks_data) - 1

            elif event.type == pygame.MOUSEMOTION:
                if dragging and dragged_index is not None:
                    if not pygame.mouse.get_pressed()[0]: # if mouse not pressed, stop dragging
                        dragging = False
                        dragged_index = None
                    else:
                        new_x = event.pos[0] - drag_offset_x # update coords of block based on where mouse goes
                        new_y = event.pos[1] - drag_offset_y
                        blocks.blocks_data[dragged_index][3] = new_x
                        blocks.blocks_data[dragged_index][4] = new_y

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if dragging:
                    dragging = False
                    dragged_index = None
        
        # updates display
        pygame.display.flip()

    pygame.quit()
        
if __name__ == "__main__":
    main()