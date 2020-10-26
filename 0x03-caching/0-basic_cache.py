#!/usr/bin/env python3
''' caching systems '''
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache class inherit from BaseCaching '''

    def get(self, key):
        ''' function get
        '''
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)

    def put(self, key, item):
        ''' function put
        '''
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
