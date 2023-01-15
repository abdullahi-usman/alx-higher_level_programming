
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(200)
        self.assertTrue(square.size == 200)