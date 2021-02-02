#!/usr/bin/env python3
''' Redis Module '''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' def count calls '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper '''
        key_m = method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' def call history '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper'''
        key_m = method.__qualname__
        inp_m = key_m + ':inputs'
        outp_m = key_m + ":outputs"
        data = str(args)
        self._redis.rpush(inp_m, data)
        fin = method(self, *args, **kwds)
        self._redis.rpush(outp_m, str(fin))
        return fin
    return wrapper


def replay(method: Callable):
    ''' def replay '''
    key_m = method.__qualname__
    inp_m = key_m + ":inputs"
    outp_m = key_m + ":outputs"
    x = method.__self__.redis
    y = x.get(key_m).decode("utf-8")
    print("{} was called {} times:".format(key_m, y))
    l1 = redis.lrange(inp_m, 0, -1)
    l2 = redis.lrange(outp_m, 0, -1)
    r = list(zip(l1, l2))
    for a, b in r:
        atb, fin = x.decode("utf-8"), y.decode("utf-8")
        print(f"{}(*{}) -> {}".format(key_m, atb, fin))


class Cache():
    ''' class cache '''
    def __init__(self):
        ''' def init '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' def store '''
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        ''' def get '''
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
