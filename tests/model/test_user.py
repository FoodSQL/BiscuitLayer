import unittest
import json
import biscuit

from pymysql.err import IntegrityError
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper
from mock import patch, Mock


class UpdateUserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        biscuit.app.testing = True
        cls.app = biscuit.app.test_client()
        cls.conn = ConnectionHelper()
        cls.conn.run('DELETE FROM _User WHERE login="brolly@dragonball.com.jp"')
        cls.conn.run('''
            INSERT INTO
                _User(id, _name, login, _password, email)
            VALUES
                (1, "Brolly", "brolly@dragonball.com.jp",
                "everyone.sux123", "brolly@dragonball.com.jp")
        ''')
        cls.user_id = 1

        # update
        cls.user = User.update_user(cls.conn, cls.user_id, 'Bruno',
                                    'brolly@dragonball.com.jp', 'dabdab')


    @classmethod
    def tearDownClass(cls):
        pass


    def test_was_success(self):
        assert self.user_id == self.user._id
        assert 'bruno' in self.user.name.lower()
        assert 'brolly@dragonball.com.jp' in self.user.email.lower()
        assert 'dabdab' in self.user.password.lower()


class GetUserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        biscuit.app.testing = True
        cls.app = biscuit.app.test_client()
        cls.conn = ConnectionHelper()
        cls.conn.run('DELETE FROM User_Pantry')
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
