from flask import Flask, request, jsonify
from biscuit.util.json_format import *
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.user import User

import biscuit.model.recipe as recipe
import biscuit.model.pantry2 as pantry2
import biscuit.model.ingredient as ingredient
import json


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    conn = ConnectionHelper()
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
    return ingredient.get_all_ingredients(conn)


def create_pantry(pantry_name, user_id):
    conn = ConnectionHelper()
    return pantry2.create_pantry_with_user(conn, pantry_name, user_id)


def add_item_to_pantry(pantry_id, item_id, amount, unit):
    conn = ConnectionHelper()
    pantry = pantry2.Pantry.get_pantry(conn, pantry_id)
    ing = ingredient.Ingredient.get_ingredient(conn, item_id)
    pantry.add_ingredient(conn, ing)
    return pantry


def remove_item_from_pantry(pantry, item_id, amount, unit):
    conn = ConnectionHelper()
    print(item_id)
    ing = ingredient.Ingredient.get_ingredient(conn, item_id)
    pantry.remove_ingredient(conn, ing)
    return pantry


def get_pantry_by_id(pantry_id):
    return pantry2.Pantry.get_pantry(ConnectionHelper(), pantry_id)


def fetch_recipes(pantry_id):
    return recipes.fetch_recipe(ConnectionHelper(), pantry_id)


def update_user(user_id, user_name, user_email, user_password):
    return User.update_user(ConnectionHelper(), user_id, user_name,
                            user_email, user_password)


@app.route('/user/update', methods=['POST'])
def update_user():
    if request.method == 'POST':
        _json = request.get_json()
        user_id = int(_json['user_id'])
        user_name = str(_json['user_name'])
        user_email = str(_json['user_email'])
        user_password = str(_json['user_password'])

        user = update_user(user_id, user_name, user_email, user_password)
        return safe_user_json(user), 200


@app.route('/recipes/<pantry_id>', methods=['GET'])
def get_possible_recipes(pantry_id):
    if request.method == 'GET':
        recipes = fetch_recipes(int(pantry_id))
        return possible_recipes_json(recipes, pantry_id), 200


@app.route('/pantry/add_item', methods=['POST'])
def pantry_add_item():
    if request.method == 'POST':
        _json = request.get_json()
        pantry_id = _json['pantry_id']
        item_id = _json['item_id']
        amount = _json['amount']
        add_item_to_pantry(pantry_id, item_id, amount, 'kg')
        return json.dumps(_json), 200


@app.route('/pantry/remove_item', methods=['POST'])
def pantry_remove_item():
    if request.method == 'POST':
        _json = request.get_json()
        pantry_id = _json['pantry_id']
        _pantry = get_pantry_by_id(pantry_id)

        for item in _json['items']:
            item_id = item['item_id']
            # amount = item['item_amount']
            remove_item_from_pantry(_pantry, item_id, 0, 'kg')

        return json.dumps(_json), 200


@app.route('/pantry/new', methods=['POST'])
def post_create_pantry():
    if request.method == 'POST':
        _json = request.get_json()
        user_id = _json['user_id']
        pantry_name = _json['pantry_name']
        pantry = create_pantry(pantry_name, user_id)
        return new_pantry_json(user_id, pantry), 200  # Should have been 201


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

        return safe_user_json(_user), 200  # should have been 200 (created)
