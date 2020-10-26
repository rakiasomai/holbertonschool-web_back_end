#!/usr/bin/env python3
''' caching systems '''
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache class inherit from BaseCaching '''

    def __init__(self):
        ''' initialize '''
        self.key_list = []
        super().__init__()

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
        if key in self.key_list:
            self.key_list.remove(key)
        if len(self.key_list) >= BaseCaching.MAX_ITEMS:
            y = self.key_list[0]
            print("DISCARD: {}".format(y))
            self.key_list.pop(0)
            self.cache_data.pop(y)
        self.cache_data.update({key: item})
        self.key_list.append(key)
