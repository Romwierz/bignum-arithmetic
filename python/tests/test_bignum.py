import unittest
from python.bignum import *

class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(div_bignum([0xff, 0xff], [0x02, 0x00]), ([0xff, 0x7f], [0x01, 0x00]))

if __name__ == "__main__":
    unittest.main()
