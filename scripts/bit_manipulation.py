
def validate_index(func):
        def _validate_index_wrap(self, *args, **kwargs):
            for arg in args:
                if arg < 0:
                    raise IndexError('Invalid Index')
            return func(self, *args, **kwargs)
        return _validate_index_wrap
    
    
class Bit(object):
    """ Initiate bit and perform bit related operations"""
    
    def __init__(self, number):
        if number is None:
            raise TypeError('number can not be None')
        self.number = number
        
    @validate_index
    def get_bit(self, index):
        return self.number & (1 << index) != 0

    @validate_index
    def set_bit(self, index):
        self.number |= (1 << index)
        return self.number
    
    @validate_index
    def clear_bit(self, index):
        self.number &= ~(1 << index)
        return self.number
    
    @validate_index
    def clear_bits_msb_to_index(self, index):
        self.number &= (~(1 << index) -1)
        return self.number

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        self.number &= ~((1 << index + 1) - 1)
    
    @validate_index
    def update_bit(self, index, value):
        if value is None or value not in (0, 1):
            raise Exception('Invalid value')
        if self.get_bit(index) == value:
            return self.number
        if value:
            self.set_bit(index)
        else:
            self.clear_bit(index)
        return self.number