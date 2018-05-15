class CompressString(object):
    """ compress a string """
    
    def compress(self, s1:str) -> str:
         """Example function with types documented in the docstring.

        Args:
            s1 (str): string to be compressed

        Returns:
            str: The return value. compressed string

        Examples:

        >>> cs = CompressString()
        >>> cs.compress('AAABCCDDDDE')
        'A3BC2D4E'

        """

        if s1 is None:
            return None
        if s1 is '':
            return ''
        result = ''
        cache = []
        for char in s1:
            if char in cache:
                continue
            else:
                cache.append(char)
            tmp_count = s1.count(char)
            if tmp_count > 1:
                result = result + char + str(tmp_count)
            else:
                result = result + char
        return result