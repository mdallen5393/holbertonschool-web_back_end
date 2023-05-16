#!/usr/bin/env python3
"""
Defines a class `LIFOCache` that inherits from `BaseCaching`
and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implementation of a cache using LIFO.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache; if the cache is full, replaces
        the correct item.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # We need to replace an item
            removed_key, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(removed_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
