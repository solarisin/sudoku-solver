# sudoku_solver/logic.py

from board import Board

def determine_region(r_idx, c_idx):
  return (r_idx // 3) * 3 + (c_idx // 3)


def solve_sudoku(board:Board):
  # return True to indicate a solution exists
  print('in solve_sudoku')
  for x, r in enumerate(board.rows()):
     for y, c in enumerate(r):
       print(f"[{x},{y},{determine_region(x,y)}] ", end='')
     print()
  return True


def is_valid(board:Board, row, col, num):
  """Checks if a number is valid in a given cell."""
  # Basic stub
  print('in is_valid')
  return True


def find_empty(board:Board) -> tuple|None:
  """Finds an empty cell in the board."""
  for x, r in enumerate(board.rows()):
     for y, c in enumerate(r):
       if c == 0:
         return x, y
  return None
