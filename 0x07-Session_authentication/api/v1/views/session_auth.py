#!/usr/bin/env python3
''' Session Auth '''

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    ''' def login '''
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify(error="email missing"), 400
    if password is None:
        return jsonify(error="password missing"), 400
    user = User.search({"email": email})
    if not user:
        return jsonify(error="no user found for this email"), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session = auth.create_session(user.id)
    json = jsonify(user.to_json())
    json.set_cookie(os.getenv('SESSION_NAME'), session)
    return json
