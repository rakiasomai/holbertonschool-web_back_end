#!/usr/bin/env python3
''' Session Auth '''

from api.v1.auth.auth import Auth
from uuid import uuid4


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
