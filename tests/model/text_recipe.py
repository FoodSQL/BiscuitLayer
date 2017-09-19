import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.recipe import Recipe
from biscuit.model.ingredient import Ingredient
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreateRecipeTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        conn.run("""
            DELETE FROM
                Recipe_Ingredient
            WHERE
                id_recipe = 1
        """)
        conn.run("""
            DELETE FROM
                Recipe
            WHERE
                id = 1
        """)
        conn.run("""
            INSERT INTO
                Recipe
            VALUES
                (1, "Arroz", "Arroz facinho de fazer",
                "100")
        """)
        conn.run("""
            INSERT INTO
                Recipe_Ingredient
            VALUES
                (1, 4)
        """)

    def test_recipe(self):
        recipe = recipe.get_recipe_by_id(self.conn, 1):
        assert recipe is not None


if __name__ == '__main__':
    unittest.main()
