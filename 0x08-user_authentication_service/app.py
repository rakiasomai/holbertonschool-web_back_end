#!/usr/bin/env python3
''' Flask Module '''
from flask import Flask, jsonify, request, redirect, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    ''' def message '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    ''' def users '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def session() -> str:
    ''' def session '''
    email = request.form.get('email')
    password = request.form.get('password')
    log = AUTH.valid_login(email, password)
    if log:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
