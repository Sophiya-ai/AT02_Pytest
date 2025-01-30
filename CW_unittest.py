import unittest

from CW_arithm_ab import add, subtract

class Test_Math(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1), 2)


    def test_subtract(self):
        self.assertEqual(subtract(10,1), 9)

if __name__ == '__main__':
    unittest.main()