# inside blocks.py
import pygame
import random
from settings import *

class Blocks:
    def __init__(self):
        self.orientation = random.randint(1, 4)
        self.generation = 3 
        self.size = block_size

        # starting positions below the grid
        self.x1 = 210 
        self.x2 = 260
        self.x3 = 310
        self.y = 520

    def onebyone(self, screen):
        colour = (0, 0, 0)
        pygame.draw.rect(screen, colour, (self.x1, self.y, self.size, self.size))

    def onebythree(self, screen):
        colour = (140, 0, 240)
        pygame.draw.rect(screen, colour, (self.x2, self.y, self.size, self.size * 3))
        pass

    def onebyfive(self, screen):
        colour = (41, 2, 122)
        pygame.draw.rect(screen, colour, (self.x2, self.y, self.size * 5, self.size))
        pass

    def twobytwo(self):
        pass

    def threebythree(self):
        pass

    def lblock(self):
        pass

    def shortT(self):
        pass

    def longT(self):
        pass

    def corner(self):
        pass

    def longcorner(self):
        pass

    def makeBlocks(self):
        
        pass