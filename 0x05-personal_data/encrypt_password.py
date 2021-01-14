#!/usr/bin/env python3
''' Personal data '''

import bcrypt


def hash_password(password: str) -> bytes:
    ''' def hash password '''
    var = password.encode('utf-8')
    return bcrypt.hashpw(var, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' def is valid '''
    var = password.encode('utf-8')
    return bcrypt.checkpw(var, hashed_password)
