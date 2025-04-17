import pytest
import pygame
from sudoku_solver.board import Board
from sudoku_solver.ui import SudokuGUI

class TestSudokuGUI:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.board = Board([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        self.gui = SudokuGUI(self.board)

    def test_unsolved_board_shown(self):
        self.gui.draw_board()
        assert self.gui.board == self.board

    def test_user_can_interact_with_board(self):
        self.gui.selected_cell = (0, 2)
        self.gui.handle_key_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_4))
        assert self.gui.board.board[0][2] == 4

    def test_user_can_solve_board(self):
        self.gui.solve_and_update()
        assert self.gui.board.is_solved()

    def test_user_can_undo_actions(self):
        self.gui.selected_cell = (0, 2)
        self.gui.handle_key_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_4))
        self.gui.undo()
        assert self.gui.board.board[0][2] == 0

    def test_solve_button_click(self):
        self.gui.handle_mouse_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(50, 570)))
        assert self.gui.board.is_solved()

    def test_undo_button_click(self):
        self.gui.handle_key_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_4))
        self.gui.handle_mouse_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(150, 570)))
        assert self.gui.board.board[0][2] == 0
