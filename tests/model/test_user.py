import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock


class CreateUserTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.conn = ConnectionHelper()
        self.user = User.create_user(
            self.conn,
            'Goku',
            'goku@dragonball.com',
            'freeza.sux123',
            '30/04/1994'
        )

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

    def test_get_user(self):
        user = User.get_user(self.conn, self.user.email)
        assert user.email in self.user.email

    def test_get_user_by_id(self):
        user = User.get_user_by_id(self.conn, self.user._id)
        assert user._id == self.user._id

if __name__ == '__main__':
    unittest.main()
