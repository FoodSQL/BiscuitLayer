import unittest
import json
import biscuit

from biscuit.model.user import User
from pymysql.err import IntegrityError
from biscuit.model.pantry2 import Pantry
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreatePantryTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.conn.run('DELETE FROM User_pantry WHERE id_user=163;')
        self.conn.run('DELETE FROM _User WHERE login="vegeta@dragonball.com";')
        self.conn.run('''
            INSERT INTO
                _User(_name, login, _password, email)
            VALUES ("Vegeta", "vegeta@dragonball.com",
                    "goku.sux123", "vegeta@dragonball.com")
        ''')
        self.user = User.get_user(self.conn, 'vegeta@dragonball.com')
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
        assert 'Minha Dispensa' in self.pantry._name

    #
    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT _name FROM pantry WHERE _name="Minha Dispensa 2"'
        )
        assert 'Minha Dispensa 2' in ans

    def test_get_pantry(self):
        pantry = Pantry.get_pantry(self.conn, 1)
        assert pantry._id == 1

if __name__ == '__main__':
    unittest.main()
