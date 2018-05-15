class SwapNumbers(object):
    """ swaps two numbers in place """
    def swap_numbers_1(self, a, b):
        if a is None or b is None:
            raise Exception('inputs a or b can not be none')
        if a == b:
            return (a, b)
        a = a - b
        b = a + b
        a = b - a
        return (a, b)
    
    def swap_numbers_2(self, a, b):
        if a is None or b is None:
            raise Exception('inputs a or b can not be none')
        if a == b:
            return (a, b)
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return (a, b)