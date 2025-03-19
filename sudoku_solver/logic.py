# sudoku_solver/logic.py

from sudoku_solver.board import Board

def determine_region(r_idx, c_idx):
  return (r_idx // 3) * 3 + (c_idx // 3)


def solve_sudoku(board:Board):
  # return True to indicate a solution exists
  print('in solve_sudoku')
  return True


def is_slice_complete(slice:list):
  # return True if the given array slice is complete
  # that is, all values are > 0, < 10 and unique
  slice.sort()
  return slice == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_solved(board:Board):
  # return True if the board is solved
  print('in is_solved')
  for r in board.rows():
    if not is_slice_complete(r):
      return False
  for c in board.cols():
    if not is_slice_complete(c):
      return False
  for g in board.regions():
    if not is_slice_complete(g):
      return False
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
