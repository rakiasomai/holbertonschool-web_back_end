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
                user = self._db.add_user(email, _hash_password(password))
                return user
            else:
                raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        ''' def valid login '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        ''' def create session '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        ''' def get user from session id '''
        if not session_id:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        ''' def destroy session '''
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        ''' def get reset password token '''
        if email:
            try:
                user = self._db.find_user_by(email=email)
            except NoResultFound:
                raise ValueError
            else:
                take = _generate_uuid()
                self._db.update_user(user.id, reset_token=take)
                return take
