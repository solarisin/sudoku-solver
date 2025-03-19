#!/usr/bin/env python
# main.py
from sudoku_solver import logic, utils
from sudoku_solver.board import Board

def main():
    predefined_boards = utils.get_predefined_boards()
    predefined_solutions = utils.get_predefined_solutions()
    predefined_boards[1] = predefined_solutions[1]
    for board_rows, solution_rows in zip(predefined_boards, predefined_solutions):
        board = Board(board_rows)
        solution = Board(solution_rows)
        print("Initial Sudoku Board:")
        print(board)
        if logic.solve_sudoku(board):
            print("\nSolved Sudoku Board:")
            print(board)
        else:
            print("\nNo solution exists.")
        if board == solution:
            print("\nSolved!")
        else:
            print("\nNot Solved.")
        print('\n'+'-'*20+'\n')


if __name__ == "__main__":
    main()