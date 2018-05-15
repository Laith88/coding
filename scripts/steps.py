class Steps(object):
    """ Count number of ways to climb up a staircase while taking 1, 2 or 3 steps at at time"""

    def count_ways(self, n:int) -> int:
        """
        Count the number of ways we can climb up the stairs such that we only take 1,2 or 3 steps at a time.

        Args:
            n1 (int): number of stairs

        Returns:
            int: The number of ways possible

        Examples:

        >>> ns = Steps()
        >>> ns.count_ways_memo(19)
        66012
        """
        if n is None:
            raise TypeError('Invalid input: please input a positive int')
        elif n <0:
            return 0
        elif n == 0:
            return 1 # ofcourse we can have this as zero but then we would an additional base case otherwise we would be just be adding multiple zeros
        else:
            return self.count_ways(n-1) + self.count_ways(n-2) + self.count_ways(n-3)
    
    def count_ways_memo(self, n):
        if n is None or n < 0:
            raise TypeError('number of steps can not be none or negative')
        cache = {}
        return self._count_ways(n, cache)
    
    def _count_ways(self, n, cache):
        if n < 0:
            return 0 
        if n == 0:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = self._count_ways(n-1,cache) + self._count_ways(n-2,cache) + self._count_ways(n-3,cache)
        return cache[n]
    