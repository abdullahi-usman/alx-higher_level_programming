#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectid(self):
        rect = Rectangle(10, 2, 0, 0, 12)

        self.assertTrue(rect.id == 12)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 3 * 2)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)

if __name__ == '__main__':
    unittest.main()
