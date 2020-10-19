#!/usr/bin/env python3
''' annotations '''
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Function to return the 1st element or None '''
    if lst:
        return lst[0]
    else:
        return None
