
from Position import Position, Direction


class Cell:
    def __init__(self):
        self.north_wall = True
        self.east_wall = True
        self.south_wall = True
        self.west_wall = True


# 2D Array or List of Lists
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[Cell() for _ in range(width)] for _ in range(height)]
        self.start = Position(0, 0)
        self.end = Position(width - 1, height - 1)

    def is_valid(self, position: Position):
        if position.x < 0 or position.x >= self.width or position.y < 0 or position.y >= self.height:
            return False
        return True

    def set_cell(self, position, cell):
        if not self.is_valid(position):
            raise IndexError(f'Invalid coordinates ({position.x}, {position.y}). Cell position out of bounds: w: {self.width}, h: {self.height}')
        self.maze[position.x][position.y] = cell


    def get_cell(self, position):
        if not self.is_valid(position):
            raise IndexError(f'Invalid coordinates ({position.x}, {position.y}).')
        return self.maze[position.x][position.y]

    def get_neighboring(self, position: Position):
        neighbors = []

        for direction in Direction:
            adjacent_pos = position.get_adjacent(direction)
            if self.is_valid(adjacent_pos):
                neighbors.append(adjacent_pos)


        return neighbors

    def remove_wall(self, position1: Position, position2: Position):
        direction = position1.get_direction_to(position2)
        if direction == None:
            raise ValueError(f"Position {position1} has no direction to {position2}. They are not adjacent.")

        if direction == Direction.UP:
            self.get_cell(position1).north_wall = False
            self.get_cell(position2).south_wall = False
        elif direction == Direction.DOWN:
            self.get_cell(position1).south_wall = False
            self.get_cell(position2).north_wall = False
        elif direction == Direction.RIGHT:
            self.get_cell(position1).east_wall = False
            self.get_cell(position2).west_wall = False
        elif direction == Direction.LEFT:
            self.get_cell(position1).west_wall = False
            self.get_cell(position2).east_wall = False
