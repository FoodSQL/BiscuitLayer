from json import dumps


STD_UNIT = 'kg'


def user_json(user):
    return dumps({
        'id': user._id,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'birthdate': user.birthdate
    })


def safe_user_json(user):
    return dumps({
        'id': user._id,
        'name': user.name,
        'email': user.email,
    })


def pantry_dictionary(pantry):
    _pantry = {}
    _pantry['pantry_id'] = pantry._id
    _pantry['pantry_name'] = pantry._name
    _pantry['items'] = []
    for item in pantry.get_ingredients():
        _pantry['items'].append(item_dictionary(item))
    return _pantry


def item_dictionary(item):
    _item = {}
    _item['item_id'] = item._id
    _item['item_name'] = item._name
    _item['item_amount'] = item.amount
    _item['item_unit'] = STD_UNIT
    return _item


def user_pantries_json(user, pantries):
    _json = { 'user_id': user._id }
    _json['pantries'] = []
    for pantry in pantries:
        _json['pantries'].append(pantry_dictionary(pantry))
    return dumps(_json)


def ingredients_json(items):
    ingredients = []
    for item in items:
        ingredients.append(item_dictionary(item))
    return dumps({ 'ingredients': ingredients })


def new_pantry_json(user_id, pantry):
    return dumps({
        'user_id': user_id,
        'pantry_name': pantry._name,
        'pantry_id': pantry._id,
    })


def pantry_add_item(pantry):
    return dumps(pantry_dictionary(pantry))


def pantry_remove_item(pantry):
    return dumps(pantry_dictionary(pantry))
