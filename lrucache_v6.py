class LRUCache:
    '''base class of least recent used cache
       created by David Spiegelman
       email: david94609@gmail.com '''

    def __init__(self, capacity):
        from collections import OrderedDict as ODict
        self.slots = ODict()
        self.capacity = capacity

    def get(self, key):
        try:
            value = self.slots[key]
        except:
            return -1
            
        del self.slots[key]
        self.slots[key] = value
        return value         

    def put(self, key, value):        
        try:
            del self.slots[key]
        except:
            if len(self.slots) == self.capacity:
                del self.slots[list(self.slots.keys())[0]]  
                   
        self.slots[key] = value            
        
    def __str__(self):
        return str(self.slots)
        
        




'''
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
'''
