import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        
        
        self.d = collections.OrderedDict()
        self.capacity = capacity
        

    # @return an integer
    def get(self, key):
        try:
            v = self.d.pop(key)
            self.d[key] = v
            return v
        except KeyError:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            self.d.pop(key)
        except KeyError:
            if self.capacity == len(self.d):
                self.d.popitem(last = False)
                
        self.d[key] = value
        

