#!/usr/bin/env python3
''' caching systems '''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache '''
    def __init__(self):
        self.last_put = ""
        super().__init__()

    def put(self, key, item):
        ''' Function puts '''
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_put)
            print('DISCARD:', self.last_put)
        if key:
            self.last_put = key

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
