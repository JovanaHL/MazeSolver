import random
from Maze import Maze



class MazeGenerator:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.visited_cells = set()
        self.stack = []
        self.current_position = maze.start
        self.visited_cells.add(maze.start)

    def backtracking_traversal(self):
        print("Current position: ",self.current_position.x, self.current_position.y)
        adjacent_cells = self.maze.get_neighboring(self.current_position)
        unvisited_cells = []
        for cell in adjacent_cells:
            if cell not in self.visited_cells:
                unvisited_cells.append(cell)

        if not unvisited_cells:
            print("There are no adjacent cells available for traversal. Attempt backtracking.")
            if not self.stack:
                print("Stack is empty. Nothing to do.")
                return False
            last_position = self.stack.pop()
            self.current_position = last_position
        else:
            self.stack.append(self.current_position)
            print("Added to stack: ", self.current_position.x, self.current_position.y)
            adjacent_cell = random.choice(unvisited_cells)
            print("Adjacent cell: " + str(adjacent_cell.x), str(adjacent_cell.y))
            self.visited_cells.add(adjacent_cell)
            self.maze.remove_wall(self.current_position, adjacent_cell)
            self.current_position = adjacent_cell



        if len(self.visited_cells) >= self.maze.width * self.maze.height:
            print("We have reached maze completion.")
            return False
        return True
