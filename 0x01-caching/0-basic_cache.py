#!/usr/bin/python3
"""BasicCache module.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class.
    """

    def __init__(self):
        """Constructor.
        """
        super().__init__()

    def put(self, key, item):
        """Put method.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get method.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
