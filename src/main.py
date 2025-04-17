#!/usr/bin/env python
# main.py
import click
from sudoku_solver import logic, utils
from sudoku_solver.board import Board

def validate_board(ctx, param, value):
    if value:
        try:
            board_rows = [list(map(int, row.split(','))) for row in value.split(';')]
            if len(board_rows) != 9 or any(len(row) != 9 for row in board_rows):
                raise ValueError
            return Board(board_rows)
        except ValueError:
            raise click.BadParameter('Invalid board format. Ensure it is a 9x9 grid with numbers separated by commas and rows separated by semicolons.')
    return None

@click.command()
@click.option('--board', default=None, callback=validate_board, help='Sudoku board to solve')
def main(board):
    if board:
        predefined_boards = [board.board]
    else:
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

        print("Is solved?", logic.is_solved(board))
        
        if board == solution:
            print("\nVerified Solved!")
        else:
            print("\nVerified Not Solved.")
        print('\n'+'-'*20+'\n')

if __name__ == "__main__":
    main()
