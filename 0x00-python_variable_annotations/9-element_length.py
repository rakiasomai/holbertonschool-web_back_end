#!/usr/bin/env python3
''' annotations '''
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' function that return th value withe the appropriate types '''
    return [(i, len(i)) for i in lst]
