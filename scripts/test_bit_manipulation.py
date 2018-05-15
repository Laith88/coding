import unittest
from bit_manipulation import Bit

class TestBit(unittest.TestCase):
    def test_get_bit(self):
        number = int('10001110', base=2)
        bit = Bit(number)
        self.assertEqual(bit.get_bit(index=3), True)

if __name__ == '__main__':
    unittest.main()