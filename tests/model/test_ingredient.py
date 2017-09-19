import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.ingredient import Ingredient
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreateIngredientTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        biscuit.app.testing = True
        cls.app = biscuit.app.test_client()
        cls.conn = ConnectionHelper()
        cls.conn.run('DELETE FROM Recipe_Ingredient WHERE id_ingredient=4')
        cls.conn.run('DELETE FROM Ingredient WHERE id=4')
        cls.conn.run('INSERT INTO Ingredient(id, _name) VALUES (4, "eggs")')
        cls.ingredient = Ingredient.get_ingredient(
            cls.conn,
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

    def test_get_all_ingredients(self):
        query = ("SELECT * FROM Ingredient")
        db_ingredients_list = self.conn.runall(query)
        ingredients_list = Ingredient.get_all_ingredients(self.conn)
        assert len(ingredients_list) == len(db_ingredients_list)


if __name__ == '__main__':
    unittest.main()
