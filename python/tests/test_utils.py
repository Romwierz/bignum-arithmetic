import unittest
from python.utils import *

class TestCompare(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(compare([0x01, 0x00], [0x01, 0x00]), 0)

    def test_greater(self):
        self.assertEqual(compare([0x02, 0x00], [0x01, 0x00]), 1)

    def test_smaller(self):
        self.assertEqual(compare([0x00, 0x00], [0x01, 0x00]), -1)

class TestShiftLeft1(unittest.TestCase):
    def test_shift_1(self):
        x = [0b00000001, 0b00000000]
        shift_left_1(x)
        self.assertEqual(x, [0b00000010, 0b00000000])

    def test_shift_2(self):
        x = [0b10000000, 0b00000000]
        shift_left_1(x)
        self.assertEqual(x, [0b00000000, 0b00000001])

    def test_shift_3(self):
        x = [0b11111111, 0b11111111]
        shift_left_1(x)
        self.assertEqual(x, [0b11111110, 0b11111111])

class TestBitCnt(unittest.TestCase):
    def test_equal1(self):
        self.assertEqual(get_bits_cnt(0b1010), 4)

    def test_equal2(self):
        self.assertEqual(get_bits_cnt(0b10100000), 8)

    def test_equal3(self):
        self.assertEqual(get_bits_cnt(0b10101000100010001000100), 23)

if __name__ == "__main__":
    unittest.main()
