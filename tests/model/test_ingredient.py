import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.ingredient import Ingredient
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreateIngredientTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.ingredient = Ingredient.create_ingredient(
            self.conn,
            'Paprika',
            5
        )

    def tearDown(self):
        pass

    def test_exists(self):
        assert self.ingredient is not None

    def test_name_is_correct(self):
        assert 'Paprika' in self.ingredient._name

    def test_price_is_correct(self):
        assert self.ingredient.price_range == 5

    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT _name FROM ingredient WHERE _name="Paprika"'
        )
        assert 'Paprika' in ans

    def test_cannot_recreate(self):
        with self.assertRaises(IntegrityError):
            Ingredient.create_ingredient(
                self.conn,
                'Paprika',
                5
            )

if __name__ == '__main__':
    unittest.main()
