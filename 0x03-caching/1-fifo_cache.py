#!/usr/bin/python3
''' caching systems '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOcache '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' Function put '''
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            x = sorted(self.cache_data)[0]
            self.cache_data.pop(x)
            print('DISCARD:', x)

    def get(self, key):
        ''' Function get '''
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
