from flask import Flask, request, jsonify
# from tests.mock.user_mock import User_Mock
from biscuit.util.json_format import user_json
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.user import User


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    conn = ConnectionHelper()
    return User(conn, name, email, password, birthdate)

@app.route('/')
def home():
    return 'Invalid page', 403


@app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        _json = request.get_json()
        name = _json['name']
        email = _json['email']
        password = _json['password']
        birthdate = _json['birthdate']

        _user = create_user(name, email, password, birthdate)

        return user_json(_user), 200

    else:
        return 'Bad request', 400
