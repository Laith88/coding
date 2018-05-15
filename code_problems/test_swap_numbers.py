import unittest
import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    """ Test the implementation of swap numbers solution """
    def setUp(self):
        self.sn = swap_numbers.SwapNumbers()
        
    def test_swap_numbers_1_2_3(self):
        self.assertEqual((3,2), self.sn.swap_numbers_2(2, 3))
        
    def test_none_input(self):
        self.assertRaises(Exception, self.sn.swap_numbers_2, (None, 3))
    
    def test_none_input_1(self):
        self.assertRaises(Exception, self.sn.swap_numbers_2, (None, None))
        
        
        
if __name__ == '__main__':
    unittest.main()