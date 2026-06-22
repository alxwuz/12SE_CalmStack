import pygame
import random
from settings import *

class Blocks:
    def __init__(self):
        self.orientation = random.randint(1, 4) # 1: normal, 2: 90 deg. 3: 180 degree: 4: 270 degree
        self.generation = 3
        self.size = block_size
        self.colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

        self.x = 70
        self.y = 532

        self.current_block1 = None
        self.current_block2 = None
        self.current_block3 = None

        self.generateBlocks()

    def onebyone(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size))

    def onebythree(self, screen):
        if self.orientation == 1 or self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size * 3))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 3, self.size))

    def onebyfive(self, screen):
        if self.orientation == 1 or self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size * 5))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 5, self.size))

    def twobytwo(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 2, self.size * 2))

    def threebythree(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 3, self.size * 3))

    def lblock(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size * 2, self.size * 2, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size, self.size))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 2, self.size))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y, self.size, self.size * 3))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x + self.size * 2, self.y, self.size, self.size))

    def shortT(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 3, self.size))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y + self.size, self.size, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size, self.size))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y, self.size, self.size * 3))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y, self.size, self.size))
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size * 3, self.size))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size * 3))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y + self.size, self.size, self.size))

    def corner(self, screen):
        if self.orientation == 1:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 2, self.size))
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size, self.size))
        elif self.orientation == 2:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size * 2, self.size))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y + self.size, self.size, self.size))
        elif self.orientation == 3:
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x, self.y + self.size, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size * 2))
            pygame.draw.rect(screen, self.colour, (self.x + self.size, self.y + self.size, self.size, self.size))

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
        self.current_block1 = random.choice(block_types)
        self.current_block2 = random.choice(block_types)
        self.current_block3 = random.choice(block_types)

    def drawBlocks(self, screen):
        self.current_block1(screen) 

        # shift it by 100
        original_x = self.x
        self.x += 100
        self.current_block2(screen)

        # shift by 200
        self.x = original_x + 200
        self.current_block3(screen)

        # convert to ogirinal value
        self.x = original_x
