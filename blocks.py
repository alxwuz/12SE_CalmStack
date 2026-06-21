import pygame
import random
from settings import *

class Blocks:
    def __init__(self):
        self.orientation = random.randint(1, 4) # 1: normal, 2: 90 deg. 3: 180 degree: 4: 270 degree
        self.generation = 3
        self.size = block_size
        self.colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

        self.x1 = 210
        self.x2 = 260
        self.x3 = 310
        self.y = 520

        self.current_block = None

    def onebyone(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size, self.size))

    def onebythree(self, screen):
        if self.orientation == 1 or 3:
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 3))
        else:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))

    def onebyfive(self, screen):
        if self.orientation == 1 or 3:
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 5))
        else:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 5, self.size))

    def twobytwo(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 2, self.size * 2))

    def threebythree(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size * 3))

    def lblock(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x1 + self.size, self.y + self.size, self.size * 2, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size, self.size * 2))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x1 + self.size, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size * 2, self.size))
        else:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size, self.size, self.size * 2))

    def shortT(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size, self.size, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size, self.size * 3))
            pygame.draw.rect(screen, self.colour, (self.x1 + self.size, self.y + self.size, self.size, self.size))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 3))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size, self.size))

    def longT(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 5, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size, self.size, self.size * 2))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 3))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size * 2, self.size * 5, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 2))
        else:
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size * 3))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size * 3, self.size))

    def corner(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size, self.size, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 2, self.size))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size, self.size))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 2, self.size))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.colour, (self.x2, self.y, self.size, self.size))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size * 2, self.size))

    def longcorner(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size, self.size * 4))
            pygame.draw.rect(screen, self.colour, (self.x2, self.y + self.size * 3, self.size * 2, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x3, self.y + self.size, self.size, self.size * 3))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x1, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size, self.size, self.size * 3))
        else:
            pygame.draw.rect(screen, self.colour, (self.x3, self.y, self.size, self.size * 3))
            pygame.draw.rect(screen, self.colour, (self.x1, self.y + self.size * 3, self.size * 3, self.size))

    def makeBlocks(self):
        block_types = [
            self.onebyone,
            self.onebythree,
            self.onebyfive,
            self.twobytwo,
            self.threebythree,
            self.lblock,
            self.shortT,
            self.longT,
            self.corner,
            self.longcorner,
        ]
        self.current_block = random.choice(block_types)
        return self.current_block