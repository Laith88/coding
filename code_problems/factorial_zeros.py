
class FactorialZeros(object):
    """return the number of trailing zeros of a factorial n! where n:int"""
    def count_zeros(self, num):
        if num is None:
            raise Exception('input can not be None')
        num_5s = 0
        for i in range(2,num+1):
            num_5s  += self._find_num_5s(i)
        return num_5s
    
    def _find_num_5s(self, num):
        tmp = 0
        while num > 0 and num % 5 == 0:
            tmp += 1
            num = num // 5
        return tmp