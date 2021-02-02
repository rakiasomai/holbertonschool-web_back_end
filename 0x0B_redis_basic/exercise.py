#!/usr/bin/env python3
''' Redis Module '''
import redis
import uuid
from typing import Union


class Cache():
    ''' class cache '''
    def __init__(self):
        ''' def init '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' def store '''
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen
