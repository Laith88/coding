
class BloomFilter(object):
    def __init__(self, size=1000, p= 0.75, n=10^6):
        """
        Args:
            n:int - number of elements
            p:float - desired false probability
            m:int - required number of bits
        
        """
        self.bits = 0
        self.size = size
        self.k = 
        
    def _hash_function(self):
        return x % self.size
    
    def add(self, value):
        """ Insert a value into the bloom filter """
        self.bits = self.bits | 1<<self._hash_function(value)
    
    def __contains__(self, value):
        if self.bits & 1<<self._hash_function(value) == 0:
            return False
        return True