import pygame

class GameGrid:
    def __init__(self):
        self.gridMatrix = [[0 for _ in range(8)] for _ in range(8)] # creates the grind in a 8x8 layout (0 means empty)
        self.cellSize = 40
        self.offsetX = 90 # centres the grid
        self.offsetY = 150
        print("grid has been created.") # terminal confirmation

    def drawGrid(self, surface):
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(
                    self.offsetX + col * self.cellSize, 
                    self.offsetY + row * self.cellSize, 
                    self.cellSize,
                    self.cellSize
                )
                # draws an outline box for every individual cell
                pygame.draw.rect(surface, (200, 200, 200), rect, 1) 

    def clearLines(self):
        pass

    def isValidMove(self):
        pass