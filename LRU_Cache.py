
"""
PROBLEM STATEMENT

design a data structure known as 
a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove
the least recently used entry when the cache memory
reaches its limit. For the current problem, 
consider both get and set operations as an use
operation.



Your job is to use an appropriate data structure(s) to implement the cache.

* In case of a cache hit, your get() operation should return the appropriate value.
* In case of a cache miss, your get() should return -1.
* While putting an element in the cache, 
your put() / set() operation must insert the element.
If the cache is full, you must write code that removes
the least recently used entry first and then insert 
the element.



All operations must take O(1) time

"""
#  we also see maps here, we can use the maps or dicts to store the caches

# we can use queues to keep track of lest recently viewed cache item

from collections import deque



class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict({})
        self.cache_history = deque()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        #check if key is in cache  
        
        if self.capacity == 0:
            return None

        # check it key is in cache and retrieve it,
        # then update the cache history and pop the oldest element
        if key in self.cache.keys():
            # retrieve and delete fro chache
            value = self.cache[key]
            del self.cache[key]
            
            #update history
            self.cache_history.appendleft(key)
            if len(self.cache_history) > self.capacity:
                self.cache_history.pop()
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # if check if chack is full 
        # and remove the least recently used entry

        self._put_cache(key,value)


    def _put_cache(self,key,value):
        # check zero capacity
        if self.capacity == 0:
            return None

        


        # a look up to check if key is in cache
        # and just update the chache history
        if key in self.cache.keys()\
             and self.size() < self.capacity:
             # empty the oldest key from the cache history
             self.cache_history.pop() 

        elif key not in self.cache.keys()\
             and self.size() < self.capacity:
             
             # put value into chache
             self.cache[key] = value
             # update history
             self.cache_history.appendleft(key)

             if len(self.cache_history) > self.capacity:
                 self.cache_history.pop()
            
        elif key not in self.cache.keys()\
            and self.size() == self.capacity:
            # get the oldest or tail from the history
            oldest_key = self.cache_history.pop()
            # delete it from the chache
            self.cache.pop(oldest_key)
            # now there is space to put new value
            self.cache[key] = value
            
            # update chache history
            self.cache_history.appendleft(key)

            if len(self.cache_history) > self.capacity:
                 self.cache_history.pop()

    def size(self):
        return len(self.cache)
    





our_cache = LRU_Cache(5)


our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9) )     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(2))      # returns -1 because the cache reached it's capacity and 2 was the least recently used entry
print(our_cache.get(3))      # returns -1 
print(our_cache.get(1)) 
print(our_cache.get(5))     # returns 5
print(our_cache.get(6))     # returns 6

our_cache.set(7, 7);
our_cache.set(8, 8);
our_cache.set(9, 9);

print(our_cache.get(2))      # returns -1 because the cache reached it's capacity 
print(our_cache.get(3))      # returns -1
print(our_cache.get(1))      # returns -1
print(our_cache.get(5))      # returns -1
print(our_cache.get(6))      # returns -1


print(our_cache.get(4))     # returns 4
print(our_cache.get(8))     # returns 8
print(our_cache.get(9))     # returns 9
print(our_cache.get(6))     # returns -1


# test case where capacity is null
our_cache = LRU_Cache(0)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);

print(our_cache.get(1))       # returns None since capacity is 0
print(our_cache.get(2))       # returns None since capacity is 0


# test case where capacity is negative
our_cache = LRU_Cache(-5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);

print(our_cache.get(1))       # returns -1 since capacity is -1
print(our_cache.get(2))       # returns -1 since capacity is -1