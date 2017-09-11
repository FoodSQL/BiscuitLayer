from tests.mock.ingredient_mock import *


class Recipe_Mock():

    def __init__(
            self,
            _id=42,
            _name='Cheese Dog',
            ingredients=[
                Ingredient_Mock(66, 'Sausage', 2),
                Ingredient_Mock(42, 'Cheese', 2),
                Ingredient_Mock(32, 'Bread', 1),
            ]):
        self._id = _id
        self._name = _name
        self.ingredients = ingredients
