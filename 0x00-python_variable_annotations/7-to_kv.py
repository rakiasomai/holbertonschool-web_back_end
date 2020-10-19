#!/usr/bin/env python3
''' annotations '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Function that return tuple '''
    return (k, v * v)

