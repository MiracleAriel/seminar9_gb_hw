def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"
