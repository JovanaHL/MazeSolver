import tkinter as tk
from Maze import Maze
from MazeGenerator import MazeGenerator


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
                print(f"Drawing cell {row}:{col}")
                self.draw(row, col, 'blue')

    def draw(self, row, col, color):
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='red', fill=color, width=2)

    def run(self):
        self.create()
        self.window.mainloop()

    def animate_step(self):
        if self.generator.onestep_traversal():
            self.redraw()
            self.window.after(100, self.animate_step)
        else:
            print("Traversal finished.")

    def redraw(self):
        for cell in self.generator.visitedCells:
            self.draw(cell.x, cell.y, 'white')
        self.draw(self.generator.current_position.x, self.generator.current_position.y, color='red')


if __name__ == "__main__":
    maze = Maze(10, 10)
    gui = MazeGUI(maze)
    gui.setup()
    gui.animate_step()
    gui.run()


