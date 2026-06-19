import pygame
from settings import *

class GameLogic:
    def __init__(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0] for i in range(8)] # 0 means empty

    def drawGrid(self, screen):
        black = (0, 0 ,0)

        x_offset = (resolution_x - (block_size * 8)) / 2
        y_offset = (resolution_y - (block_size * 8)) / 5

        grid_total_size = 8 * block_size
        for i in range(9):
            position = i * block_size

            pygame.draw.line(screen, black, (position + x_offset, y_offset), (position + x_offset, grid_total_size + y_offset))
            pygame.draw.line(screen, black, (x_offset, position + y_offset), (grid_total_size + x_offset, position + y_offset))

    def clearLines(self):
        pass

    def isValidMove(self):
        pass