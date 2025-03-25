# sudoku_solver/logic.py

from sudoku_solver.board import Board, House, DimIdx

def print_cell_info(board:Board, x:DimIdx, y:DimIdx):
  r = x+1
  c = y+1
  print(f"Cell r{r}c{c} = {board.board[x,y]}")
  print(f"Houses of r{r}c{c}:")
  print(f"  {board.row_of(x)}")
  print(f"  {board.col_of(y)}")
  print(f"  {board.region_of(x,y)}")


def solve_sudoku(board:Board):
  # return True to indicate a solution exists
  print('in solve_sudoku')
  x,y = find_empty(board)
  if x is not None and y is not None:
    print(f"first empty cell idx: {x}, {y}")
    print_cell_info(board, x, y)
  return True


def is_solved(board:Board):
  # return True if the board is solved, just need to
  # check one dim 
  print('in is_solved')
  for i in range(9):
    if not board.row_of(i).is_complete():
      return False
  return True


def is_valid(board:Board, row, col, num):
  """Checks if a number is valid in a given cell."""
  print('in is_valid')
  for h in board.houses(row, col):
    if num in h.array:
      print(f"Found value {num} in {h.dim.name} {h.idx}")
      return False
  return True


def find_empty(board:Board):
  """Finds an empty cell in the board."""
  for x, r in enumerate(board.rows()):
     for y, c in enumerate(r):
       if c == 0:
         return x, y
  return None,None
