import customtkinter as ctk
import random
from settings import *

shapes = [
    {
        "name": "1x1",
        "cells": [(0, 0)]
    },
    {
        "name": "2x1",
        "cells": [(0, 0), (1, 0)]
    },
    {
        "name": "2x2",
        "cells": [(0, 0), (1, 0), (0, 1), (1, 1)]
    },
    {
        "name": "3x1",
        "cells": [(-1, 0), (0, 0), (1, 0)]
    },
    {
        "name": "top left corner",
        "cells": [(0, 0), (0, 1), (1, 1)]
    },
    {
        "name": "top right corner",
        "cells": [(-1, 0), (0, 0), (0, -1)]
    },
    {
        "name": "t",
        "cells": [(-1, 0), (0, 0), (1, 0), (0, -1)]
    },
    {
        "name": "t inverted",
        "cells": [(-1, 0), (0, 0), (1, 0), (0, 1)]
    }
]

# colours for randomised generation of pieces
piece_colours = [
    "#FF6B6B", 
    "#4ECDC4",
    "#45B7D1",  
    "#96CEB4",  
    "#FFEAA7",  
    "#DDA0DD",
    "#98D8C8",
    "#F7DC6F",
    "#BB8FCE",
    "#85C1E9",
]

class CalmStack(ctk.CTk):
    def __init__ (self):
        super().__init__()

        # main window
        self.title("CalmStack")
        self.geometry(resolution)
        self.configure(fg_color=grid_bg)

        # score and piece index
        self.score = 0
        self.selected_piece_index = None

        self.board = [
            [None for _ in range(grid_width)]
            for _ in range(grid_height)
        ]

        # score label
        self.score_label = ctk.CTkLabel(self, text="Score: 0", font=("Lexend", 16, "bold"), text_color="white")
        self.score_label.pack(pady=10)

        # game board
        self.board_canvas = ctk.CTkCanvas(self, width=grid_width * cell_size, height=grid_height * cell_size, highlightthickness=0)
        self.board_canvas.configure(bg=grid_bg)
        self.board_canvas.pack(pady=10)

        self.board_canvas.bind("<Button-1>", self.on_board_click)

        # piece frame
        self.pieces_frame = ctk.CTkFrame(self, fg_color=grid_bg)
        self.pieces_frame.pack(pady=10)

        # status label
        self.status_label = ctk.CTkLabel(self, text="Select a piece and place it on the board", text_color="white", font=("Lexend", 11))
        self.status_label.pack(pady=10)

        # restart button
        self.restart_button = ctk.CTkButton(
            self, 
            text="Restart", 
            command=self.restart_game, 
            fg_color="lightblue", 
            text_color="white", 
            font=("Lexend", 11, "bold")
        )
        self.restart_button.pack(pady=10, ipadx=12, ipady=5)

        self.draw_board()
        self.generate_pieces()
        self.refresh_piece_buttons()

    def draw_board(self):
        self.board_canvas.delete("all")

        for y in range(grid_height):
            for x in range(grid_width):
                x1 = x * cell_size
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                colour = self.board[y][x]
                if colour is None:
                    colour = empty_colour

                self.board_canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=colour,
                    outline=outline_colour,
                    width=2
                )
    def generate_pieces(self): 
        self.available_pieces = []
        for _ in range(3):
            random.choice(shapes)
            piece = random.choice(shapes).copy()
            piece["colour"] = random.choice(piece_colours)
            self.available_pieces.append(piece)

        self.selected_piece_index = None

    def refresh_piece_buttons(self):
        for widget in self.pieces_frame.winfo_children():
            widget.destroy()

        for i, piece in enumerate(self.available_pieces):
            canvas = ctk.CTkCanvas(
                self.pieces_frame,
                width=120,
                height=100,
                bg="darkblue",
                highlightthickness=2,
            )
            canvas.configure(bg="darkblue")

            canvas.grid(
                row=0,
                column=i,
                padx=10
            )

            self.draw_piece_preview(
                canvas,
                piece
            )

            canvas.bind(
                "<Button-1>",
                lambda event, idx=i:
                self.select_piece(idx)
            )
            
            label = ctk.CTkLabel(
                self.pieces_frame,
                text=piece["name"],
                text_color="white",
                fg_color="transparent"
            )

            label.grid(
                row=1,
                column=i
            )

    def draw_piece_preview(self, canvas, piece):
        preview_size = 22

        min_x = min(c[0] for c in piece["cells"])
        max_x = max(c[0] for c in piece["cells"])

        min_y = min(c[1] for c in piece["cells"])
        max_y = max(c[1] for c in piece["cells"])

        shape_w = max_x - min_x + 1
        shape_h = max_y - min_y + 1

        offset_x = (120 - shape_w * preview_size) // 2
        offset_y = (100 - shape_h * preview_size) // 2

        for cx, cy in piece["cells"]:
            x1 = offset_x + (cx - min_x) * preview_size
            y1 = offset_y + (cy - min_y) * preview_size

            x2 = x1 + preview_size
            y2 = y1 + preview_size

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=piece["colour"],
                outline="white"
            )

    def select_piece(self, index):
        self.selected_piece_index = index
        piece = self.available_pieces[index]
        self.status_label.config(text=f"Selected: {piece['name']}")

    def can_place_piece(self, piece, gx, gy):
        for dx, dy in piece["cells"]:
            x = gx + dx
            y = gy + dy

            if x<0 or x>= grid_width:
                return False
            
            if y<0 or y>= grid_height:
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
        self.score_label.configure(text=f"Score: {self.score}")
        self.draw_board()
    
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
                self.board[y][x] = None
                cleared += 1

        for x in full_cols:
            for y in range(grid_height):
                self.board[y][x] = None
                cleared += 1

        if cleared:
            self.score += cleared * 2
    
    def on_board_click(self, event):
        if self.selected_piece_index is None:
            self.status_label.config(text="Select a piece first.")
            return
        
        gx = event.x // cell_size
        gy = event.y // cell_size

        piece = self.available_pieces[self.selected_piece_index]

        if self.can_place_piece(piece, gx, gy):
            self.place_piece(
                piece,
                gx,
                gy
            )

            self.available_pieces.pop(self.selected_piece_index)
            self.selected_piece_index = None

            if len(self.available_pieces) == 0:
                self.generate_pieces()

            self.refresh_piece_buttons()

            if self.has_no_moves():
                self.status_label.config(text="Game Over!")
            else:
                self.status_label.config(text="Piece placed!")

        else:
            self.status_label.config(text="Cannot place piece there.")

    def has_no_moves(self):
        for piece in self.available_pieces:
            for y in range(grid_height):
                    for x in range(grid_width):
                        if self.can_place_piece(
                            piece,
                            x,
                            y
                        ):
                            return False

        return True

    def restart_game(self):
        self.score = 0
        self.board = [
            [None for _ in range(grid_width)]
            for _ in range(grid_height)
        ]

        self.score_label.config(text="Score: 0")
        self.status_label.config(text="Select a piece then click on the board.")

        self.generate_pieces()
        self.refresh_piece_buttons()
        self.draw_board()
    
if __name__ == "__main__":
    game = CalmStack()
    game.mainloop()