
import unittest
from factorial_zeros import FactorialZeros

class TestFactorialZeros(unittest.TestCase):
    """ Test the implementation of swap numbers solution """
        
    def test_factorial_zeros_general_case(self):
        fz = FactorialZeros()
        result = fz.count_zeros(15)
        self.assertEqual(result, 3)
    
    def test_factorial_zeros_none_input(self):
        fz = FactorialZeros()
        self.assertRaises(Exception,fz.count_zeros, None)
        
if __name__ == '__main__':
    unittest.main()