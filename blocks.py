import pygame

class Block:
    def __init__(self, colour, shape_coords):
        self.colour = colour
        self.shape_coords = shape_coords # holds layout coordinates
        
        # starting positions below the grid
        self.x = 210 
        self.y = 520
        
        # tracking drag state
        self.is_dragging = False
        self.drag_offset_x = 0 
        self.drag_offset_y = 0

    def draw(self):
        pass