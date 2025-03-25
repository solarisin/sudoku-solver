from typing import Annotated, Literal, TypeVar
from beartype import beartype
from beartype.vale import Is, IsAttr, IsEqual
import numpy as np
import numpy.typing as npt
from enum import Enum

house_t = Annotated[npt.NDArray[np.integer], Is[lambda array: array.shape == (9,) and array.max() <= 9 and array.min() >= 0]]

board_t = Annotated[npt.NDArray[np.integer], IsAttr["shape", IsEqual[(9,9)]]]

DimIdx = Annotated[int, Is[lambda x: 0 <= x < 9]]


class HouseDim(Enum):
  ROW = 0
  COL = 1
  REGION = 2

class House:
  def __init__(self, dim:HouseDim, idx:DimIdx, array:house_t):
    self.dim = dim
    self.idx = idx
    self.array = array

  def __str__(self):
    return f"{self.dim.name} {self.idx}: {self.array}"

  def is_complete(self) -> bool:
    return sorted(self.array) == list(range(1, 10))


class Board:
  def __init__(self, board:board_t):
    self.board = board

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

  def __ne__(self, other):
    return not self.__eq__(other)

  def houses(self, r:DimIdx, c:DimIdx):
    return self.row_of(r), self.col_of(c), self.region_of(r,c)

  def row_of(self, r:DimIdx) -> House:
    return House(HouseDim.ROW, r, self.board[r])

  def col_of(self, c:DimIdx):
    return House(HouseDim.COL, c, self.board[:, c])

  def region_of(self, r:DimIdx, c:DimIdx):
    reg_idx = (r // 3) * 3 + (c // 3)
    regions = self.regions()
    return House(HouseDim.REGION, reg_idx, regions[reg_idx])

  def rows(self):
    return self.board.tolist()

  def cols(self):
    return self.board.T.tolist()

  def regions(self):
    regs = np.zeros((0,9), dtype=np.integer)
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        freg = self.board[i:i+3, j:j+3].flatten()
        regs= np.append(regs, [freg], axis=0)
    return regs
