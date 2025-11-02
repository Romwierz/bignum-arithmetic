import unittest
from python.arithmetic8 import *

class TestAdd8(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add8(0xFF, 0x01, 0), (0x00, 1))

if __name__ == "__main__":
    unittest.main()
