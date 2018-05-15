class FindDifference(object):
    """ find the difference between two strings """
    def find_diff_1(self, s1:str, s2:str) -> str:
        """
        Find the difference between s1 and s2 where s2 has one different string string.

        Args:
            s1: string to be compressed
            s2: string to be compressed



        Returns:
            str: single character string

        Examples:

        >>> fd = FindDifference()
        >>> fd.find_diff_1('test', 'tegt')
        'g'

        """
        if s1 is None and s2 is None:
            raise TypeError('Sting inputs can not be None')
        for char in s2:
            count_char_s1 = s1.count(char)
            count_char_s2 = s2.count(char)
            if count_char_s2 != count_char_s1:
                return char
        return ''
    
    def find_diff_2(self, s1, s2):
        """
        Find the difference between s1 and s2 where s2 has one different string string.

        Args:
            s1: string to be compressed
            s2: string to be compressed



        Returns:
            str: single character string

        Examples:

        >>> fd = FindDifference()
        >>> fd.find_diff_2('test', 'tegt')
        'g'

        """
        dict_s1 = {}
        dict_s2 = {}
        for char in s1:
            if char in dict_s1:
                dict_s1[char] += 1
            else:
                dict_s1[char] = 1     
        for char in s2:
            if char in dict_s2:
                dict_s2[char] += 1
            else:
                dict_s2[char] = 1
        for char in dict_s2:
            try:
                if char not in dict_s1 or dict_s2[char]>dict_s1[char]:
                    return str(char)
            except KeyError:
                continue
        return ''