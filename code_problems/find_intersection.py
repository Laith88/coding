
class Point(object):
    """ return a point data stucture """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if not y: raise Exception('y can not be none')
        self._y = y
    
    @x.setter
    def x(self, x):
        if not x: raise Exception('x can not be none')
        self._x = x

class Line(object):
    """ return a point line stucture """
    def __init__(self, point1, point2):
        self.x2 = max(point1.x, point2.x)
        self.y1 = min(point1.y, point2.y)
        self.x1 = min(point1.x, point2.x)
        self.y2 = max(point1.y, point2.y)
        #catch a vertical line
        try:
            self.m = (point2.y-point1.y)/(point2.x-point1.x)
        except ZeroDivisionError as err:
            raise Exception('can not be vertical line')
        self.b = point1.y - (self.m*point1.x)
        
    def fun(self, x):
        """ return the y value given an x input for that specific line """
        return self.m * x + self.b
    
class FindIntersection(object):
    """ find an intersection point between two line segments """
    def __init__(self, delta = 0.001):
        self.delta = delta
        
    def find_intesection(self, l1, l2):
        if l1.m == l2.m:
            return False
        #catch division by zero
        try:
            x_p = (l1.b - l2.b) / (l2.m - l1.m)
        except ZeroDivisionError:
            return False    
        #make sure that we are still in the same range of the input segments
        if x_p >= max(l1.x1, l2.x1) and x_p <= min(l1.x2, l2.x2):
            y_p1 = l1.fun(x_p)
            y_p2 = l2.fun(x_p)
            if (y_p1 - y_p2) < self.delta:
                return (x_p, y_p1)
            else:
                return False
        else:
            return False