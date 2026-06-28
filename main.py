from login_ui import *
from game_logic import *
from game_ui import *
from settings import *

class CalmStackGame:
    def __init__(self):
        self.game = CalmStack()
        self.ui = GameUI()
        
        # connects the ui to the methods
        self.ui.bind_board_click(self.on_board_click)
        self.ui.bind_restart(self.restart_game)     
        
        self.game.generate_pieces() # create first 3 pieces
        self.update_view() 
    
    def on_board_click(self, event):
        if self.game.selected_piece_index is None: # selection check
            self.ui.update_status("Select a piece first.")
            return
        
        gx = event.x // cell_size  # column number
        gy = event.y // cell_size  # row number
        
        piece = self.game.available_pieces[self.game.selected_piece_index]
        
        if self.game.can_place_piece(piece, gx, gy): # placement check
            self.game.place_piece(piece, gx, gy)
            
            self.game.available_pieces.pop(self.game.selected_piece_index) # removes the selected piece from available ones
            self.game.selected_piece_index = None
            
            if len(self.game.available_pieces) == 0:
                self.game.generate_pieces() # generates new blocks once no more pieces

            self.update_view()
            
            if self.game.has_no_moves():
                self.ui.update_status(f"Game Over! Press restart to play again. Your score was {self.game.score}")
            else:
                self.ui.update_status("Piece placed!")
        else:
            if self.game.has_no_moves():
                self.ui.update_status(f"Game Over! Press restart to play again. Your score was {self.game.score}")
            else:
                self.ui.update_status("Cannot place piece there.")
    
    def select_piece(self, index):
        name = self.game.select_piece(index)
        self.ui.update_status(f"Selected: {name}")
    
    def restart_game(self):
        self.game.restart_game() # resets score + board
        self.game.generate_pieces()
        self.ui.update_status("Select a piece then click on the board.")
        self.update_view() 
    
    def update_view(self):
        self.ui.draw_board(self.game.board)  
        self.ui.update_score(self.game.score)  
        self.ui.refresh_piece_buttons(
            self.game.available_pieces,  
            self.select_piece
        )
    
    def run(self):
        self.ui.run()

if __name__ == "__main__":
    login = LoginUI()
    if login.run():
        game = CalmStackGame()
        game.run()