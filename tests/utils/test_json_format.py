import unittest
import json
import biscuit

from biscuit.util.json_format import *
from tests.mock.user_mock import *
from tests.mock.ingredient_mock import *
from tests.mock.pantry_mock import *
from tests.mock.recipe_mock import *


class RecipeJSONFormatTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.pantry_id = 42
        self.recipes = [
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
        self.json = json.loads(
            possible_recipes_json(self.recipes, self.pantry_id))


    def test_outter_json_integrity(self):
        self.assertEquals(42, self.json['pantry_id'])


    def test_recipes_list(self):
        _list = self.json['recipes']
        self.assertEquals(42, _list[0]['recipe_id'])
        self.assertEquals(30, _list[1]['recipe_id'])
        assert 'pasta & pesto' in _list[2]['recipe_name'].lower()
        assert 'provoleta' in _list[3]['recipe_name'].lower()


    def test_ingredients_list(self):
        _list = self.json['recipes'][3]['recipe_ingredients']
        self.assertEquals(22, _list[0]['ingredient_id'])
        self.assertEquals(11, _list[1]['ingredient_id'])
        assert 'olive oil' in _list[2]['ingredient_name'].lower()
        assert 'paprika' in _list[3]['ingredient_name'].lower()


class PantryJSONFormatTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.user = User_Mock(
            None,
            'Goku',
            'goku@dragonball.com.jp',
            'freeza.sux123',
            '30/04/1994'
        )
        self.pantries = [
            Pantry_Mock(12, 'My Food', [
                Ingredient_Mock(42, 'Potato', 3),
                Ingredient_Mock(77, 'Paprika', 4),
                Ingredient_Mock(32, 'Papaya', 99),
            ]),
            Pantry_Mock(92, 'My Drinks', [
                Ingredient_Mock(92, 'Cake', 3),
                Ingredient_Mock(7,  'Coke', 4),
                Ingredient_Mock(91, 'Pepsi', 99),
                Ingredient_Mock(44, 'Diet Coke', 30982),
            ])
        ]
        self.json = json.loads(user_pantries_json(self.user, self.pantries))


    def tearDown(self):
        pass


    def test_outter_json_integrity(self):
        self.assertEquals(42, self.json['user_id'])


    def test_pantry_json_integrity(self):
        assert 'My Food' in self.json['pantries'][0]['pantry_name']
        assert 'My Drinks' in self.json['pantries'][1]['pantry_name']
