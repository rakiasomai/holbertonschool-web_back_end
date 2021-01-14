#!/usr/bin/env python3
''' Personal data '''

import bcrypt


def hash_password(password: str) -> bytes:
    ''' def hash password '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
