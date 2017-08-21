from flask import Flask, request, jsonify


app = Flask(__name__)


def create_user(name, email, password, birthdate):
    # wrapper used for mocking
    return User(name, email, password, birthdate)

@app.route('/')
def home():
    return 'Invalid page', 403


@app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        print(request.json['name'])
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        birthdate = request.json['birthdate']
        print(birthdate, email, name, password)

        user = create_user(name, email, password, birthdate)

        return jsonify(user), 200

    else:
        return 'Bad request', 400
