import tkinter as tk

import main as game


BACKGROUND = "#f4f1ea"
BOARD_COLOR = "#ffffff"
TEXT_COLOR = "#202a35"
PLAYER_COLORS = {game.PLAYER1: "#d85c45", game.PLAYER2: "#287a72"}


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False, False)

        tk.Label(
            root,
            text="TIC-TAC-TOE",
            font=("Segoe UI", 22, "bold"),
            bg=BACKGROUND,
            fg=TEXT_COLOR,
        ).pack(pady=(22, 4))

        self.status = tk.Label(
            root,
            text="",
            font=("Segoe UI", 12),
            bg=BACKGROUND,
            fg=TEXT_COLOR,
        )
        self.status.pack(pady=(0, 14))

        board_frame = tk.Frame(root, bg=BACKGROUND)
        board_frame.pack(padx=24, pady=4)
        self.buttons = []
        for position in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Segoe UI", 30, "bold"),
                width=3,
                height=1,
                bg=BOARD_COLOR,
                fg=TEXT_COLOR,
                activebackground="#e7e4dc",
                relief="flat",
                bd=0,
                command=lambda index=position: self.play(index),
            )
            button.grid(
                row=position // 3,
                column=position % 3,
                padx=5,
                pady=5,
                ipadx=5,
                ipady=5,
            )
            self.buttons.append(button)

        tk.Button(
            root,
            text="New game",
            font=("Segoe UI", 11, "bold"),
            bg=TEXT_COLOR,
            fg="white",
            activebackground="#344454",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=9,
            command=self.reset,
        ).pack(pady=(17, 24))

        self.update_status()

    def play(self, position):
        mark, result = game.make_move(position)
        if mark is None:
            return

        button = self.buttons[position]
        button.config(text=mark, fg=PLAYER_COLORS[mark], state="disabled")

        if result == "draw":
            self.status.config(text="It's a draw!")
            self.disable_board()
        elif result in (game.PLAYER1, game.PLAYER2):
            self.status.config(text=f"Player {result} wins!")
            self.disable_board()
        else:
            self.update_status()

    def update_status(self):
        player = game.get_current_player()
        self.status.config(
            text=f"Player {player}'s turn",
            fg=PLAYER_COLORS[player],
        )

    def disable_board(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset(self):
        game.reset_game()
        for button in self.buttons:
            button.config(text="", state="normal", fg=TEXT_COLOR)
        self.update_status()


def run_app():
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()