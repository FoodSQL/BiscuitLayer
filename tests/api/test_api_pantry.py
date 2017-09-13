import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.user_mock import User_Mock
from tests.mock.ingredient_mock import *
from tests.mock.pantry_mock import *


def fake_get_user(user_id):
    user = User_Mock(None, 'Goku', 'a@b', '124', '01/01/1991')
    user._id = user_id
    return user


def fake_get_pantries(user):
    return [
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



class GetUserPantriesAPITestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()


    def tearDown(self):
        pass


    @patch('biscuit.biscuit._get_pantries', side_effect=fake_get_pantries)
    @patch('biscuit.biscuit.get_user_by_id', side_effect=fake_get_user)
    def test_was_success(self, mock, mock1):
        response = self.app.get('/pantry/1')
        _json = json.loads(response.get_data(as_text=True))

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, _json['user_id'])
        assert 'My Food'.lower() in _json['pantries'][0]['pantry_name'].lower()
        assert 'My Drink'.lower() in _json['pantries'][1]['pantry_name'].lower()
