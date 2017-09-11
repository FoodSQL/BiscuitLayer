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
        cls.user = User.get_user(cls.conn, 'vegeta@dragonball.com')
        cls.conn.run('DELETE FROM User_pantry WHERE id_user=%s;', cls.user._id)
        cls.conn.run('DELETE FROM _User WHERE login="vegeta@dragonball.com";')
        cls.conn.run('DELETE FROM _User WHERE login="vegeta@dragonball.com";')
        cls.conn.run('''
            INSERT INTO
                _User(_name, login, _password, email)
            VALUES ("Vegeta", "vegeta@dragonball.com",
                    "goku.sux123", "vegeta@dragonball.com")
        ''')
        cls.user = User.get_user(cls.conn, 'vegeta@dragonball.com')

    @classmethod
    def tearDownClass(cls):
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
        cls.conn.run('DELETE FROM _User WHERE login="majinboo@dragonball.com"')
        cls.user = User.create_user(
            cls.conn,
            'Majin Boo',
            'majinboo@dragonball.com',
            'freeza.sux123',
            '30/04/1994'
        )


    @classmethod
    def tearDownClass(cls):
        pass

    def test_exists(self):
        assert self.user is not None

    def test_name_is_correct(self):
        assert 'Majin Boo' in self.user.name

    def test_password_is_correct(self):
        assert 'freeza.sux123' in self.user.password

    def test_email_is_correct(self):
        assert 'majinboo@dragonball.com' in self.user.email

    def test_is_in_db(self):
        ans = self.conn.run(
            'SELECT email FROM _User WHERE login="majinboo@dragonball.com"'
        )
        assert 'majinboo@dragonball.com' in ans

    def test_cannot_recreate(self):
        with self.assertRaises(IntegrityError):
            User.create_user(
                self.conn,
                'Majin Boo',
                'majinboo@dragonball.com',
                'freeza.sux123',
                '30/04/1994'
            )

if __name__ == '__main__':
    unittest.main()
