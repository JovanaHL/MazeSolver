# class for maze with size attributes
# will it call another file for maze generation

from enum import Enum

# for each cell
class CellType(Enum):
    WALL = '#'
    PATH = '[ ]'
    START = 'S'
    END = 'E'

# 2D Array or List of Lists
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[CellType.PATH for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, cell_type):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise IndexError(f'Invalid coordinates ({x}, {y}). Cell position out of bounds: w: {self.width}, h: {self.height}')
        self.maze[x][y] = cell_type


    def get_cell(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise IndexError(f'Invalid coordinates ({x}, {y}).')
        return self.maze[x][y]

