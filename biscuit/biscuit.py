from flask import Flask, request, jsonify
from biscuit.util.json_format import *
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.user import User

import biscuit.model.pantry2 as pantry2
import biscuit.model.ingredient as ingredient


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    conn = ConnectionHelper()
    print(conn)
    return User.create_user(conn, name, email, password, birthdate)

def create_ingredient(_name, price_range):
    conn = ConnectionHelper()
    return Ingredient.create_ingredient(conn, _name, price_range)


def get_user(email):
    # wrapper used for mocking
    conn = ConnectionHelper()
    return User.get_user(conn, email)


def get_user_by_id(user_id):
    conn = ConnectionHelper()
    return User.get_user_by_id(conn, user_id)


def _get_pantries(user):
    conn = ConnectionHelper()
    return pantry2.get_pantries(conn, user)


def get_ingredient_list():
    conn = ConnectionHelper()
    return get_all_ingredients()


def create_pantry(pantry_name, user_id):
    conn = ConnectionHelper()
    return pantry2.create_pantry_with_user(conn, pantry_name, user_id)


def add_item_to_pantry(pantry_id, item_id, amount, unit):
    conn = ConnectionHelper()
    pantry = pantry2.Pantry.get_pantry(conn, pantry_id)
    pantry.add_item(conn, item_id, amount, unit)
    return pantry


def remove_item_from_pantry(pantry, item_id, amount, unit):
    conn = ConnectionHelper()
    pantry.remove_item(conn, item_id, amount, unit)
    return pantry


def get_pantry_by_id(pantry_id):
    return pantry2.Pantry.get_pantry(ConnectionHelper(), pantry_id)


@app.route('/pantry/add_item', methods=['POST'])
def pantry_add_item():
    if request.method == 'POST':
        _json = request.get_json()
        pantry_id = _json['pantry_id']
        item_id = _json['item_id']
        amount = _json['amount']
        add_item_to_pantry(pantry_id, item_id, amount, 'kg')
        return _json, 200


@app.route('/pantry/remove_item', methods=['POST'])
def pantry_remove_item():
    if request.method == 'POST':
        _json = request.get_json()
        pantry_id = _json['pantry_id']
        pantry = get_pantry_by_id(pantry_id)

        for item in _json['items']:
            item_id = item['item_id']
            amount = item['amount']
            remove_item_from_pantry(pantry, item_id, amount, 'kg')

        return _json, 200


@app.route('/pantry/new', methods=['POST'])
def post_create_pantry():
    if request.method == 'POST':
        _json = request.get_json()
        user_id = _json['user_id']
        pantry_name = _json['pantry_name']
        pantry = create_pantry(pantry_name, user_id)
        return new_pantry_json(user_id, pantry), 200


@app.route('/pantry/<user_id>', methods=['GET'])
def get_pantries(user_id):
    if request.method == 'GET':
        user = get_user_by_id(int(user_id))
        pantries = _get_pantries(user)
        if len(pantries) > 0:
            return user_pantries_json(user, pantries), 200
        else:
            return 'Pantries not found', 404


@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    if request.method == 'GET':
        return ingredients_json(get_ingredient_list()), 200


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
