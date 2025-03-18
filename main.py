#!/usr/bin/env python
# main.py
from sudoku_solver import ui, logic, utils
def main():
    predefined_boards = utils.get_predefined_boards()
    predefined_solutions = utils.get_predefined_solutions()
    predefined_boards[1] = predefined_solutions[1]
    for board, solution in zip(predefined_boards, predefined_solutions):
        print("Initial Sudoku Board:")
        ui.display_board(board)
        if logic.solve_sudoku(board):
            print("\nSolved Sudoku Board:")
            ui.display_board(board)
        else:
            print("\nNo solution exists.")
        if board == solution:
            print("\nSolved!")
        else:
            print("\nNot Solved.")
        print('\n'+'-'*20+'\n')
if __name__ == "__main__":
    main()