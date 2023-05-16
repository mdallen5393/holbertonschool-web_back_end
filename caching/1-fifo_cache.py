#!/usr/bin/env python3
"""
Defines a class `FIFOCache` that inherits from `BaseCaching`
and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implementation of a cache using FIFO.
    """
    def __init__(self):
        super().__init__()
        self.count = 0
        self.key_list = []

    def put(self, key, item):
        """
        Adds an item to the cache; if the cache is full, replaces
        the correct item.
        """
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # We need to replace an item
                removed_key = next(iter(self.cache_data))
                self.cache_data.pop(removed_key)
                print("DISCARD: {}".format(removed_key))

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
