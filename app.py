import tkinter as tk

import main as game


BACKGROUND = "#0B1B25"
BOARD_COLOR = "#24343e"
CELL_COLOR = "#f4f1ea"
TEXT_COLOR = "#f4f1ea"
MUTED_COLOR = "#a8b7bd"
ACCENT_COLOR = "#e6b85c"
RESULT_COLOR = ACCENT_COLOR
PLAYER_COLORS = {game.PLAYER1: "#ff5c5c", game.PLAYER2: "#4aa3ff"}


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False, False)

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

        self.board_size = 390
        self.board_margin = 10
        self.cell_gap = 10
        self.cell_size = (
            self.board_size - 2 * self.board_margin - 2 * self.cell_gap
        ) / 3
        self.board = tk.Canvas(
            root,
            width=self.board_size,
            height=self.board_size,
            bg=BOARD_COLOR,
            highlightthickness=0,
        )
        self.board.pack(padx=24, pady=4)
        self.draw_cells()
        self.board.bind("<Button-1>", self.on_board_click)

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

    def draw_cells(self):
        for position in range(9):
            row, column = divmod(position, 3)
            left = self.board_margin + column * (self.cell_size + self.cell_gap)
            top = self.board_margin + row * (self.cell_size + self.cell_gap)
            self.board.create_rectangle(
                left,
                top,
                left + self.cell_size,
                top + self.cell_size,
                fill=CELL_COLOR,
                outline=CELL_COLOR,
            )

    def on_board_click(self, event):
        column = int((event.x - self.board_margin) // (self.cell_size + self.cell_gap))
        row = int((event.y - self.board_margin) // (self.cell_size + self.cell_gap))
        if not (0 <= row < 3 and 0 <= column < 3):
            return

        local_x = (event.x - self.board_margin) % (self.cell_size + self.cell_gap)
        local_y = (event.y - self.board_margin) % (self.cell_size + self.cell_gap)
        if local_x >= self.cell_size or local_y >= self.cell_size:
            return

        self.play(row * 3 + column)

    def play(self, position):
        mark, result = game.make_move(position)
        if mark is None:
            return

        row, column = divmod(position, 3)
        center_x = (
            self.board_margin
            + column * (self.cell_size + self.cell_gap)
            + self.cell_size / 2
        )
        center_y = (
            self.board_margin
            + row * (self.cell_size + self.cell_gap)
            + self.cell_size / 2
        )
        self.board.create_text(
            center_x,
            center_y,
            text=mark,
            font=("Segoe UI", 44, "bold"),
            fill=PLAYER_COLORS[mark],
        )

        if result == "draw":
            self.status.config(text="")
            self.show_result("Draw!", ACCENT_COLOR)
        elif result in (game.PLAYER1, game.PLAYER2):
            self.status.config(text="")
            self.show_result(f"{result} wins!", RESULT_COLOR)
        else:
            self.update_status()

    def show_result(self, message, accent):
        center = self.board_size / 2
        self.board.create_rectangle(
            0,
            center - 45,
            self.board_size,
            center + 45,
            fill=BACKGROUND,
            outline=BACKGROUND,
        )
        self.board.create_text(
            center,
            center,
            text=message,
            font=("Segoe UI", 40, "bold"),
            fill=accent,
        )

    def update_status(self):
        player = game.get_current_player()
        self.status.config(
            text=f"Player {player}'s turn",
            fg=PLAYER_COLORS[player],
            font=("Segoe UI", 12),
        )

    def reset(self):
        game.reset_game()
        self.board.delete("all")
        self.draw_cells()
        self.update_status()


def run_app():
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()