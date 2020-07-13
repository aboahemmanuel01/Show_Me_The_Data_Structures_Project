## Least Recently Used Cache

The goal of this project is to design an LRU which is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

My task is to use an appropriate data structure(s) to implement the cache with following guidelines:
```
In case of a cache hit, the get() operation should return the appropriate value.
In case of a cache miss, the get() should return -1.
While putting an element in the cache, the put() / set() operation must insert the element. 
If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.
```
For the current problem, the cache size was considered as; cache = 5.

The lookup operation `(i.e., get()) and put() / set()` is supposed to be fast for a cache memory.
