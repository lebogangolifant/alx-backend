#!/usr/bin/python3
"""
FIFOCache class module that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """
        Add an item to the cache (FIFO algorithm)
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))
            if key not in self.current_keys:
                self.current_keys.append(key)

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
