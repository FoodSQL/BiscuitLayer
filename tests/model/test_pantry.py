import unittest
import json
import biscuit

from biscuit.model.user import User
from pymysql.err import IntegrityError
from biscuit.model.pantry2 import Pantry
from biscuit.model.ingredient import Ingredient
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreatePantryTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.user = User.get_user(self.conn, 'vegeta@dragonball.com')
        self.conn.run('DELETE FROM User_Pantry WHERE id_user=%s;', self.user._id)
        self.conn.run('DELELE FROM Ingredient WHERE id=4')
        self.conn.run('INSERT INTO Ingredient (id, _name) VALUES (4, "eggs")')
        self.conn.run('DELETE FROM _User WHERE login="vegeta@dragonball.com";')
        self.conn.run('''
            INSERT INTO
                _User(_name, login, _password, email)
            VALUES ("Vegeta", "vegeta@dragonball.com",
                    "goku.sux123", "vegeta@dragonball.com")
        ''')
        self.user = User.get_user(self.conn, 'vegeta@dragonball.com')
        self.ingredient = Ingredient.get_ingredient(
            self.conn,
            4
        )
        self.pantry = Pantry.create_pantry(
            self.conn,
            'Minha Dispensa 2',
            self.user._id
        )

    # def tearDown(self):
    #     pass
    #
    def test_exists(self):
        assert self.pantry is not None

    def test_name_is_correct(self):
        assert 'Minha Dispensa 2' in self.pantry._name


    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT _name FROM pantry WHERE _name="Minha Dispensa 2"'
        )
        assert 'Minha Dispensa 2' in ans

    def test_is_related(self):
        ans = self.conn.run(
            'SELECT id_pantry FROM User_Pantry WHERE id_pantry=%s',
            self.pantry._id
        )
        assert ans[0] == self.pantry._id

    def test_has_ingredient(self):
        self.conn.run('DELETE FROM Ingredient_Pantry WHERE id_ingredient=%s', self.ingredient._id)
        self.pantry.add_ingredient(self.conn, self.ingredient)
        assert self.ingredient._name in self.pantry.ingredients[0]._name

    def test_ingredient_relation(self):
        ans = self.conn.run(
            'SELECT id_ingredient FROM Ingredient_Pantry WHERE id_ingredient=%s',
            self.ingredient._id
        )
        assert self.ingredient._id == ans[0]


    # def test_get_pantry(self):
    #     pantry = Pantry.get_pantries(self.conn, self.user._id)
    #     assert pantry._id == 1

    def test_list_exists(self):
        pantries = Pantry.get_pantries(self.conn, self.user._id)
        assert pantries is not None

    def test_list_has_pantry(self):
        pantries = Pantry.get_pantries(self.conn, self.user._id)
        assert self.pantry._name in pantries[0]._name

    def test_remove_ingredient(self):
        self.pantry.remove_ingredient(self.conn, self.ingredient)
        for i in self.pantry.ingredients:
            assert self.ingredient._name not in i._name

    def test_remove_ingredient_from_db(self):
        ans = self.conn.run(
        """
        SELECT * FROM Ingredient_Pantry
        WHERE id_pantry = %s
        AND id_ingredient = %s
        """ , (self.pantry._id, self.ingredient._id)
        )
        assert ans is None


if __name__ == '__main__':
    unittest.main()
