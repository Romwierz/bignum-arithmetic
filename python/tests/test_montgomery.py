import unittest
from python.montgomery import *

class TestDiv(unittest.TestCase):
    def test_mont(self):
        a = 235147
        b = 11034
        m = 14567
        _a = montgomery_convert_in(a, m)
        _b = montgomery_convert_in(b, m)
        _x = mul_montgomery(_a, _b, m)
        x = montgomery_convert_out(_x, m)
        self.assertEqual(x, 10793)

if __name__ == "__main__":
    unittest.main()
