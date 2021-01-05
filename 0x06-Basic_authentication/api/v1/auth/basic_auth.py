#!/usr/bin/env python3
''' Module of Basic_auth
'''
import base64
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
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        ''' def decode base 64 authorization '''
        if base64_authorization_header and type(base64_authorization_header) == str:
            try:
                x = base64_authorization_header.encode('utf-8')
                base = base64.b64decode(x)
                return base.decode('utf-8')
            except Exception:
                return None
