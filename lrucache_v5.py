class LRUCache:
    '''base class of least recent used cache
       created by David Spiegelman
       email: david94609@gmail.com '''

    def __init__(self, capacity):
        # slots - a list of dictionaries
        self.slots = [{'____': None}] * capacity

    def get(self, key):
        i = self.__findKey(key)
        if i == -1:
            return i
        
        self.slots.append(self.slots.pop(i))
        return self.slots[-1][key]

    def put(self, key, value):        
        i = self.__findKey(key)
        if i == -1:
            del self.slots[0]
            self.slots.append({key: value})
        else:
            self.slots.append(self.slots.pop(i))
            self.slots[-1][key] = value
        
    def __findKey(self, key):
        index = -1
        for x, v in enumerate(self.slots):
            if key in v:
                index = x
                break
        return index
        
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

