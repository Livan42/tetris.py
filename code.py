import tkinter as tk
import random
from threading import Lock

COLORS = ['gray', 'lightgreen', 'pink', 'blue', 'orange', 'purple']

class Tetris():
    FIELD_HEIGHT = 20
    FIELD_WIDTH = 10
    SCORE_PER_ELIMINATED_LINES = (0, 40, 100, 300, 1200)
    TETROMINOS = [
        [(0, 0), (0, 1), (1, 0), (1,1)], # O
        [(0, 0), (0, 1), (1, 1), (2,1)], # L
        [(0, 1), (1, 1), (2, 1), (2,0)], # J 
        [(0, 1), (1, 0), (1, 1), (2,0)], # Z
        [(0, 1), (1, 0), (1, 1), (2,1)], # T
        [(0, 0), (1, 0), (1, 1), (2,1)], # S
        [(0, 1), (1, 1), (2, 1), (3,1)], # I
    ]

def __init__(self):
        self.field = [[0 for c in range(Tetris.FIELD_WIDTH)] for r in range(Tetris.FIELD_HEIGHT)]
        self.score = 0
        self.level = 0
        self.total_lines_eliminated = 0
        self.game_over = False
        self.move_lock = Lock()
        self.reset_tetromino()

def reset_tetromino(self):
        self.tetromino = random.choice(Tetris.TETROMINOS)[:]
        self.tetromino_color = random.randint(1, len(COLORS)-1)
        self.tetromino_offset = [-2, Tetris.FIELD_WIDTH//2]
        self.game_over = any(not self.is_cell_free(r, c) for (r, c) in self.get_tetromino_coords())
    
def get_tetromino_coords(self):
        return [(r+self.tetromino_offset[0], c + self.tetromino_offset[1]) for (r, c) in self.tetromino]

def apply_tetromino(self):
        for (r, c) in self.get_tetromino_coords():
            self.field[r][c] = self.tetromino_color

        new_field = [row for row in self.field if any(tile == 0 for tile in row)]
        lines_eliminated = len(self.field)-len(new_field)
        self.total_lines_eliminated += lines_eliminated
        self.field = [[0]*Tetris.FIELD_WIDTH for x in range(lines_eliminated)] + new_field
        self.score += Tetris.SCORE_PER_ELIMINATED_LINES[lines_eliminated] * (self.level + 1)
        self.level = self.total_lines_eliminated // 10
        self.reset_tetromino()

 def get_color(self, r, c):
        return self.tetromino_color if (r, c) in self.get_tetromino_coords() else self.field[r][c]
 
 def is_cell_free(self, r, c):
        return r < Tetris.FIELD_HEIGHT and 0 <= c < Tetris.FIELD_WIDTH and (r < 0 or self.field[r][c] == 0)
    
 def move(self, dr, dc):
     with self.move_lock:
         if self.game_over:
             return

         if all(self.is_cell_free(r + dr, c + dc) for (r, c) in self.get_tetromino_coords()):
             self.tetromino_offset = [self.tetromino_offset[0] + dr, self.tetromino_offset[1] + dc]
         elif dr == 1 and dc == 0:
                self.game_over = any(r < 0 for (r, c) in self.get_tetromino_coords())
                if not self.game_over:
                    self.apply_tetromino()

