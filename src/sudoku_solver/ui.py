# sudoku_solver/ui.py

import pygame
from sudoku_solver.board import Board
from sudoku_solver.logic import solve_sudoku

class SudokuGUI:
    def __init__(self, board: Board):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 540))
        pygame.display.set_caption("Sudoku Solver")
        self.board = board
        self.font = pygame.font.SysFont(None, 40)
        self.message = ""

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), thickness)
        for r in range(9):
            for c in range(9):
                if self.board.board[r][c] != 0:
                    text = self.font.render(str(self.board.board[r][c]), True, (0, 0, 0))
                    self.screen.blit(text, (c * 60 + 20, r * 60 + 15))
        if self.message:
            message_text = self.font.render(self.message, True, (255, 0, 0))
            self.screen.blit(message_text, (10, 550))
        pygame.display.flip()

    def update_board(self, board: Board):
        self.board = board
        self.draw_board()

    def solve_and_update(self):
        solve_sudoku(self.board)
        self.update_board(self.board)

    def display_message(self, message: str):
        self.message = message
        self.draw_board()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_board()
        pygame.quit()
