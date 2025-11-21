import random

from Maze import Maze
from Position import Position


class MazeGenerator:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.visitedCells = set()
        self.stack = []
        self.current_position = maze.start
        self.visitedCells.add(maze.start)

    def onestep_traversal(self):
        start_position = self.current_position
        adjacent_cells = self.maze.get_neighboring(start_position)
        unvisited_cells = []
        for cell in adjacent_cells:
            if cell not in self.visitedCells:
                unvisited_cells.append(cell)

        if not unvisited_cells:
            print("There are no adjacent cells available for traversal.")
            return False
        adjacent_cell = random.choice(unvisited_cells)
        print("Adjacent cell: " + str(adjacent_cell.x), str(adjacent_cell.y))
        self.visitedCells.add(adjacent_cell)
        self.current_position = adjacent_cell

        if len(self.visitedCells) >= self.maze.width * self.maze.height:
            print("We have reached the end of the maze.")
            return False
        return True
