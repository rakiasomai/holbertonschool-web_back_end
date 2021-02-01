#!/usr/bin/env python3
''' Hashed Module '''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    ''' def hash password '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    ''' def generate uid '''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' def register user '''
        if email and password:
            try:
                self._db.find_user_by(email=email)
            except NoResultFound:
                new_user = self._db.add_user(email, _hash_password(password))
                return new_user
            else:
                raise ValueError("User {} already exists".format(email))
