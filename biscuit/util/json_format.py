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
    added_items = set()
    for item in pantry.get_ingredients():
        if item._id not in added_items:
            added_items.add(item._id)
            _pantry['items'].append(item_dictionary(item))
    return _pantry


def item_dictionary(item):
    _item = {}
    _item['item_id'] = item._id
    _item['item_name'] = item._name
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


def ingredient_dictionary(ingredient):
    return {
        'ingredient_id': ingredient._id,
        'ingredient_name': ingredient._name,  # TODO: check _
    }


def recipe_dictionary(recipe):
    res = {
        'recipe_id': recipe._id,
        'recipe_name': recipe._name,  # TODO: check _
        'recipe_percentage': recipe.percentage,
        'recipe_ingredients': []
    }
    for ingredient in recipe.ingredients:
        res['recipe_ingredients'].append(ingredient_dictionary(ingredient))
    return res

def possible_recipes_json(recipes, pantry_id):
    res = {
        'pantry_id': pantry_id,
        'recipes': [],
    }

    for recipe in recipes:
        res['recipes'].append(recipe_dictionary(recipe))

    return dumps(res)
