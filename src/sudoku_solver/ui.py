# sudoku_solver/ui.py

import pygame
from sudoku_solver.board import Board
from sudoku_solver.logic import solve_sudoku, brute_force_solve

class SudokuGUI:
    def __init__(self, board: Board):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 600))
        pygame.display.set_caption("Sudoku Solver")
        self.board = board
        self.font = pygame.font.SysFont(None, 40)
        self.message = ""
        self.selected_cell = (0, 0)
        self.history = []

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
        pygame.draw.rect(self.screen, (255, 0, 0), (self.selected_cell[1] * 60, self.selected_cell[0] * 60, 60, 60), 3)
        self.highlight_same_numbers()
        if self.message:
            message_text = self.font.render(self.message, True, (255, 0, 0))
            self.screen.blit(message_text, (10, 550))
        self.draw_buttons()
        pygame.display.flip()

    def draw_buttons(self):
        solve_button = pygame.Rect(10, 560, 100, 30)
        undo_button = pygame.Rect(120, 560, 100, 30)
        pygame.draw.rect(self.screen, (0, 0, 0), solve_button)
        pygame.draw.rect(self.screen, (0, 0, 0), undo_button)
        solve_text = self.font.render("Solve", True, (255, 255, 255))
        undo_text = self.font.render("Undo", True, (255, 255, 255))
        self.screen.blit(solve_text, (20, 565))
        self.screen.blit(undo_text, (130, 565))

    def update_board(self, board: Board):
        self.board = board
        self.draw_board()

    def solve_and_update(self):
        self.save_state()
        brute_force_solve(self.board)
        self.update_board(self.board)

    def display_message(self, message: str):
        self.message = message
        self.draw_board()

    def handle_key_event(self, event):
        if event.key in range(pygame.K_1, pygame.K_10):
            num = event.key - pygame.K_0
            self.save_state()
            self.board.board[self.selected_cell[0]][self.selected_cell[1]] = num
            self.draw_board()
        elif event.key == pygame.K_UP:
            self.selected_cell = (max(self.selected_cell[0] - 1, 0), self.selected_cell[1])
        elif event.key == pygame.K_DOWN:
            self.selected_cell = (min(self.selected_cell[0] + 1, 8), self.selected_cell[1])
        elif event.key == pygame.K_LEFT:
            self.selected_cell = (self.selected_cell[0], max(self.selected_cell[1] - 1, 0))
        elif event.key == pygame.K_RIGHT:
            self.selected_cell = (self.selected_cell[0], min(self.selected_cell[1] + 1, 8))
        self.draw_board()

    def handle_mouse_event(self, event):
        if event.button == 1:  # Left mouse button
            pos = pygame.mouse.get_pos()
            if 560 <= pos[1] <= 590:
                if 10 <= pos[0] <= 110:
                    self.solve_and_update()
                elif 120 <= pos[0] <= 220:
                    self.undo()
            else:
                self.selected_cell = (pos[1] // 60, pos[0] // 60)
            self.draw_board()

    def highlight_same_numbers(self):
        selected_value = self.board.board[self.selected_cell[0]][self.selected_cell[1]]
        if selected_value != 0:
            for r in range(9):
                for c in range(9):
                    if self.board.board[r][c] == selected_value and (r, c) != self.selected_cell:
                        pygame.draw.rect(self.screen, (0, 255, 0), (c * 60, r * 60, 60, 60), 3)

    def save_state(self):
        self.history.append(self.board.board.copy())

    def undo(self):
        if self.history:
            self.board.board = self.history.pop()
            self.draw_board()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_event(event)
            self.draw_board()
        pygame.quit()
