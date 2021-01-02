#!/usr/bin/env python3
'''
manage the API authentification
'''
from flask import request
from typing import TypeVar, List


class Auth():
    '''
    manage the API authentification
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' require_authentification '''
        return False

    def authorization_header(self, request=None) -> str:
        ''' def authorization_header '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' def current_user '''
        return None
