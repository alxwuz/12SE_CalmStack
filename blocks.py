import pygame
import random
from settings import *

class Blocks:
    def __init__(self):
        self.size = block_size
        self.initial_x = 70
        self.initial_y = 532
        self.blocks_data = []

    def onebyone(self, screen, x, y, colour, orientation):
        pygame.draw.rect(screen, colour, (x, y, self.size, self.size))

    def onebythree(self, screen, x, y, colour, orientation):
            pygame.draw.rect(screen, colour, (x, y, self.size, self.size * 3))

    def onebyfive(self, screen, x, y, colour, orientation):
            pygame.draw.rect(screen, colour, (x, y, self.size, self.size * 5))

    def twobytwo(self, screen, x, y, colour, orientation):
        pygame.draw.rect(screen, colour, (x, y, self.size * 2, self.size * 2))

    def threebythree(self, screen, x, y, colour, orientation):
        pygame.draw.rect(screen, colour, (x, y, self.size * 3, self.size * 3))

    def lblock(self, screen, x, y, colour, orientation):
        if orientation == 1:
            pygame.draw.rect(screen, colour, (x, y, self.size, self.size * 2))
            pygame.draw.rect(screen, colour, (x, y + self.size * 2, self.size * 2, self.size))
        elif orientation == 2:
            pygame.draw.rect(screen, colour, (x, y, self.size * 3, self.size))
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size, self.size))
        elif orientation == 3:
            pygame.draw.rect(screen, colour, (x, y, self.size * 2, self.size))
            pygame.draw.rect(screen, colour, (x + self.size, y, self.size, self.size * 3))
        else:
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size * 3, self.size))
            pygame.draw.rect(screen, colour, (x + self.size * 2, y, self.size, self.size))

    def shortT(self, screen, x, y, colour, orientation):
        if orientation == 1:
            pygame.draw.rect(screen, colour, (x, y, self.size * 3, self.size))
            pygame.draw.rect(screen, colour, (x + self.size, y + self.size, self.size, self.size))
        elif orientation == 2:
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size, self.size))
            pygame.draw.rect(screen, colour, (x + self.size, y, self.size, self.size * 3))
        elif orientation == 3:
            pygame.draw.rect(screen, colour, (x + self.size, y, self.size, self.size))
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size * 3, self.size))
        else:
            pygame.draw.rect(screen, colour, (x, y, self.size, self.size * 3))
            pygame.draw.rect(screen, colour, (x + self.size, y + self.size, self.size, self.size))

    def corner(self, screen, x, y, colour, orientation):
        if orientation == 1:
            pygame.draw.rect(screen, colour, (x, y, self.size * 2, self.size))
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size, self.size))
        elif orientation == 2:
            pygame.draw.rect(screen, colour, (x, y, self.size * 2, self.size))
            pygame.draw.rect(screen, colour, (x + self.size, y + self.size, self.size, self.size))
        elif orientation == 3:
            pygame.draw.rect(screen, colour, (x + self.size, y, self.size, self.size * 2))
            pygame.draw.rect(screen, colour, (x, y + self.size, self.size, self.size))
        else:
            pygame.draw.rect(screen, colour, (x, y, self.size, self.size * 2))
            pygame.draw.rect(screen, colour, (x + self.size, y + self.size, self.size, self.size))

    def generateBlocks(self):
        block_types = [
            self.onebyone,
            self.onebythree,
            self.onebyfive,
            self.twobytwo,
            self.threebythree,
            self.lblock,
            self.shortT,
            self.corner,
        ]
        self.blocks_data = []
        for i in range(3): # generates 3 random pieces
            func = random.choice(block_types)
            colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            orient = random.randint(1, 4)
            x = self.initial_x + i * 175 # makes sure they are spaced apart
            y = self.initial_y
            self.blocks_data.append([func, orient, colour, x, y]) # saves in list

    def drawBlocks(self, screen):
        for func, orient, colour, x, y in self.blocks_data:
            func(screen, x, y, colour, orient) # runs the randomised data from the list

    def get_block_at(self, pos):
        mouse_x, mouse_y = pos
        for i, (func, orient, colour, x, y) in enumerate(self.blocks_data):
            rect = pygame.Rect(x, y, self.size * 3, self.size * 3) # hitbox not fully accurate though
            if rect.collidepoint(mouse_x, mouse_y):
                return i
        return None