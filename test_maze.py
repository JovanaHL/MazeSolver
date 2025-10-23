from unittest import TestCase

from Maze import Maze, CellType


class TestMaze(TestCase):
    def test_maze(self):
        maze = Maze(5, 5)
        self.assertEqual(maze.width, 5)
        self.assertEqual(maze.height, 5)

    def test_set_get_cell(self):
        maze = Maze(5, 5)
        maze.set_cell(3, 4, CellType.PATH)
        self.assertEqual(maze.width, 5)
        self.assertEqual(maze.height, 5)
        cell = maze.get_cell(3, 4)
        self.assertEqual(cell, CellType.PATH)

    def test_bounds(self):
        maze = Maze(5, 5)
        maze.set_cell(3, 4, CellType.PATH)

        self.assertRaises(IndexError, maze.get_cell, -1, -1)
        self.assertRaises(IndexError, maze.set_cell, 6, 6, CellType.PATH)


    def test_default_init(self):
        maze = Maze(5, 5)
        self.assertEqual(maze.get_cell(0, 0), CellType.PATH)

