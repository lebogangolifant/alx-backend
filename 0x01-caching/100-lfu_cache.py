#!/usr/bin/python3
"""
LFUCache module that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.frequency = {}
        self.usage_count = {}

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.usage_count[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_frequency = min(self.frequency.values())
                    least_used_keys = [k for k, v in self.frequency.items()
                                       if v == min_frequency]

                    if len(least_used_keys) > 1:
                        least_used_keys = sorted(least_used_keys,
                                                 key=lambda k:
                                                 self.usage_count.get(k, 0))

                    discarded_key = least_used_keys[0]
                    del self.cache_data[discarded_key]
                    del self.frequency[discarded_key]
                    del self.usage_count[discarded_key]
                    print('DISCARD: {}'.format(discarded_key))

                # Add the new item to the cache
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.usage_count[key] = 1

    def get(self, key):
        """
        Get an item from the cache
        """
        if key in self.cache_data:
            # Update frequency and usage count
            self.frequency[key] += 1
            self.usage_count[key] += 1
        return self.cache_data.get(key, None)
