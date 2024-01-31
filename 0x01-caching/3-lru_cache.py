#!/usr/bin/python3
"""
LRUCache module that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.order_used:
                self.order_used.remove(key)
            self.order_used.insert(0, key)

            if len(self.order_used) > BaseCaching.MAX_ITEMS:
                discarded_key = self.order_used.pop(-1)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Get an item from the cache
        """
        if key in self.order_used:
            self.order_used.remove(key)
            self.order_used.append(key)
        return self.cache_data.get(key, None)
