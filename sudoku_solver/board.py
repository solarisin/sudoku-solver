import numpy as np


class Board:
  def __init__(self, board):
    self.board = np.array(board)

  
  def __str__(self):
    board_str = str()
    for i in range(9):
      if i % 3 == 0 and i != 0:
        board_str += "- - - + - - - + - - -\n"
      for j in range(9):
        if j % 3 == 0 and j != 0:
          board_str += "| "
        board_str += str(self.board[i][j]) if self.board[i][j] != 0 else "."
        board_str += " "
      board_str += "\n"
    return board_str

  def __eq__(self, other):
    return np.array_equal(self.board, other.board)

  
  def rows(self):
    '''Returns a list of rows'''
    return self.board.tolist()

  
  def cols(self):
    '''Retruns a list of columns'''
    return self.board.T.tolist()

  
  def regions(self):
    '''Returns a list of 3x3 sub-boards'''
    regions = []
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        regions.append(self.board[i:i+3, j:j+3].tolist())
    return regions
