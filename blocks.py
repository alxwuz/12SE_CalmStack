import pygame

class Block:
    def __init__(self, colour, shape_coords):
        self.colour = colour
        self.shape_coords = shape_coords
        # standard spawn layout coordinates below the grid
        self.x = 210
        self.y = 520

    def draw(self, surface):
        cell_size = 40
        # draws each component square relative to the block anchor position
        for rel_x, rel_y in self.shape_coords:
            rect = pygame.Rect(
                self.x + rel_x * cell_size,
                self.y + rel_y * cell_size,
                cell_size,
                cell_size
            )
            pygame.draw.rect(surface, self.colour, rect)