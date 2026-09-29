import tkinter as tk

import main as game


BACKGROUND = "#17232b"
BOARD_COLOR = "#24343e"
CELL_COLOR = "#f4f1ea"
TEXT_COLOR = "#f4f1ea"
MUTED_COLOR = "#a8b7bd"
ACCENT_COLOR = "#e6b85c"
PLAYER_COLORS = {game.PLAYER1: "#d85c45", game.PLAYER2: "#287a72"}


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False, False)
        self.result_overlay = None

        tk.Label(
            root,
            text="TIC-TAC-TOE",
            font=("Segoe UI", 23, "bold"),
            bg=BACKGROUND,
            fg=TEXT_COLOR,
        ).pack(pady=(24, 5))

        self.status = tk.Label(
            root,
            text="",
            font=("Segoe UI", 12),
            bg=BACKGROUND,
            fg=MUTED_COLOR,
        )
        self.status.pack(pady=(0, 17))

        self.board_frame = tk.Frame(root, bg=BOARD_COLOR, padx=5, pady=5)
        self.board_frame.pack(padx=24, pady=4)
        self.buttons = []
        for position in range(9):
            button = tk.Button(
                self.board_frame,
                text="",
                font=("Segoe UI", 30, "bold"),
                width=3,
                height=1,
                bg=CELL_COLOR,
                fg=TEXT_COLOR,
                activebackground="#e4dac8",
                relief="flat",
                bd=0,
                cursor="hand2",
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
            bg=ACCENT_COLOR,
            fg=BACKGROUND,
            activebackground="#f0ca77",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=9,
            cursor="hand2",
            command=self.reset,
        ).pack(pady=(18, 25))

        self.update_status()

    def play(self, position):
        mark, result = game.make_move(position)
        if mark is None:
            return

        button = self.buttons[position]
        button.config(text=mark, fg=PLAYER_COLORS[mark], state="disabled")

        if result == "draw":
            self.status.config(text="")
            self.disable_board()
            self.show_result("Draw!", ACCENT_COLOR)
        elif result in (game.PLAYER1, game.PLAYER2):
            self.status.config(text="")
            self.disable_board()
            self.show_result(f"{result} wins!", PLAYER_COLORS[result])
        else:
            self.update_status()

    def show_result(self, message, accent):
        if self.result_overlay is not None:
            self.result_overlay.destroy()

        overlay = tk.Label(
            self.board_frame,
            text=message,
            font=("Segoe UI", 48, "bold"),
            bg=BOARD_COLOR,
            fg=accent,
            padx=36,
            pady=24,
        )
        overlay.place(relx=0.5, rely=0.5, anchor="center")
        self.result_overlay = overlay
        self.root.after(2500, lambda: self.dismiss_result(overlay))

    def dismiss_result(self, overlay):
        if self.result_overlay is overlay:
            overlay.destroy()
            self.result_overlay = None

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
        if self.result_overlay is not None:
            self.result_overlay.destroy()
            self.result_overlay = None
        game.reset_game()
        for button in self.buttons:
            button.config(text="", state="normal", fg=TEXT_COLOR, bg=CELL_COLOR)
        self.update_status()


def run_app():
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()