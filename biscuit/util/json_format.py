from json import dumps

def user_json(user):
    return dumps({
        'id': user._id,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'birthdate': user.birthdate
    })
