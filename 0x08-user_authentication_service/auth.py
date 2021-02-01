#!/usr/bin/env python3
''' Hashed Module '''

import bcrypt


def _hash_password(password: str) -> str:
    ''' def hash password '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
