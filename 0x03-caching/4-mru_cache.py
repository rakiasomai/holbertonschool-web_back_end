#!/usr/bin/python3
''' caching systems '''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache '''
    def __init__(self):
        self.counter = 0
        self.ages = {}
        super().__init__()

    def put(self, key, item):
        ''' Function puts '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                x = sorted(self.ages.items(),
                           key=lambda x: x[1], reverse=True)[0][0]
                self.cache_data.pop(x)
                self.ages.pop(x)
                print('DISCARD:', x)

            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key):
        ''' Function get '''
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        return None
