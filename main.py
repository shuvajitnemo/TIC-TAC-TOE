PLAYER1 = "X"
PLAYER2 = "O"

board = [" "] * 9
current_player = PLAYER1
game_over = False

WINNING_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

def check_winner():
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None

def get_current_player():
    return current_player

def make_move(position):
    global current_player, game_over

    if game_over or not isinstance(position, int) or not 0 <= position < 9:
        return None, None
    if board[position] != " ":
        return None, None

    played_mark = current_player
    board[position] = played_mark
    result = check_winner()

    if result is not None:
        game_over = True
    else:
        current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

    return played_mark, result

def reset_game():
    global current_player, game_over
    board[:] = [" "] * 9
    current_player = PLAYER1
    game_over = False  

def print_board():
 

    print("Current board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

if __name__ == "__main__":
    import app

    app.run_app()
