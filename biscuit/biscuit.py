from flask import Flask, request, jsonify
from biscuit.util.json_format import user_json
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.user import User


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    conn = ConnectionHelper()
    return User.create_user(conn, name, email, password, birthdate)

def create_ingredient(_name, price_range):
    conn = ConnectionHelper()
    return Ingredient.create_ingredient(conn, _name, price_range)
    
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
