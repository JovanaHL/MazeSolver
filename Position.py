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

    def get_direction_to(self, other_position):
        # return Direction from this Position to another position, or None if not adjacent
        # get distances in x and y pos
        dx = other_position.x - self.x
        dy = other_position.y - self.y

        # check if not adjacent and immediately return no direction
        if abs(dx) + abs(dy) != 1:
            return None

        for direction in Direction:
            if direction.value == (dx, dy):
                return direction

        raise ValueError("Unexpected direction")
  
    def get_position(self):
        return self.x, self.y

    def get_adjacent(self, direction):
        delta_x, delta_y = direction.value
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        return Position(new_x, new_y)

