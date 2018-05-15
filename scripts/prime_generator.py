
class PrimeGenerator(object):
    """Class wrapper for prime generator."""
    def generate_prime(self, max_num:int)->list:
        """ 
        Return an array of all the primes as True in the prime index.
        Args:
            s1 (str): string to be compressed

        Returns:
            list: Array of Booleans, default is false, True at the index of primes

        Examples:

        >>> pg = PrimeGenerator()
        >>> pg.generate_prime(10)
        [False, False, True, True, False, True, False, True, False, False]
        
        """
        if max_num is None:
            raise TypeError('max_num can not be none')
        array = [True] * max_num
        array[0] = False
        array[1] = False
        prime = 2
        while prime <= max_num ** 0.5:
            self._cross_off(array, prime)
            prime = self._next_prime(array, prime)
        return array
    
    def _cross_off(self, array, prime):
        for i in range(prime*prime, len(array), prime):
            array[i] = False
    
    def _next_prime(self, array, prime):
        next = prime + 1
        while next < len(array) and not array[next]:
            next += 1
        return next