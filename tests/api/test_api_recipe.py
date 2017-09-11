import unittest
import json
import biscuit


from mock import patch, Mock
from tests.mock.recipe_mock import *
from tests.mock.ingredient_mock import *


def fake_fetch_recipes(pantry_id):
    return [
        Recipe_Mock(),
        Recipe_Mock(_name='Cheese HotDog', _id=30),
        Recipe_Mock(_id=66, _name='Pasta & Pesto', ingredients=[
            Ingredient_Mock(62, 'Pasta', 1),
            Ingredient_Mock(90, 'Pesto', 3),
            Ingredient_Mock(70, 'Cheese', 2),
        ]),
        Recipe_Mock(_id=21, _name='Provoleta', ingredients=[
            Ingredient_Mock(22, 'Provolone', 9),
            Ingredient_Mock(11, 'Flour', 1),
            Ingredient_Mock(24, 'Olive Oil', 3),
            Ingredient_Mock(74, 'Paprika', 2)
        ]),
    ]


class RecipeAPITestCase(unittest.TestCase):

    @patch('biscuit.biscuit.fetch_recipes', side_effect=fake_fetch_recipes)
    def setUp(self, mock):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.pantry_id = 42
        self.res = self.app.get('/recipes/{}'.format(self.pantry_id))
        self.json = json.loads(self.res.get_data(as_text=True))


    def tearDown(self):
        pass


    def test_reponse_status(self):
        self.assertEquals(200, self.res.status_code)


    # same tests as for the json integrity
    def test_outter_json_integrity(self):
        self.assertEquals(42, int(self.json['pantry_id']))


    def test_recipes_list(self):
        _list = self.json['recipes']
        self.assertEquals(42, int(_list[0]['recipe_id']))
        self.assertEquals(30, int(_list[1]['recipe_id']))
        assert 'pasta & pesto' in _list[2]['recipe_name'].lower()
        assert 'provoleta' in _list[3]['recipe_name'].lower()


    def test_ingredients_list(self):
        _list = self.json['recipes'][3]['recipe_ingredients']
        self.assertEquals(22, int(_list[0]['ingredient_id']))
        self.assertEquals(11, int(_list[1]['ingredient_id']))
        assert 'olive oil' in _list[2]['ingredient_name'].lower()
        assert 'paprika' in _list[3]['ingredient_name'].lower()
