import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.pantry2 import Pantry
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock

class CreatePantryTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.pantry = Pantry.create_pantry(
            self.conn,
            'Minha Dispensa'
        )

    def tearDown(self):
        pass

    def test_exists(self):
        assert self.pantry is not None

    def test_name_is_correct(self):
        assert 'Minha Dispensa' in self.pantry._name


    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT _name FROM pantry WHERE _name="Minha Dispensa"'
        )
        assert 'Minha Dispensa' in ans


if __name__ == '__main__':
    unittest.main()
