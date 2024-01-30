#!/usr/bin/python3
"""
BasicCache module that inherits from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
