from flask import Flask, request, jsonify
from biscuit.util.json_format import *
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.user import User


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    conn = ConnectionHelper()
    print(conn)
    return User.create_user(conn, name, email, password, birthdate)


def get_user(email):
    # wrapper used for mocking
    conn = ConnectionHelper()
    return User.get_user(conn, email)


@app.route('/')
def home():
    return 'Invalid page', 403


@app.route('/user/login', methods=['POST'])
def user_login():
    if request.method == 'POST':
        _json = request.get_json()
        email = _json['email']
        password = _json['password']
        user = get_user(email)

        if user:
            if user.password == password:
                return safe_user_json(user), 200

        return 'Not acceptable', 406


@app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        _json = request.get_json()
        name = _json['name']
        email = _json['email']
        password = _json['password']
        birthdate = None
        _user = create_user(name, email, password, birthdate)

        return safe_user_json(_user), 200
