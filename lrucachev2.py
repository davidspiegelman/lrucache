class LRUCache:
    '''base class of least recent used cache
       created by David Spiegelman
       email: david94609@gmail.com '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.age = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.ages = list(range(-1 * capacity, 0)) 

    def get(self, key):
        i = self.__findKey(key)
        if i == -1:
            return i
        
        self.ages[i] = self.age
        self.age += 1    
        return self.values[i]

    def put(self, key, value):        
        i = self.__findKey(key)
        if i == -1:
            i, age = 0, self.ages[0]
            
            for x, v in enumerate(self.ages[1:], start=1):
                if v < age:
                    i, age = x, v
                
            self.keys[i] = key
                
        self.values[i] = value
        self.ages[i] = self.age
        self.age += 1      
        
    def __findKey(self, key):
        try:
            i = self.keys.index(key)
        except:
            return -1 
        return i
        
    def __str__(self):
        return str(tuple(zip(self.keys, self.values, self.ages))) 
        
        




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

