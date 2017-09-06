import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.user_mock import User_Mock


def fake_ingredient(name, price_range):
    # Inserting mock mid-application
    return Ingredient_Mock(None, name, price_range)


class IngredientTestCase(unittest.TestCase):

    @patch('biscuit.biscuit.create_ingredient', side_effect=fake_ingredient)
    def setUp(self, mock):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.response = self.app.post(
            '/ingredient',
            data=json.dumps({
                '_name': 'Paprika',
                'price_range': 5
            }),
            content_type='application/json'
        )

    # def tearDown(self):
    #     # mostly used for closing files and db
    #     pass
    #
    # def test_was_success(self):
    #     self.assertEqual(self.response.status_code, 200)

    # def test_has_keys(self):
    #     _json = json.loads(self.response.get_data(as_text=True))
    #     assert 'Paprika' in _json['_name']
    #     assert _json['price_range'] == 5


if __name__ == '__main__':
    unittest.main()
