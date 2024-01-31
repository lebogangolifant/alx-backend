#!/usr/bin/env python3
"""
LIFOCache module that inherits from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.current_keys:
                self.current_keys.remove(key)
            self.current_keys.append(key)

            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(-2)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
