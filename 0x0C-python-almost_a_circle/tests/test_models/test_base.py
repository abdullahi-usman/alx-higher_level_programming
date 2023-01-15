
import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    def test_baseid(self):
        b1 = Base()
        self.assertTrue(b1.id > 0)


if __name__ == '__main__':
    unittest.main()
