from enum import Enum
class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

  
    def get_position(self):
        return self.x, self.y

    def get_adjacent(self, direction):
        delta_x, delta_y = direction.value
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        return Position(new_x, new_y)