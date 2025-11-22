import tkinter as tk
from Maze import Maze, Cell
from MazeGenerator import MazeGenerator
from Position import Position


class MazeGUI:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.cell_size = 50
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=maze.width*self.cell_size, height=maze.height*self.cell_size, bg="white")
        self.generator = MazeGenerator(maze)

    def setup(self):
        self.window.title("Maze Generator")
        self.canvas.pack(fill="both", expand=True)

    def create(self):
        for row in range(self.maze.height):
            for col in range(self.maze.width):
                self.draw(Position(row, col), 'blue')
                self.draw_wall(Position(row, col), 'black')


    def draw(self, position: Position, color):
        x1 = position.y * self.cell_size # swapped because col -> position.y (horizontal; LEFT/RIGHT)
        y1 = position.x * self.cell_size # swapped because row -> position.x (vertical; UP/DOWN)
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)

    def draw_wall(self, position: Position, color):
        x1 = position.y * self.cell_size
        y1 = position.x * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        cell = self.maze.get_cell(position)

        if cell.north_wall:
            self.canvas.create_line(x1, y1, x2, y1, fill=color, width=2)

        if cell.south_wall:
            self.canvas.create_line(x1, y2, x2, y2, fill=color, width=2)

        if cell.west_wall:
            self.canvas.create_line(x1, y1, x1, y2, fill=color, width=2)

        if cell.east_wall:
            self.canvas.create_line(x2, y1, x2, y2, fill=color, width=2)

    def run(self):
        self.create()
        self.window.mainloop()

    def animate_step(self):
        if self.generator.backtracking_traversal():
            self.redraw()
            self.window.after(100, self.animate_step)
        else:
            self.redraw()
            self.draw(self.generator.current_position, 'white')
            self.draw_wall(self.generator.current_position, 'black')
            print("Traversal finished.")

    def redraw(self):
        for cell in self.generator.visited_cells:
            self.draw(cell, 'white')
            self.draw_wall(cell, 'black')
        self.draw(self.generator.current_position, 'red')
        self.draw_wall(self.generator.current_position, 'black')


if __name__ == "__main__":
    maze = Maze(10, 10)
    gui = MazeGUI(maze)
    gui.setup()
    gui.animate_step()
    gui.run()


