#!/usr/bin/env python3
''' annotations '''
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    ''' Function that return the value '''
    if key in dct:
        return dct[key]
    else:
        return default
