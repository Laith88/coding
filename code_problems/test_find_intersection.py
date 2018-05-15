
import unittest
from find_intersection import Point, Line, FindIntersection

class TestSwapNumbers(unittest.TestCase):
    """ Test the implementation of swap numbers solution """
        
    def test_intersection_general_case(self):
        p1 = Point(4,1)
        p2 = Point(7,6)
        p3 = Point(4,6)
        p4 = Point(7,1)
        l1 = Line(p1, p2)
        l2 = Line(p3, p4)
        fi = FindIntersection()
        (a,b) = fi.find_intesection(l1, l2)
        self.assertAlmostEqual(a, 5.5)
        self.assertAlmostEqual(b, 3.5)
    
    def test_no_intersection_general_case(self):
        p1 = Point(1,5)
        p2 = Point(2,3)
        p3 = Point(4,1)
        p4 = Point(7,6)
        l1 = Line(p1, p2)
        l2 = Line(p3, p4)
        fi = FindIntersection()
        result = fi.find_intesection(l1, l2)
        self.assertFalse(result)
    
    def test_vertical_line_exception(self):
        self.assertRaises(Exception, Line, (Point(1,5),Point(1,3)))
        
    def test_horizontal_lines_exception(self):
        p1 = Point(1,5)
        p2 = Point(2,5)
        p3 = Point(4,7)
        p4 = Point(7,6)
        l1 = Line(p1, p2)
        l2 = Line(p3, p4)
        fi = FindIntersection()
        self.assertRaises(Exception, fi.find_intesection, (l1, l2))
        
if __name__ == '__main__':
    unittest.main()