#The Boilerplate code for this course was used as a template in this solution

import collections
#from collections import deque
from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()
        #self.order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        #if key is None:
         # return -1

        #return self.cache.get(key, -1)
        if key in self.cache.keys():
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        #if len(self.order) >= self.capacity:
        	#del self.cache[self.order.popleft()]

        #self.order.append(key)
        #self.cache[key] = value\

        try:
            self.cache.pop(key)

        except KeyError:

            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)

        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(1)

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3)) # Return -1

our_cache.set(7, 7);
print(our_cache.get(4)) 


our_cache = LRU_Cache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

print(our_cache.get(1))  # Return -1
print(our_cache.get(2))  # Return 2
print(our_cache.get(3))  # Return 3