import customtkinter as ctk
from settings import *
from auth import register_user, verify_user

class LoginUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("CalmStack Login")
        self.root.geometry(resolution)
        self.root.configure(fg_color=grid_bg)

        self.is_register_mode = False
        self.login_successful = False

        self.create_ui()

    def create_ui(self):
        self.title_label = ctk.CTkLabel(
            self.root, text="Login", font=("Lexend", 22, "bold"), text_color="white"
        )
        self.title_label.pack(pady=(120, 30))

        self.username_entry = ctk.CTkEntry(
            self.root, placeholder_text="Username",
            fg_color=empty_colour, border_color=outline_colour,
            text_color="white", font=("Lexend", 12)
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self.root, placeholder_text="Password", show="*",
            fg_color=empty_colour, border_color=outline_colour,
            text_color="white", font=("Lexend", 12)
        )
        self.password_entry.pack(pady=10)
        self.password_entry.bind("<Return>", lambda e: self.handle_action())

        self.status_label = ctk.CTkLabel(
            self.root, text="", text_color="white", font=("Lexend", 11)
        )
        self.status_label.pack(pady=15)

        self.button = ctk.CTkButton(
            self.root, text="Sign In", fg_color="lightblue",
            text_color="white", font=("Lexend", 11, "bold"),
            command=self.handle_action
        )
        self.button.pack(pady=10, ipadx=12, ipady=5)

        self.toggle = ctk.CTkButton(
            self.root, text="Register instead", fg_color="transparent",
            text_color="white", font=("Lexend", 11),
            command=self.toggle_mode
        )
        self.toggle.pack(pady=10)

    def toggle_mode(self):
        self.is_register_mode = not self.is_register_mode
        self.title_label.configure(text="Register" if self.is_register_mode else "Login")
        self.button.configure(text="Register" if self.is_register_mode else "Sign In")
        self.toggle.configure(text="Login instead" if self.is_register_mode else "Register instead")

    def handle_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.is_register_mode:
            success, message = register_user(username, password)
        else:
            success, message = verify_user(username, password)

        self.status_label.configure(text=message)

        if success:
            self.login_successful = True
            self.root.update()
            self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.login_successful

if __name__ == "__main__":
    LoginUI().run()