#!/usr/bin/env python
# main.py
import click
from sudoku_solver import logic
from sudoku_solver.board import Board
from sudoku_solver.ui import SudokuGUI

@click.command()
@click.option('--board', default=None, help='Sudoku board to solve')
def main(board):
    if board:
        try:
            board_numbers = list(map(int, board))
            if len(board_numbers) != 81:
                raise ValueError
            board_rows = [board_numbers[i:i+9] for i in range(0, 81, 9)]
            board = Board(board_rows)
        except ValueError:
            raise click.BadParameter('Invalid board format. Ensure it is a string of 81 numbers.')
    else:
        raise click.BadParameter('Board is required.')

    gui = SudokuGUI(board)
    gui.run()

if __name__ == "__main__":
    main()
