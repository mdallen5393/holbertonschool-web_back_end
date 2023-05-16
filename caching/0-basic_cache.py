#!/usr/bin/env python3
"""
Defines a class `BasicCache` that inherits from `BaseCaching`
and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implementation of a cache using a basic dictionary.
    """
    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
