#!/usr/bin/env python3
''' annotations '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' function to multip '''
    def multip(n: float) -> float:
        return multiplier * n
    return multip
