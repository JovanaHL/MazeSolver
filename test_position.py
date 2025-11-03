from unittest import TestCase

from Position import Position, Direction


class TestPosition(TestCase):
    def test_init(self):
        """Test Position initialization with x and y coordinates."""
        position = Position(5, 5)
        self.assertEqual(position.x, 5)
        self.assertEqual(position.y, 5)

    def test_get_position(self):
        """Test get_position returns tuple of (x, y) coordinates."""
        position = Position(5, 5)
        x, y = position.get_position()
        self.assertEqual(x, 5)
        self.assertEqual(y, 5)

    def test_get_adjacent_up(self):
        """Test get_adjacent with UP direction increases y by 1."""
        position = Position(5, 5)
        adjacent = position.get_adjacent(Direction.UP)
        self.assertEqual(adjacent.x, 5)
        self.assertEqual(adjacent.y, 6)

    def test_get_adjacent_down(self):
        """Test get_adjacent with DOWN direction decreases y by 1."""
        position = Position(5, 5)
        adjacent = position.get_adjacent(Direction.DOWN)
        self.assertEqual(adjacent.x, 5)
        self.assertEqual(adjacent.y, 4)

    def test_get_adjacent_left(self):
        """Test get_adjacent with LEFT direction decreases x by 1."""
        position = Position(5, 5)
        adjacent = position.get_adjacent(Direction.LEFT)
        self.assertEqual(adjacent.x, 4)
        self.assertEqual(adjacent.y, 5)

    def test_get_adjacent_right(self):
        """Test get_adjacent with RIGHT direction increases x by 1."""
        position = Position(5, 5)
        adjacent = position.get_adjacent(Direction.RIGHT)
        self.assertEqual(adjacent.x, 6)
        self.assertEqual(adjacent.y, 5)

    def test_get_adjacent_negative_coordinates(self):
        """Test get_adjacent handles negative coordinates correctly."""
        position = Position(0, 0)
        adjacent_left = position.get_adjacent(Direction.LEFT)
        adjacent_down = position.get_adjacent(Direction.DOWN)
        self.assertEqual(adjacent_left.x, -1)
        self.assertEqual(adjacent_left.y, 0)
        self.assertEqual(adjacent_down.x, 0)
        self.assertEqual(adjacent_down.y, -1)

    def test_direction_enum_values(self):
        """Test Direction enum contains correct delta values for each direction."""
        self.assertEqual(Direction.UP.value, (0, 1))
        self.assertEqual(Direction.DOWN.value, (0, -1))
        self.assertEqual(Direction.LEFT.value, (-1, 0))
        self.assertEqual(Direction.RIGHT.value, (1, 0))

