import customtkinter as ctk
from settings import *

class GameUI:
    def __init__(self):
        # main window
        self.root = ctk.CTk()
        self.root.title("CalmStack")
        self.root.geometry(resolution)
        self.root.configure(fg_color=grid_bg)
        
        self.create_ui()
    
    def create_ui(self): # creates all the ui elements in the game
        # score display
        self.score_label = ctk.CTkLabel(
            self.root, 
            text="Score: 0", 
            font=("Lexend", 16, "bold"), 
            text_color="white"
        )
        self.score_label.pack(pady=10)

        # high score display
        self.high_score_label = ctk.CTkLabel(
            self.root,
            text="High score: 0",
            font=("Lexend", 16, "bold"),
            text_color="gold"
        )
        self.high_score_label.pack(pady=10)
        
        # game board canvas
        self.board_canvas = ctk.CTkCanvas(
            self.root, 
            width=grid_width * cell_size, 
            height=grid_height * cell_size, 
            highlightthickness=0
        )
        self.board_canvas.configure(bg=grid_bg)
        self.board_canvas.pack(pady=10)
        
        # piece selection frame
        self.pieces_frame = ctk.CTkFrame(self.root, fg_color=grid_bg)
        self.pieces_frame.pack(pady=10)
        
        # status message
        self.status_label = ctk.CTkLabel(
            self.root, 
            text="Select a piece and place it on the board", 
            text_color="white", 
            font=("Lexend", 11)
        )
        self.status_label.pack(pady=10)
        
        # restart button
        self.restart_button = ctk.CTkButton(
            self.root, 
            text="Restart", 
            fg_color="lightblue", 
            text_color="white", 
            font=("Lexend", 11, "bold")
        )
        self.restart_button.pack(pady=10, ipadx=12, ipady=5)
    
    def draw_board(self, board):
        for y in range(grid_height):
            for x in range(grid_width):
                x1 = x * cell_size # convert grid to pixels
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                
                colour = board[y][x]
                if colour is None:
                    colour = empty_colour
                
                self.board_canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=colour,
                    outline=outline_colour,
                    width=2
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
    
    def refresh_piece_buttons(self, available_pieces, select_callback):
        for widget in self.pieces_frame.winfo_children():
            widget.destroy()

        for i, piece in enumerate(available_pieces):
            canvas = ctk.CTkCanvas(
                self.pieces_frame,
                width=120,
                height=100,
                bg="darkblue",
                highlightthickness=2,
            )
            canvas.grid(row=0, column=i, padx=10)

            self.draw_piece_preview(canvas, piece)

            canvas.bind(
                "<Button-1>",
                lambda event, idx=i: select_callback(idx)
                )
            
            label = ctk.CTkLabel(
                self.pieces_frame,
                text=piece["name"],
                text_color="white",
                fg_color="transparent"
            )

            label.grid(row=1, column=i)

    def update_high_score(self, score):
        self.high_score_label.configure(text=f"High score: {score}")
    
    def update_score(self, score):
        self.score_label.configure(text=f"Score: {score}")
    
    def update_status(self, text):
        self.status_label.configure(text=text)
    
    def bind_board_click(self, callback):
        self.board_canvas.bind("<Button-1>", callback)
    
    def bind_restart(self, callback):
        self.restart_button.configure(command=callback)
    
    def run(self):
        self.root.mainloop()