from collections import deque
from Maze import Maze


class PathFinder:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.visited_cells = set()
        self.queue = deque()
        self.current_position = maze.start
        self.visited_cells.add(self.current_position)
        self.path_tracker = {maze.start: None}
        self.solution_path = []

    def reconstruct_path(self):
        path = []
        last_position = self.maze.end
        while last_position is not None:
            path.append(last_position)
            last_position = self.path_tracker[last_position]
        self.solution_path = path

    def backtracking_traversal(self):
        print("Pathfinding.")

        if self.current_position == self.maze.end:
            print("Maze solved.")
            self.reconstruct_path()
            return False

        # add safety check in case queue is empty

        adjacent_cells = self.maze.get_neighboring_path(self.current_position)
        for cell in adjacent_cells:
            if cell not in self.visited_cells:
                self.queue.append(cell)
                self.visited_cells.add(cell)
                self.path_tracker[cell] = self.current_position # upcoming adjacent: predecessor

        self.current_position = self.queue.popleft()

        return True