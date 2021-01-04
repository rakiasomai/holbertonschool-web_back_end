#!/usr/bin/env python3
''' Module of Basic_auth
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    ''' BasicAuth class
    '''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])
