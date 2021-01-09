#!/usr/bin/env python3
''' Personal Data '''

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    ''' Returns the log message obfuscated '''
    for field in fields:
        msg = re.sub(rf"{field}=(.*?)\{separator}",
                     f'{field}={redaction}{separator}', message)
    return msg
