#!/usr/bin/env python3
''' Session Auth '''

from api.v1.auth.auth import Auth
from uuid import uuid4
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    ''' class auth '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' def create session '''
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' def user id for session id '''
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        ''' def current user '''
        if request is None:
            return None
        s_cookie = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(s_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        ''' def destroy session (logout) '''
        if not request:
            return False
        s_cookie = self.session_cookie(request)
        if not s_cookie:
            return False
        user_id = self.user_id_for_session_id(s_cookie)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(s_cookie)
        return True
