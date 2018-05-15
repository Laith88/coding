
class Item(object):
    """Instantiate a item node data structure for the hash-table data stucture."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable(object):
    """Return hash-table data stucture."""
    def __init__(self, size = 11):
        self.size = size #size is pref. prime
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """Calculate a simple hash function."""
        return key % self.size
    
    def set(self, key, value):
        """set a key:value pair in the hash-table."""
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))
    
    def get(self, key):
        """get a key:value pair if in the hash-table."""
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')
        
    def remove(self, key):
        """remove a key:value pair if in the hash-table."""
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')
        
    def __getitem__(self, key):
        """Allow bracket access to hashtable for getting an item"""
        return self.get(key)
    
    def __setitem__(self, key, value):
        """Allow bracket access to hashtable for setting an item"""
        self.set(key, value)