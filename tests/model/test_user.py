import unittest
import json

from biscuit import app
from mock import patch, Mock


def fake_user(name, email, password, birthdate):
    # Inserting mock mid-application
    user = User_Mock(name, email, password, birthdate)


class UserTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        # mostly used for closing files and db
        pass

    @patch('biscuit.create_user', side_effect=fake_user)
    def test_create_response(self):
        print(dir(biscuit))
        # mock = Mock()
        # mock.create_user.side_effect = fake_user  # where the magic happens
        response = self.app.post('/user', data=json.dumps({
            'name': 'Goku',
            'email': 'goku@dragonball.com',
            'password': 'freeza_sux123',
            'birthdate': '30/04/1994'
        }))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
