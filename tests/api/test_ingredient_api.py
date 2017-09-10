import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.ingredient_mock import *


def fake_ingredient_list():
    return [
        Ingredient_Mock(42, 'Potato', 3),
        Ingredient_Mock(77, 'Paprika', 4),
        Ingredient_Mock(32, 'Papaya', 99),
        Ingredient_Mock(92, 'Cake', 3),
        Ingredient_Mock(7,  'Coke', 4),
        Ingredient_Mock(91, 'Pepsi', 99),
        Ingredient_Mock(44, 'Diet Coke', 30982),
    ]


class GetIngredientListAPITestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()

    def tearDown(self):
        pass

    @patch('biscuit.biscuit.get_ingredient_list', side_effect=fake_ingredient_list)
    def test_was_success(self, mock):
        response = self.app.get('/ingredients')
        _json = json.loads(response.get_data(as_text=True))

        self.assertEqual(200, response.status_code)
        assert 'potato' in _json['ingredients'][0]['item_name'].lower()
        assert 'paprika' in _json['ingredients'][1]['item_name'].lower()
        self.assertEqual(42, _json['ingredients'][0]['item_id'])
        self.assertEqual(77, _json['ingredients'][1]['item_id'])


if __name__ == '__main__':
    unittest.main()
