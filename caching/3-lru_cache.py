#!/usr/bin/env python3
"""
Defines a class `LRUCache` that inherits from `BaseCaching`
and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implementation of a cache using LRU.
    """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Adds an item to the cache; if the cache is full, replaces
        the correct item.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            # key exists, but item is different; still counts as a replacement
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # We need to replace an item
            removed_key = self.queue.pop(0)
            self.cache_data.pop(removed_key)
            print("DISCARD: {}".format(removed_key))

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if not key or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
