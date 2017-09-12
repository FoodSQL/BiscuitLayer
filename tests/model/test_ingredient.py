import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.ingredient import Ingredient
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreateIngredientTestCase(
unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.ingredient = Ingredient.get_ingredient(
            self.conn,
            4
        )

    def test_exists(self):
        assert self.ingredient is not None

    def test_name_is_correct(self):
        assert 'eggs' in self.ingredient._name


    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT _name FROM Ingredient WHERE _name="eggs"'
        )
        assert 'eggs' in ans



if __name__ == '__main__':
    unittest.main()
