# sudoku_solver/ui.py
def display_board(board):
    """Displays the Sudoku board."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()