import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock


class GetUserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        biscuit.app.testing = True
        cls.app = biscuit.app.test_client()
        cls.conn = ConnectionHelper()
        cls.conn.run('DELETE FROM _User WHERE email="vegeta@dragonball.com"')
        cls.conn.run('''
            INSERT INTO
                _User(_name, login, _password, email)
            VALUES ("Vegeta", "vegeta@dragonball.com", "goku.sux123", "01/04/1992")
        ''')
        cls.user = User.get_user(cls.conn, 'vegeta@dragonball.com')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_exists(self):
        assert self.user is not None

    def test_name_is_correct(self):
        assert 'Vegeta' in self.user.name

    def test_password_is_correct(self):
        assert 'goku.sux123' in self.user.password

    def test_email_is_correct(self):
        assert 'vegeta@dragonball.com' in self.user.email

    def test_has_id(self):
        assert self.user._id is not None


class CreateUserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        biscuit.app.testing = True
        cls.app = biscuit.app.test_client()
        cls.conn = ConnectionHelper()
        cls.conn.run('DELETE FROM _User WHERE email="goku@dragonball.com"')
        cls.user = User.create_user(
            cls.conn,
            'Goku',
            'goku@dragonball.com',
            'freeza.sux123',
            '30/04/1994'
        )

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_exists(self):
        assert self.user is not None

    def test_name_is_correct(self):
        assert 'Goku' in self.user.name

    def test_password_is_correct(self):
        assert 'freeza.sux123' in self.user.password

    def test_email_is_correct(self):
        assert 'goku@dragonball.com' in self.user.email

    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT email FROM _User WHERE login="goku@dragonball.com"'
        )
        assert 'goku@dragonball.com' in ans

    def test_cannot_recreate(self):
        with self.assertRaises(IntegrityError):
            User.create_user(
                self.conn,
                'Goku',
                'goku@dragonball.com',
                'freeza.sux123',
                '30/04/1994'
            )

if __name__ == '__main__':
    unittest.main()
