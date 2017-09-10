import unittest
import json
import biscuit

from biscuit.util.json_format import *
from tests.mock.user_mock import *
from tests.mock.ingredient_mock import *
from tests.mock.pantry_mock import *


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
        self.json = user_pantries_json(self.user, self.pantries)


    def tearDown(self):
        pass


    def test_outter_json_integrity(self):
        assert 'Goku' in self.json['name']
        assert 'goku@dragonball.com.jp' in self.json['email']


    def test_pantry_json_integrity(self):
        assert 'My Food' in self.json['pantries'][0]['pantry_name']
        assert 'My Drinks' in self.json['pantries'][1]['pantry_name']
