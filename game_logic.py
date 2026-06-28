import random
from abc import ABC, abstractmethod
from settings import *
from blocks import *


class Game(ABC): # abstract base class for similar games
    def __init__(self):
        self.score = 0
        self.selected_piece_index = None
        self.board = [[None for _ in range(grid_width)] for _ in range(grid_height)]
        self.available_pieces = []
    
    @abstractmethod
    def generate_pieces(self):
        pass
    
    @abstractmethod
    def clear_lines(self):
        pass

class CalmStack(Game):
    def __init__(self):
        super().__init__()
    
    def generate_pieces(self): # generates 3 random pieces
        self.available_pieces = []
        for _ in range(3):
            piece = random.choice(shapes).copy()
            piece["colour"] = random.choice(piece_colours)
            self.available_pieces.append(piece)
        self.selected_piece_index = None
    
    def select_piece(self, index):
        self.selected_piece_index = index
        piece = self.available_pieces[index]
        return piece["name"]
    
    def can_place_piece(self, piece, gx, gy): # placement chekcs
        for dx, dy in piece["cells"]:
            x = gx + dx # board poition = anchor + offset
            y = gy + dy
            
            if x < 0 or x >= grid_width:
                return False
            if y < 0 or y >= grid_height:
                return False
            if self.board[y][x] is not None:
                return False
        return True
    
    def place_piece(self, piece, gx, gy):
        for dx, dy in piece["cells"]:
            x = gx + dx
            y = gy + dy
            self.board[y][x] = piece["colour"]
        
        self.score += len(piece["cells"])
        self.clear_lines()
    
    def clear_lines(self):
        full_rows = []
        for y in range(grid_height):
            if all(self.board[y][x] is not None for x in range(grid_width)):
                full_rows.append(y)
        
        full_cols = []
        for x in range(grid_width):
            if all(self.board[y][x] is not None for y in range(grid_height)):
                full_cols.append(x)
        
        cleared = 0
        
        for y in full_rows:
            for x in range(grid_width):
                if self.board[y][x] is not None:
                    self.board[y][x] = None
                    cleared += 1
        
        for x in full_cols:
            for y in range(grid_height):
                if self.board[y][x] is not None:
                    self.board[y][x] = None
                    cleared += 1
        
        if cleared:
            self.score += cleared * 2
    
    def has_no_moves(self):
        if not self.available_pieces:
            return True
        
        for piece in self.available_pieces:
            for y in range(grid_height):
                for x in range(grid_width):
                    if self.can_place_piece(piece, x, y):
                        return False
        return True
    
    def restart_game(self):
        self.score = 0
        self.board = [[None for _ in range(grid_width)] for _ in range(grid_height)]
        self.available_pieces = []
        self.selected_piece_index = None